"""Arm C fine-tuning, DDP on 2x T4 (adapted from laya's Kaggle notebook,
notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb in github.com/NandhaKishorM/laya).

Usage: torchrun --standalone --nproc_per_node=2 finetune/train_ddp.py <model_dir> <items.pt>
       <manifest.json> <output_dir> [epochs]

Unchanged from the notebook: the loss (proper-scoring-rule policy gradient on noisy logits +
soft cross-entropy), optimiser (AdamW, encoder 2.5e-5, head 1e-4, cosine), fp16 autocast,
gradient checkpointing, the DDP shard trim, per-epoch rolling checkpoint, and the post-training
temperature fit on held-out items. Changed for this benchmark: items come from `prepare.py`
(train-split units only); the temperature hold-out is by document (the manifest's
`temperature_holdout_doc_ids`) instead of a random item slice; max_len 512 / head 192 (arm C);
3 epochs; `training_meta.json` records the manifest hash, settings and per-epoch loss. Nothing is
pushed anywhere.
"""

import hashlib
import json
import os
import random
import sys
import time

import torch
import torch.distributed as dist
from laya.common import build_model, proper_reward
from safetensors.torch import load_file, save_file
from torch.nn.parallel import DistributedDataParallel as DDP
from transformers import AutoTokenizer

SEED = 20260930
MICRO_BATCH, GRAD_ACCUM, GROUP_SIZE = 8, 4, 4  # effective 64 sequences over 2 GPUs
LR_ENCODER, LR_HEAD = 2.5e-5, 1.0e-4
SIGMA_START, SIGMA_END = 0.4, 0.1
MAX_LEN, HEAD_MAX_LEN = 512, 192


def collate(items, pad_id):
    n, L = len(items), max(len(it["ids"]) for it in items)
    kmax = max(len(it["markers"]) for it in items)
    ids = torch.full((n, L), pad_id, dtype=torch.long)
    att = torch.zeros((n, L), dtype=torch.long)
    mpos = torch.zeros((n, kmax), dtype=torch.long)
    mmask = torch.zeros((n, kmax), dtype=torch.bool)
    target = torch.zeros((n, kmax), dtype=torch.float32)
    for i, it in enumerate(items):
        ids[i, : len(it["ids"])] = torch.tensor(it["ids"])
        att[i, : len(it["ids"])] = 1
        k = len(it["markers"])
        mpos[i, :k] = torch.tensor(it["markers"])
        mmask[i, :k] = True
        target[i, : len(it["target"])] = torch.tensor(it["target"], dtype=torch.float32)
    return {
        "input_ids": ids,
        "attention_mask": att,
        "marker_pos": mpos,
        "marker_mask": mmask,
        "target": target,
        "qtype": torch.tensor([it["qtype"] for it in items]),
    }


def fit_one_temp(sel):
    if len(sel) < 10:
        return 1.0
    kmax = max(len(z) for z, _ in sel)
    Z = torch.full((len(sel), kmax), -1e4)
    T = torch.zeros((len(sel), kmax))
    for i, (z, t) in enumerate(sel):
        Z[i, : len(z)] = torch.tensor(z)
        T[i, : len(t)] = torch.tensor(t, dtype=torch.float32)
    log_t = torch.zeros(1, requires_grad=True)
    opt = torch.optim.LBFGS([log_t], lr=0.1, max_iter=100)

    def closure():
        opt.zero_grad()
        loss = -(T * torch.log_softmax(Z / log_t.exp(), -1)).sum(-1).mean()
        loss.backward()
        return loss

    opt.step(closure)
    return float(torch.clamp(log_t.exp(), 0.1, 10.0).item())


