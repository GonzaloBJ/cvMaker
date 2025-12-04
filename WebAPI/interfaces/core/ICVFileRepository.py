from abc import ABC, abstractmethod

from blueprints.cvMaker.models import DefaultResponse

class ICVFileRepository(ABC):
    @abstractmethod
    def make_pdf_from_html(self, cv_rendered_template: str, css_files: list[str], output_pdf: str) -> DefaultResponse:
        pass
    
    @abstractmethod    
    def get_cv_file_path(self, person_name: str, language_enum_name: str, file_extention: str) -> str:
        pass
