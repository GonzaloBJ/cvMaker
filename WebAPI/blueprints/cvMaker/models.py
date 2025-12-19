from dataclasses import dataclass
from pydantic import BaseModel

from enums.cvMaker import EColorScheme
from enums.cvMaker import ELanguages

@dataclass
class DefaultResponse(BaseModel):
    status: str | None
    message: str | None
    file: str | None
    html: str | None
    
    def __init__(self, status: str | None = None, message: str | None = None, file: str | None = None, html: str | None = None) -> None:
        super().__init__(status=status, message=message, file=file, html=html)
    
    @staticmethod
    def success(message: str, file: str, html: str) -> 'DefaultResponse':
        return DefaultResponse(
            status= "Correcto", 
            message=message, 
            file=file, 
            html=html)
        
    @staticmethod
    def fail(message: str) -> 'DefaultResponse':
        return DefaultResponse(
            status= "Error", 
            message=message, 
            file=None, 
            html=None)

class QueryParams(BaseModel):
    template: str = 'basic'
    lang: str = 'ESP'
    person: str = 'gb'
    color: str = 'lightBlue'
    
    def color_to_enum(self):
        try:
            return EColorScheme(self.color).value
        except KeyError:
            return EColorScheme.LIGHT_BLUE.value
        
    def lang_to_enum(self):
        try:
            return ELanguages[self.lang]
        except KeyError:
            return ELanguages.ESP