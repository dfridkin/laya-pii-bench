"""Seeded world: studies, sites, people and events. Documents are views of this world.

Constraints enforced here (docs/specs/generator.md, D-016, D-018):
- every person (patient, site staff, CRO monitor, sponsor contact, IRB staff) belongs to exactly
  one site, so a person's name can't cross split groups;
- site numbers are unique within a study; the split key is `study/site`;
- full names and family names are unique across the world, and institution/city names are
  invented stems that never reuse a person's family name (keeps V2 unambiguous);
- the same subject has one timeline (enrollment, visits, events) reused by every document.
"""

from __future__ import annotations

import random
import unicodedata
from datetime import date, timedelta
from typing import Literal

from faker import Faker
from pydantic import BaseModel, ConfigDict

from bench.config import GenSpec
from bench.domain import Lang, SubjectRole
from bench.generate import providers as pv
from bench.generate.seeds import rng, sub_seed

STUDY_START = date(2025, 1, 6)
VISIT_DAYS = (1, 15, 29, 57, 85)
AE_TERMS = (
    "headache", "nausea", "fatigue", "neutropenia", "rash", "diarrhoea", "dizziness",
    "pneumonia", "elevated ALT", "hypertension", "arthralgia", "insomnia",
)  # fmt: skip
CONMEDS = (
    ("paracetamol", "500 mg"), ("ibuprofen", "400 mg"), ("lisinopril", "10 mg"),
    ("metformin", "850 mg"), ("atorvastatin", "20 mg"), ("omeprazole", "20 mg"),
    ("amoxicillin", "500 mg"), ("levothyroxine", "50 mcg"),
)  # fmt: skip
LABS = (
    ("ALT", "U/L", 7, 56), ("AST", "U/L", 10, 40), ("Creatinine", "mg/dL", 0.6, 1.3),
    ("Hemoglobin", "g/dL", 12.0, 17.5), ("Platelets", "10^9/L", 150, 400),
    ("Neutrophils", "10^9/L", 1.8, 7.5),
)  # fmt: skip
INDICATIONS = ("moderate plaque psoriasis", "type 2 diabetes", "chronic heart failure",
               "rheumatoid arthritis", "non-small cell lung cancer")  # fmt: skip
LOCALES: dict[str, str] = {"en": "en_US", "de": "de_DE", "es": "es_ES", "pl": "pl_PL"}

# Invented place-name stems (no person names; not intended to match real places or hospitals).
PLACE_STEMS: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "en": (("North", "East", "West", "Linden", "Harrow", "Cedar", "Maple", "Ashford"),
           ("vale", "brook", "field", "haven", "crest", "ridge", "mere", "wood")),
    "de": (("Neu", "Ober", "Nieder", "Alt", "Kirch", "Wald", "Linden", "Birken"),
           ("waldstadt", "heide", "brunn", "feld", "tal", "hausen", "au", "stett")),
    "es": (("Villa", "Puerto", "Monte", "Valle", "Campo", "Río", "Torre", "Llano"),
           ("verde", "alto", "claro", "sereno", "dorado", "nuevo", "real", "hondo")),
    "pl": (("Nowa", "Stara", "Górna", "Dolna", "Wielka", "Mała", "Leśna", "Polna"),
           (" Wola", " Łąka", " Brzezina", " Dąbrowa", " Kępa", " Olszyna", " Górka", " Lipa")),
}  # fmt: skip
INSTITUTION = {
    "en": ("{city} Regional Medical Center", "{city} Clinical Research Institute"),
    "de": ("Klinikum {city}", "Studienzentrum {city}"),
    "es": ("Hospital Universitario {city}", "Centro de Investigación Clínica {city}"),
    "pl": ("Szpital Kliniczny {city}", "Centrum Badań Klinicznych {city}"),
}
STAFF_JOBS: tuple[tuple[str, SubjectRole, str], ...] = (
    ("pi", SubjectRole.STAFF, "Principal Investigator"),
    ("subi", SubjectRole.STAFF, "Sub-Investigator"),
    ("coordinator", SubjectRole.STAFF, "Study Coordinator"),
    ("pharmacist", SubjectRole.STAFF, "Research Pharmacist"),
    ("cra", SubjectRole.STAFF, "Clinical Research Associate"),  # CRO monitor, one site (D-018)
    ("sponsor_contact", SubjectRole.SPONSOR, "Clinical Trial Manager"),  # D-017
    ("irb_chair", SubjectRole.STAFF, "IRB Chair"),
    ("irb_admin", SubjectRole.STAFF, "IRB Administrator"),
)
CRO_DOMAIN = "northvale-cro.example.com"
SPONSOR_DOMAIN = "fenwick-tx.example.com"


