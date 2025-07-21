from typing import List

class MultiLanguageText:
    ESP: str
    ENG: str
    
    def __init__(self, ESP: str, ENG: str) -> None:
        self.ESP = ESP
        self.ENG = ENG

class EmploymentHistory:
    position: MultiLanguageText
    client: str
    company: str
    dateRange: MultiLanguageText
    workModel: str
    outSourcing: bool
    currentJob: bool
    functions: List[MultiLanguageText]

    def __init__(self, position: MultiLanguageText, client: str, company: str, dateRange: MultiLanguageText, outSourcing: bool, currentJob: bool, functions: List[MultiLanguageText], workModel: str) -> None:
        self.position = position
        self.client = client
        self.company = company
        self.dateRange = dateRange
        self.outSourcing = outSourcing
        self.currentJob = currentJob
        self.functions = functions
        self.workModel = workModel


class Certification:
    title: str
    educationalInstitution: str
    certificationDate: str

    def __init__(self, title: str, educationalInstitution: str, certificationDate: str) -> None:
        self.title = title
        self.educationalInstitution = educationalInstitution
        self.certificationDate = certificationDate


class Formation:
    degree: str
    educationalInstitution: str
    endDate: str
    hasDegree: bool

    def __init__(self, degree: str, educationalInstitution: str, endDate: str, hasDegree: bool) -> None:
        self.degree = degree
        self.educationalInstitution = educationalInstitution
        self.endDate = endDate
        self.hasDegree = hasDegree
        

class Reference:
    contactName: str
    position: str
    company: str
    phoneNumber: str
    email: str

    def __init__(self, contactName: str, position: str, company: str, phoneNumber: str, email: str) -> None:
        self.contactName = contactName
        self.position = position
        self.company = company
        self.phoneNumber = phoneNumber
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
    profileSummary: MultiLanguageText
    picturePath: str
    contacts: List[ContactInfo]
    goals: List[MultiLanguageText]
    skills: List[str]
    formation: List[Formation]
    certification: List[Certification]
    languages: Languages
    refereces: List[Reference]

    def __init__(self, name: str, career: MultiLanguageText, profileSummary: MultiLanguageText, goals: List[MultiLanguageText], picturePath: str, languages: Languages, skills: List[str], formation: List[Formation], certification: List[Certification], references: List[Reference]) -> None:
        self.name = name
        self.career = career
        self.profileSummary = profileSummary
        self.goals = goals
        self.picturePath = picturePath
        self.skills = skills
        self.formation = formation
        self.certification = certification
        self.languages = languages
        self.references = references

class SectionConfig:
    profile: MultiLanguageText
    formation: MultiLanguageText
    certification: MultiLanguageText
    languages: MultiLanguageText
    goals: MultiLanguageText
    skills: MultiLanguageText
    workHistory: MultiLanguageText
    references: MultiLanguageText
    
    def __init__(self, profile: MultiLanguageText, formation: MultiLanguageText, certification: MultiLanguageText, languages: MultiLanguageText, goals: MultiLanguageText, skills: MultiLanguageText, workHistory: MultiLanguageText, references: MultiLanguageText) -> None:
        self.profile = profile
        self.formation = formation
        self.certification = certification
        self.languages = languages
        self.goals = goals
        self.skills = skills
        self.workHistory = workHistory
        self.references = references
        

class CV:
    lang: str
    sectionConfig: SectionConfig
    professionalInfo: ProfessionalInfo
    employmentHistory: List[EmploymentHistory]

    def __init__(self, sectionConfig: List[MultiLanguageText], professionalInfo: ProfessionalInfo, employmentHistory: List[EmploymentHistory]) -> None:
        self.lang: str = ""
        self.sectionConfig = sectionConfig
        self.professionalInfo = professionalInfo
        self.employmentHistory = employmentHistory

