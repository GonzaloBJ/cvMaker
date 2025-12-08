from dataclasses import asdict
from enums.cvMaker import EFileExtentions
from models.cvMakerModel import CVTemplateConfig

from repository.CVDataRepository import CVDataRepository
from repository.CVFileRepository import CVFileRepository
from repository.CVTemplateRepository import CVTemplateRepository
from utils import convert_person_fullname_to_short, convert_str_to_normalized

class CVMakerService():
    def __init__(self):
        self.cv_template_repo = CVTemplateRepository()
        self.cv_data_repo = CVDataRepository()
        self.cv_file_repo = CVFileRepository()
        
    def make_cv_from_file(self, language_name: str, color_scheme: str, person_acronym: str, template_name_param: str) :
        try:            
            # Get CV context data
            cv_data_path = self.cv_data_repo.get_path_by_person_acronym(person_acronym)
            cv_data = self.cv_data_repo.get_cv_data_by_path(cv_data_path)
            # Get CV template configuration
            cv_template_config: CVTemplateConfig = self.cv_template_repo.get_config(language_name)
             # Merge context data and template configuration
            cv_context = asdict(cv_template_config) | asdict(cv_data)
            # Get CV selected template
            cv_template = self.cv_template_repo.get_by_name_and_color(template_name_param, color_scheme)
            # Get rendered template
            cv_rendered_template = self.cv_template_repo.get_rendered_template(cv_template, cv_context) 
            # Get formatted person name
            formatted_person_name = self._get_formatted_person_name(cv_data.professionalInfo.name)
            # Generate output PDF file name
            output_pdf = self.cv_file_repo.get_cv_file_path(formatted_person_name, language_name, EFileExtentions.PDF.value)
            # Generate PDF CV by specified template and context
            cv_object = self.cv_file_repo.make_pdf_from_html(cv_rendered_template.html_template_str, cv_rendered_template.css_files, output_pdf)
            return cv_object
        except Exception:
            raise

    def _get_formatted_person_name(self, person_name: str) -> str:
        try:
            short_name = convert_person_fullname_to_short(person_name)
            name = convert_str_to_normalized(short_name)
            return name
        except Exception:
            raise        
        