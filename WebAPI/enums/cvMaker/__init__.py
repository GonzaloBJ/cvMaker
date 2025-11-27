from enum import Enum

class ELanguages(Enum):
    ESP = 0
    ENG = 1 
    
class EFileExtentions(Enum):
    PDF = ".pdf"
    DOCX = ".docx" 
    HTML = ".html"
    CSS = ".css"
    
class EWorkModel(Enum):
    HYBRID = "hybrid"
    ON_SITE = "on-site"
    REMOTE = "remote"
    
class EColorScheme(Enum):
    LIGHT_BLUE = "lightBlue"
    DARK_RED = "darkRed"
    DARK_GREY = "darkGrey"