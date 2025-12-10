from abc import ABC, abstractmethod

from blueprints.cvMaker.models import DefaultResponse

class ICVOutputDocumentStrategy(ABC):
    @abstractmethod
    def generate_from_rendered_template(self, cv_rendered_template: str, css_files: list[str], output_document: str) -> DefaultResponse:
        pass
    
    @abstractmethod    
    def get_cv_document_path(self, person_name: str, language_enum_name: str, file_extention: str) -> str:
        pass