class _M(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Person(_M):
    id: str
    given: str
    family: str
    sex: Literal["F", "M"]
    title: str  # "Dr." for investigators, else Ms./Mr.
    role: SubjectRole
    job: str
    job_title: str
    email: str | None
    phone: str | None


class AdverseEvent(_M):
    term: str
    onset: date
    resolved: date | None
    serious: bool
    grade: int
    related: bool


class ConMed(_M):
    drug: str
    dose: str
    start: date
    stop: date | None


class LabResult(_M):
    test: str
    unit: str
    value: float
    low: float
    high: float
    collected: date


class Deviation(_M):
    on: date
    description: str


class Subject(_M):
    person: Person
    subject_id: str
    rand_no: str
    dob: date
    mrn: str
    street: str
    postcode: str
    enrolled: date
    visits: list[date]
    aes: list[AdverseEvent]
    conmeds: list[ConMed]
    labs: list[LabResult]
    deviations: list[Deviation]

    @property
    def age(self) -> int:
        e, b = self.enrolled, self.dob
        return e.year - b.year - ((e.month, e.day) < (b.month, b.day))


class Site(_M):
    key: str  # "{protocol_no}/{site_no}": split group key (D-016)
    study: str  # protocol no
    site_no: str
    lang: Lang
    city: str
    institution: str
    domain: str  # institutional email domain (example.org)
    mrn_format: str
    staff: dict[str, Person]  # job -> person
    subjects: list[Subject]


class Study(_M):
    protocol_no: str
    compound: str
    nct: str
    eudract: str
    indication: str
    sites: list[Site]


class World(_M):
    seed: int
    sponsor: str
    studies: list[Study]

    def sites(self) -> list[Site]:
        return [s for st in self.studies for s in st.sites]

    def study_of(self, site: Site) -> Study:
        return next(st for st in self.studies if st.protocol_no == site.study)

    def persons(self) -> list[Person]:
        out: list[Person] = []
        for s in self.sites():
            out += [s.staff[j] for j, _, _ in STAFF_JOBS]
            out += [sub.person for sub in s.subjects]
        return out


Sex = Literal["F", "M"]


def _sex(r: random.Random) -> Sex:
    return "F" if r.random() < 0.5 else "M"


def _title(job: str, sex: Sex) -> str:
    if job in ("pi", "subi", "irb_chair"):
        return "Dr."
    return "Ms." if sex == "F" else "Mr."


def _ascii(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


class _Names:
    """Unique full and family names across the world, drawn per locale."""

    def __init__(self, seed: int) -> None:
        self.seed = seed
        self.families: set[str] = set()
        self.fakers = {lang: Faker(loc) for lang, loc in LOCALES.items()}

    def draw(self, lang: str, sex: str, key: str, forbidden: set[str]) -> tuple[str, str]:
        fk = self.fakers[lang]
        for attempt in range(200):
            fk.seed_instance(sub_seed(self.seed, "name", key, attempt))
            given = fk.first_name_female() if sex == "F" else fk.first_name_male()
            family = fk.last_name()
            if " " in given or "-" in family or " " in family or len(family) < 3:
                continue  # keep one-token names so surface variants stay well defined
            if family in self.families or family in forbidden or given == family:
                continue
            self.families.add(family)
            return given, family
        raise RuntimeError(f"could not draw a unique name for {key}")


def _place(lang: str, r: random.Random, used: set[str]) -> str:
    pre, suf = PLACE_STEMS[lang]
    for _ in range(100):
        name = r.choice(pre) + r.choice(suf)
        if name not in used:
            used.add(name)
            return name
    raise RuntimeError("ran out of place names")


def build(spec: GenSpec) -> World:
    seed, w = spec.seed, spec.world
    names = _Names(seed)
    places: set[str] = set()
    site_langs: list[Lang] = [lang for lang, n in sorted(w.site_locales.items()) for _ in range(n)]
    rng(seed, "site_langs").shuffle(site_langs)
    studies: list[Study] = []
    for si in range(w.studies):
        r = rng(seed, "study", si)
        compound = pv.compound_code(w.compound_prefix, r)
        protocol = pv.protocol_no(compound, r.randint(1, 30))
        sites: list[Site] = []
        for ti in range(w.sites_per_study):
            lang = site_langs[si * w.sites_per_study + ti]
            sr = rng(seed, "site", si, ti)
            city = _place(lang, sr, places)
            site_no = pv.site_no(si, ti)
            inst = sr.choice(INSTITUTION[lang]).format(city=city)
            kind = sr.choice(["hospital", "clinic", "crc"])
            domain = f"{_ascii(city).replace(' ', '')}-{kind}.example.org"
            staff: dict[str, Person] = {}
            for job, role, title in STAFF_JOBS:
                sex = _sex(sr)
                given, family = names.draw(lang, sex, f"{si}/{ti}/{job}", places)
                dom = (
                    CRO_DOMAIN
                    if job == "cra"
                    else SPONSOR_DOMAIN
                    if role is SubjectRole.SPONSOR
                    else domain
                )
                staff[job] = Person(
                    id=f"{protocol}/{site_no}/{job}", given=given, family=family, sex=sex,
                    title=_title(job, sex),
                    role=role, job=job, job_title=title,
                    email=f"{_ascii(given)[0]}.{_ascii(family)}@{dom}",
                    phone=pv.phone(lang, sr),
                )  # fmt: skip
            mrn_format = sr.choice(pv.MRN_FORMATS)
            subjects = [
                _subject(seed, si, ti, n, lang, site_no, protocol, mrn_format, city, names, places)
                for n in range(1, w.subjects_per_site + 1)
            ]
            sites.append(Site(
                key=f"{protocol}/{site_no}", study=protocol, site_no=site_no, lang=lang,
                city=city, institution=inst, domain=domain, mrn_format=mrn_format, staff=staff,
                subjects=subjects,
            ))  # fmt: skip
        studies.append(Study(
            protocol_no=protocol, compound=compound, nct=pv.nct_id(r), eudract=pv.eudract_no(r),
            indication=r.choice(INDICATIONS), sites=sites,
        ))  # fmt: skip
    return World(seed=seed, sponsor=w.sponsor, studies=studies)


def _subject(
    seed: int, si: int, ti: int, n: int, lang: str, site_no: str, protocol: str,
    mrn_format: str, city: str, names: _Names, places: set[str],
) -> Subject:  # fmt: skip
    r = rng(seed, "subject", si, ti, n)
    sex = _sex(r)
    given, family = names.draw(lang, sex, f"{si}/{ti}/subject/{n}", places)
    enrolled = STUDY_START + timedelta(days=r.randint(0, 260))
    age = r.randint(90, 95) if r.random() < 0.05 else r.randint(18, 84)  # some > 89 (phi_quasi)
    dob = enrolled - timedelta(days=age * 365 + r.randint(1, 360))
    fk = names.fakers[lang]
    fk.seed_instance(sub_seed(seed, "address", si, ti, n))
    street = fk.street_address().replace("\n", " ")
    postcode = fk.postcode()
    visits = [
        enrolled + timedelta(days=d - 1 + (r.randint(-2, 2) if d > 1 else 0)) for d in VISIT_DAYS
    ]
    aes: list[AdverseEvent] = []
    for _ in range(r.choice((0, 1, 1, 2, 3))):
        onset = visits[0] + timedelta(days=r.randint(2, 80))
        dur = r.randint(1, 20)
        aes.append(AdverseEvent(
            term=r.choice(AE_TERMS), onset=onset,
            resolved=onset + timedelta(days=dur) if r.random() < 0.8 else None,
            serious=r.random() < 0.15, grade=r.randint(1, 3), related=r.random() < 0.4,
        ))  # fmt: skip
    conmeds: list[ConMed] = []
    for drug, dose in r.sample(CONMEDS, r.randint(0, 3)):
        start = enrolled - timedelta(days=r.randint(0, 400))
        stop = start + timedelta(days=r.randint(5, 200)) if r.random() < 0.5 else None
        conmeds.append(ConMed(drug=drug, dose=dose, start=start, stop=stop))
    labs = [
        LabResult(test=t, unit=u, low=lo, high=hi, collected=v,
                  value=round(r.uniform(lo * 0.7, hi * 1.3), 1))
        for v in visits[:3] for t, u, lo, hi in LABS
    ]  # fmt: skip
    deviations = [
        Deviation(on=visits[r.randint(1, 4)], description=r.choice((
            "visit performed outside the protocol window", "ECG not performed at visit",
            "study drug dispensed without documented accountability check",
            "informed consent re-signature missing after amendment", "fasting status not recorded",
        )))
        for _ in range(r.choice((0, 0, 1, 2)))
    ]  # fmt: skip
    person = Person(
        id=f"{protocol}/{site_no}/subject/{n}", given=given, family=family, sex=sex,
        title=_title("subject", sex), role=SubjectRole.PATIENT, job="subject",
        job_title="Participant", email=None, phone=pv.phone(lang, r),
    )  # fmt: skip
    return Subject(
        person=person,
        subject_id=pv.subject_id(site_no, n),
        rand_no=pv.rand_no(r),
        dob=dob,
        mrn=pv.mrn(mrn_format, r),
        street=street,
        postcode=postcode,
        enrolled=enrolled,
        visits=visits,
        aes=aes,
        conmeds=conmeds,
        labs=labs,
        deviations=deviations,
    )
