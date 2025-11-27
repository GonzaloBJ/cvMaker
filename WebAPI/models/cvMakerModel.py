from typing import Any
from dataclasses import dataclass

from enums.cvMaker import EFileExtentions

@dataclass
class CVTemplate:
    name: str
    rootPath:str
    colorSchemesPath: str
    description: str

    def __init__(self, name: str, rootPath:str, colorSchemesPath: str, description: str) -> None:
        self.name = name
        self.rootPath = rootPath
        self.colorSchemesPath = colorSchemesPath
        self.description = description
        
    def get_html_path(self) -> str:
        return f"{self.rootPath}{self.name}{EFileExtentions.HTML.value}"
            
    def set_color_scheme_css_path(self, color_scheme: str) -> None:
        self.colorSchemesPath = f"{self.rootPath}{self.colorSchemesPath}{color_scheme}{EFileExtentions.CSS.value}"
    
    def get_css_path(self) -> str:
        return f"{self.rootPath}{self.name}{EFileExtentions.CSS.value}"

@dataclass
class CVDataSource:
    personAcronym: str
    personName: str
    dataPath: str

    def __init__(self, personAcronym: str, personName: str, dataPath: str) -> None:
        self.personAcronym = personAcronym
        self.personName = personName
        self.dataPath = dataPath

@dataclass
class Certification:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Certification':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Certification(_ESP, _ENG)

@dataclass
class Formation:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Formation':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Formation(_ESP, _ENG)

@dataclass
class Goals:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Goals':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Goals(_ESP, _ENG)

@dataclass
class Languages:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Languages':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Languages(_ESP, _ENG)

@dataclass
class Profile:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Profile(_ESP, _ENG)

@dataclass
class References:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'References':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return References(_ESP, _ENG)

@dataclass
class Skills:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'Skills':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return Skills(_ESP, _ENG)

@dataclass
class WorkHistory:
    ESP: str
    ENG: str

    @staticmethod
    def from_dict(obj: Any) -> 'WorkHistory':
        _ESP = str(obj.get("ESP"))
        _ENG = str(obj.get("ENG"))
        return WorkHistory(_ESP, _ENG)

@dataclass
class SectionConfig:
    profile: Profile
    formation: Formation
    certification: Certification
    languages: Languages
    goals: Goals
    skills: Skills
    workHistory: WorkHistory
    references: References

    @staticmethod
    def from_dict(obj: Any) -> 'SectionConfig':
        _profile = Profile.from_dict(obj.get("profile"))
        _formation = Formation.from_dict(obj.get("formation"))
        _certification = Certification.from_dict(obj.get("certification"))
        _languages = Languages.from_dict(obj.get("languages"))
        _goals = Goals.from_dict(obj.get("goals"))
        _skills = Skills.from_dict(obj.get("skills"))
        _workHistory = WorkHistory.from_dict(obj.get("workHistory"))
        _references = References.from_dict(obj.get("references"))
        return SectionConfig(_profile, _formation, _certification, _languages, _goals, _skills, _workHistory, _references)

@dataclass
class CVTemplateConfig:
    lang: str
    sectionConfig: SectionConfig

    @staticmethod
    def from_dict(obj: Any) -> 'CVTemplateConfig':
        _lang = str(obj.get("lang"))
        _sectionConfig = SectionConfig.from_dict(obj.get("sectionConfig"))
        return CVTemplateConfig(_lang, _sectionConfig)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)