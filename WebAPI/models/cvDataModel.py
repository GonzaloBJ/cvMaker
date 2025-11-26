from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Career:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Career':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Career(_ESP, _ENG)

@dataclass
class Certification:
    title: str
    educationalInstitution: str
    certificationDate: str

    @staticmethod
    def from_dict(obj: Any) -> 'Certification':
        _title = str(obj.get("title"))
        _educationalInstitution = str(obj.get("educationalInstitution"))
        _certificationDate = str(obj.get("certificationDate"))
        return Certification(_title, _educationalInstitution, _certificationDate)

@dataclass
class Contact:
    icon: str
    name: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Contact':
        _icon = str(obj.get("icon"))
        _name = str(obj.get("name"))
        _value = str(obj.get("value"))
        return Contact(_icon, _name, _value)

@dataclass
class DateRange:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'DateRange':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return DateRange(_ESP, _ENG)

@dataclass
class Description:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Description(_ESP, _ENG)
    
@dataclass
class Position:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Position':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Position(_ESP, _ENG)

@dataclass
class Function:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Function':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Function(_ESP, _ENG)

@dataclass
class EmploymentHistory:
    position: Position
    client: str
    company: str
    dateRange: DateRange
    workModel: str
    outSourcing: bool
    currentJob: bool
    description: Description
    functions: List[Function]

    @staticmethod
    def from_dict(obj: Any) -> 'EmploymentHistory':
        _position = Position.from_dict(obj.get("position"))
        _client = str(obj.get("client"))
        _company = str(obj.get("company"))
        _dateRange = DateRange.from_dict(obj.get("dateRange"))
        _workModel = str(obj.get("workModel"))
        _outSourcing = bool(obj.get("outSourcing"))
        _currentJob = bool(obj.get("currentJob"))
        _description = Description.from_dict(obj.get("description"))
        _functions = [Function.from_dict(y) for y in obj.get("functions")]
        return EmploymentHistory(_position, _client, _company, _dateRange, _workModel, _outSourcing, _currentJob, _description, _functions)

@dataclass
class Formation:
    degree: str
    educationalInstitution: str
    endDate: str
    hasDegree: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Formation':
        _degree = str(obj.get("degree"))
        _educationalInstitution = str(obj.get("educationalInstitution"))
        _endDate = str(obj.get("endDate"))
        _hasDegree = bool(obj.get("hasDegree"))
        return Formation(_degree, _educationalInstitution, _endDate, _hasDegree)


@dataclass
class Goal:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Goal':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Goal(_ESP, _ENG)

@dataclass
class Language:
    language: str
    level: str
    certified: bool
    certificationName: str

    @staticmethod
    def from_dict(obj: Any) -> 'Language':
        _language = str(obj.get("language"))
        _level = str(obj.get("level"))
        _certified = bool(obj.get("certified")) 
        _certificationName = str(obj.get("certificationName"))
        return Language(_language, _level, _certified, _certificationName)

@dataclass
class ProfileSummary:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileSummary':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return ProfileSummary(_ESP, _ENG)

@dataclass
class Reference:
    contactName: str
    position: str
    company: str
    phoneNumber: str
    email: str

    @staticmethod
    def from_dict(obj: Any) -> 'Reference':
        _contactName = str(obj.get("contactName"))
        _position = str(obj.get("position"))
        _company = str(obj.get("company"))
        _phoneNumber = str(obj.get("phoneNumber"))
        _email = str(obj.get("email"))
        return Reference(_contactName, _position, _company, _phoneNumber, _email)

@dataclass
class ProfessionalInfo:
    name: str
    career: Career
    profileSummary: ProfileSummary
    picturePath: str
    contacts: List[Contact]
    goals: List[Goal]
    skills: List[str]
    formation: List[Formation]
    certification: List[Certification]
    languages: List[Language]
    references: List[Reference]

    @staticmethod
    def from_dict(obj: Any) -> 'ProfessionalInfo':
        _name = str(obj.get("name"))
        _career = Career.from_dict(obj.get("career"))
        _profileSummary = ProfileSummary.from_dict(obj.get("profileSummary"))
        _picturePath = str(obj.get("picturePath"))
        _contacts = [Contact.from_dict(y) for y in obj.get("contacts")]
        _goals = [Goal.from_dict(y) for y in obj.get("goals")]
        _skills = [y for y in obj.get("skills")]
        _formation = [Formation.from_dict(y) for y in obj.get("formation")]
        _certification = [Certification.from_dict(y) for y in obj.get("certification")]
        _languages = [Language.from_dict(y) for y in obj.get("languages")]
        _references = [Reference.from_dict(y) for y in obj.get("references")]
        return ProfessionalInfo(_name, _career, _profileSummary, _picturePath, _contacts, _goals, _skills, _formation, _certification, _languages, _references)


@dataclass
class Root:
    professionalInfo: ProfessionalInfo
    employmentHistory: List[EmploymentHistory]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _professionalInfo = ProfessionalInfo.from_dict(obj.get("professionalInfo"))
        _employmentHistory = [EmploymentHistory.from_dict(y) for y in obj.get("employmentHistory")]
        return Root(_professionalInfo, _employmentHistory)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
