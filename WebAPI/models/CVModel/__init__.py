from typing import List

class MultiLanguageText:
    ESP: str
    ENG: str

class EmploymentHistory:
    position: MultiLanguageText
    client: str
    company: str
    date_range: MultiLanguageText
    work_model: str
    out_sourcing: bool
    current_job: bool
    functions: List[MultiLanguageText]

    def __init__(self, position: MultiLanguageText, client: str, company: str, date_range: MultiLanguageText, out_sourcing: bool, current_job: bool, functions: List[MultiLanguageText], work_model: str) -> None:
        self.position = position
        self.client = client
        self.company = company
        self.date_range = date_range
        self.out_sourcing = out_sourcing
        self.current_job = current_job
        self.functions = functions
        self.work_model = work_model


class Certification:
    title: str
    educational_institution: str
    certification_date: str

    def __init__(self, title: str, educational_institution: str, certification_date: str) -> None:
        self.title = title
        self.educational_institution = educational_institution
        self.certification_date = certification_date


class Formation:
    degree: str
    educational_institution: str
    end_date: str
    has_degree: bool

    def __init__(self, degree: str, educational_institution: str, end_date: str, has_degree: bool) -> None:
        self.degree = degree
        self.educational_institution = educational_institution
        self.end_date = end_date
        self.has_degree = has_degree
        

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
        
        
class ContactInfo: 
    icon: str 
    name: str
    value: str
    
    def __init__(self, icon: str, name: str, value: str) -> None:
        self.icon = icon
        self.name = name
        self.value = value
        
        
class Languages:
    language: str
    level: str
    certified: bool
    
    def __init__(self, language: str, level: str, certified: bool) -> None:
        self.language = language
        self.level = level
        self.certified = certified


class ProfessionalInfo:
    name: str
    career: MultiLanguageText
    profile_summary: MultiLanguageText
    picture_path: str
    contacts: List[ContactInfo]
    goals: List[MultiLanguageText]
    skills: List[str]
    formation: List[Formation]
    certification: List[Certification]
    languages: Languages
    refereces: List[Reference]

    def __init__(self, name: str, career: MultiLanguageText, profile_summary: MultiLanguageText, goals: List[MultiLanguageText], picture_path: str, languages: Languages, skills: List[str], formation: List[Formation], certification: List[Certification], references: List[Reference]) -> None:
        self.name = name
        self.career = career
        self.profile_summary = profile_summary
        self.goals = goals
        self.picture_path = picture_path
        self.skills = skills
        self.formation = formation
        self.certification = certification
        self.languages = languages
        self.references = references


class CV:
    professional_info: ProfessionalInfo
    employment_history: List[EmploymentHistory]

    def __init__(self, professional_info: ProfessionalInfo, employment_history: List[EmploymentHistory]) -> None:
        self.professional_info = professional_info
        self.employment_history = employment_history