def main():
    dist.init_process_group("nccl")
    rank, world = dist.get_rank(), dist.get_world_size()
    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    torch.cuda.set_device(local_rank)
    device = torch.device("cuda", local_rank)
    model_dir, items_path, manifest_path, output_dir = sys.argv[1:5]
    epochs = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    random.seed(SEED + rank)
    torch.manual_seed(SEED)

    with open(os.path.join(model_dir, "rl_agent_config.json")) as f:
        cfg = json.load(f)
    cfg.update(
        gradient_checkpointing=True,
        max_tokens_per_batch=4096,
        max_len=MAX_LEN,
        head_max_len=HEAD_MAX_LEN,
    )
    tok = AutoTokenizer.from_pretrained(os.path.join(model_dir, "tokenizer"))
    model = build_model(cfg, encoder_dir=os.path.join(model_dir, "encoder"))
    model.load_state_dict(load_file(os.path.join(model_dir, "model.safetensors")), strict=True)
    model.encoder.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )
    model.head_checkpointing = True
    model.to(device).train()
    ddp_model = DDP(model, device_ids=[local_rank], find_unused_parameters=True)

    items = torch.load(items_path, weights_only=False)
    calib_items = [it for it in items if it["holdout"]]  # held-out train documents
    train_items = [it for it in items if not it["holdout"]]
    train_items.sort(key=lambda it: (len(it["ids"]), it["label"]))  # same order on every rank
    random.Random(SEED).shuffle(train_items)
    train_items = train_items[: len(train_items) // world * world]  # equal shards (no deadlock)
    my_items = train_items[rank::world]

    enc = [p for n, p in ddp_model.named_parameters() if "encoder." in n]
    head = [p for n, p in ddp_model.named_parameters() if "encoder." not in n]
    optimizer = torch.optim.AdamW(
        [{"params": enc, "lr": LR_ENCODER}, {"params": head, "lr": LR_HEAD}], weight_decay=0.01
    )
    total_updates = (len(my_items) // (MICRO_BATCH * GRAD_ACCUM)) * epochs
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=max(1, total_updates), eta_min=1e-6
    )
    scaler = torch.amp.GradScaler("cuda", enabled=True)
    if rank == 0:
        print(
            f"{len(train_items)} train items ({len(calib_items)} held out), {len(my_items)} "
            f"per rank, {epochs} epochs",
            flush=True,
        )
    t0, epoch_losses = time.time(), []
    for epoch in range(epochs):
        random.Random(SEED + 1000 * epoch + rank).shuffle(my_items)
        sigma = SIGMA_START + (SIGMA_END - SIGMA_START) * epoch / max(1, epochs - 1)
        epoch_loss, n_batches, accum = 0.0, 0, 0
        optimizer.zero_grad(set_to_none=True)
        for b in range(0, len(my_items), MICRO_BATCH):
            batch = collate(my_items[b : b + MICRO_BATCH], tok.pad_token_id)
            with torch.autocast("cuda", dtype=torch.float16):
                logits, act = ddp_model(
                    batch["input_ids"].to(device),
                    batch["attention_mask"].to(device),
                    batch["marker_pos"].to(device),
                    batch["marker_mask"].to(device),
                    batch["qtype"].to(device),
                )
            logits = logits.float()
            mask = batch["marker_mask"].to(device)
            k = mask.sum(-1, keepdim=True).float()
            target = batch["target"].to(device)
            eps = torch.randn((GROUP_SIZE,) + logits.shape, device=device) * sigma * mask
            eps = (eps - eps.sum(-1, keepdim=True) / k) * mask
            z = logits.detach().unsqueeze(0) + eps
            q = torch.softmax(z.masked_fill(~mask, -1e4), -1)
            with torch.no_grad():
                r = proper_reward(
                    q, target.unsqueeze(0), batch["qtype"].to(device), mask, w_sph=0.75, w_rps=1.0
                )
                adv = r - r.mean(0, keepdim=True)
                adv = adv / (adv.std() + 1e-6)
            logp = -(((z - logits.unsqueeze(0)) ** 2) * mask).sum(-1) / (2 * sigma**2)
            loss_rl = -(adv * logp).mean()
            loss_ce = (
                -(target * torch.log_softmax(logits.masked_fill(~mask, -1e4), -1)).sum(-1).mean()
            )
            loss = (loss_rl + loss_ce) / GRAD_ACCUM + 0.0 * act.sum()
            scaler.scale(loss).backward()
            accum += 1
            if accum % GRAD_ACCUM == 0 or b + MICRO_BATCH >= len(my_items):
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(ddp_model.parameters(), 1.0)
                scaler.step(optimizer)
                scaler.update()
                scheduler.step()
                optimizer.zero_grad(set_to_none=True)
            epoch_loss += loss.item() * GRAD_ACCUM
            n_batches += 1
            if rank == 0 and n_batches % 100 == 0:
                print(
                    f"  epoch {epoch + 1}/{epochs} step {n_batches} loss {loss.item() * GRAD_ACCUM:.4f}"
                    f" ({time.time() - t0:.0f}s)",
                    flush=True,
                )
        epoch_losses.append(epoch_loss / max(1, n_batches))
        if rank == 0:
            print(
                f"=== epoch {epoch + 1}/{epochs} done in {time.time() - t0:.0f}s, avg loss "
                f"{epoch_losses[-1]:.4f} ===",
                flush=True,
            )
            ck = os.path.join(output_dir, "checkpoint_latest")
            os.makedirs(ck, exist_ok=True)
            save_file(
                {k: v.half().contiguous().cpu() for k, v in model.state_dict().items()},
                os.path.join(ck, "model.safetensors"),
            )
        dist.barrier()

    if rank == 0:
        model.eval()
        preds = []
        with torch.no_grad():
            for c in range(0, len(calib_items), 16):
                chunk = calib_items[c : c + 16]
                cb = collate(chunk, tok.pad_token_id)
                with torch.autocast("cuda", dtype=torch.float16):
                    lsub, _ = model(
                        cb["input_ids"].to(device),
                        cb["attention_mask"].to(device),
                        cb["marker_pos"].to(device),
                        cb["marker_mask"].to(device),
                        cb["qtype"].to(device),
                    )
                lnp = lsub.float().cpu().numpy()
                for i, it in enumerate(chunk):
                    preds.append((it["qtype"], lnp[i, : len(it["markers"])], it["target"]))
        temps = [1.0, 1.0, 1.0]
        for qt in range(3):
            sel = [(z, t) for q_t, z, t in preds if q_t == qt]
            if sel:
                temps[qt] = fit_one_temp(sel)
        print("checkpoint temperatures (choice, score, noul):", [round(t, 3) for t in temps])
        os.makedirs(output_dir, exist_ok=True)
        save_file(
            {k: v.half().contiguous().cpu() for k, v in model.state_dict().items()},
            os.path.join(output_dir, "model.safetensors"),
        )
        model.encoder.config.save_pretrained(os.path.join(output_dir, "encoder"))
        tok.save_pretrained(os.path.join(output_dir, "tokenizer"))
        cfg.update(fine_tuned=True, model_name="laya-pii-bench-arm-c", temperature=temps)
        cfg.pop("temperature_by_options", None)
        cfg.pop("gradient_checkpointing", None)
        with open(os.path.join(output_dir, "rl_agent_config.json"), "w") as f:
            json.dump(cfg, f, indent=2)
        with open(manifest_path, "rb") as f:
            manifest_sha = hashlib.sha256(f.read()).hexdigest()
        meta = {
            "manifest_sha256": manifest_sha,
            "items": len(items),
            "train_items": len(train_items),
            "temperature_holdout_items": len(calib_items),
            "epochs": epochs,
            "seed": SEED,
            "micro_batch": MICRO_BATCH,
            "grad_accum": GRAD_ACCUM,
            "world_size": world,
            "lr_encoder": LR_ENCODER,
            "lr_head": LR_HEAD,
            "max_len": MAX_LEN,
            "head_max_len": HEAD_MAX_LEN,
            "epoch_losses": epoch_losses,
            "temperatures": temps,
            "seconds": round(time.time() - t0),
            "torch": torch.__version__,
            "gpus": [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())],
        }
        with open(os.path.join(output_dir, "training_meta.json"), "w") as f:
            json.dump(meta, f, indent=2)
        print(f"saved {output_dir}", flush=True)
    dist.destroy_process_group()


if __name__ == "__main__":
    main()
