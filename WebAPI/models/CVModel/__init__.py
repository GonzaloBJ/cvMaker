from enum import Enum
from typing import List


class Career:
    esp: str
    eng: str

    def __init__(self, esp: str, eng: str) -> None:
        self.esp = esp
        self.eng = eng


class WorkModel(Enum):
    HYBRID = "hybrid"
    ON_SITE = "on-site"
    REMOTE = "remote"


class EmploymentHistory:
    position: Career
    client: str
    company: str
    date_range: Career
    work_model: WorkModel
    out_sourcing: bool
    current_job: bool
    functions: List[Career]

    def __init__(self, position: Career, client: str, company: str, date_range: Career, work_model: WorkModel, out_sourcing: bool, current_job: bool, functions: List[Career]) -> None:
        self.position = position
        self.client = client
        self.company = company
        self.date_range = date_range
        self.work_model = work_model
        self.out_sourcing = out_sourcing
        self.current_job = current_job
        self.functions = functions


class Certification:
    title: str
    educational_institution: str
    certification_date: int

    def __init__(self, title: str, educational_institution: str, certification_date: int) -> None:
        self.title = title
        self.educational_institution = educational_institution
        self.certification_date = certification_date


class Contact:
    icon: str
    name: str
    value: str

    def __init__(self, icon: str, name: str, value: str) -> None:
        self.icon = icon
        self.name = name
        self.value = value


class Formation:
    degree: str
    educational_institution: str
    end_date: int
    has_degree: bool

    def __init__(self, degree: str, educational_institution: str, end_date: int, has_degree: bool) -> None:
        self.degree = degree
        self.educational_institution = educational_institution
        self.end_date = end_date
        self.has_degree = has_degree


class Language:
    language: str
    level: str
    certified: bool

    def __init__(self, language: str, level: str, certified: bool) -> None:
        self.language = language
        self.level = level
        self.certified = certified


class Reference:
    contact_name: str
    position: str
    company: str
    phone_number: str
    email: str

    def __init__(self, contact_name: str, position: str, company: str, phone_number: str, email: str) -> None:
        self.contact_name = contact_name
        self.position = position
        self.company = company
        self.phone_number = phone_number
        self.email = email


class ProfessionalInfo:
    name: str
    career: Career
    profile_summary: Career
    picture_path: str
    contacts: List[Contact]
    goals: List[Career]
    skills: List[str]
    formation: List[Formation]
    certification: List[Certification]
    languages: List[Language]
    references: List[Reference]

    def __init__(self, name: str, career: Career, profile_summary: Career, picture_path: str, contacts: List[Contact], goals: List[Career], skills: List[str], formation: List[Formation], certification: List[Certification], languages: List[Language], references: List[Reference]) -> None:
        self.name = name
        self.career = career
        self.profile_summary = profile_summary
        self.picture_path = picture_path
        self.contacts = contacts
        self.goals = goals
        self.skills = skills
        self.formation = formation
        self.certification = certification
        self.languages = languages
        self.references = references


class SectionConfig:
    profile: Career
    formation: Career
    certification: Career
    languages: Career
    goals: Career
    skills: Career
    work_history: Career
    references: Career

    def __init__(self, profile: Career, formation: Career, certification: Career, languages: Career, goals: Career, skills: Career, work_history: Career, references: Career) -> None:
        self.profile = profile
        self.formation = formation
        self.certification = certification
        self.languages = languages
        self.goals = goals
        self.skills = skills
        self.work_history = work_history
        self.references = references


class Root:
    lang: str
    section_config: SectionConfig
    professional_info: ProfessionalInfo
    employment_history: List[EmploymentHistory]

    def __init__(self, lang: str, section_config: SectionConfig, professional_info: ProfessionalInfo, employment_history: List[EmploymentHistory]) -> None:
        self.lang = lang
        self.section_config = section_config
        self.professional_info = professional_info
        self.employment_history = employment_history
