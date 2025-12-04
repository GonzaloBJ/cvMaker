from dataclasses import asdict
from datetime import datetime
import os
from config import HTML_TO_PDF_CONFIG, OUTPUT_DIR_PATH
from enums.cvMaker import EFileExtentions
from models.cvMakerModel import CVTemplateConfig
from blueprints.cvMaker.models import DefaultResponse
import pdfkit

from repository.CVDataRepository import CVDataRepository
from repository.CVTemplateRepository import CVTemplateRepository
from utils import convert_person_fullname_to_short, convert_str_to_normalized

class CVMakerService():
    def __init__(self):
        self.cv_template_repo = CVTemplateRepository()
        self.cv_data_repo = CVDataRepository()
        
    def make_from_file(self, language_name: str, color_scheme: str, person_acronym_param: str, template_name_param: str) :
        try:            
            # Get CV context data
            cv_data = self.cv_data_repo.get_by_acronym(person_acronym_param)
            # Get CV template configuration
            cv_template_config: CVTemplateConfig = self.cv_template_repo.get_config(language_name)
             # Merge context data and template configuration
            cv_context = asdict(cv_template_config) | asdict(cv_data)
            # Get CV selected template
            cv_template = self.cv_template_repo.get_by_name_and_color(template_name_param, color_scheme)
            # Get rendered template
            cv_rendered_template = self.cv_template_repo.get_rendered_template(cv_template, cv_context) 
            # Get formatted person name
            formatted_person_name = self.get_formatted_person_name(cv_data.professionalInfo.name)
            # Generate output PDF file name
            output_pdf = self.get_cv_file_path(formatted_person_name, language_name, EFileExtentions.PDF.value)
            # Generate PDF CV by specified template and context
            cv_object = self.make_pdf_cv(cv_rendered_template.html_template_str, cv_rendered_template.css_files, output_pdf)
            return cv_object
        except Exception:
            raise

    def make_pdf_cv(self, cv_rendered_template: str, css_files: list[str], output_pdf: str) -> DefaultResponse:
        try:
            config = pdfkit.configuration(wkhtmltopdf=HTML_TO_PDF_CONFIG)
                        
            pdfkit.from_string(cv_rendered_template, output_pdf, configuration=config, css=css_files)
           
            return DefaultResponse(status= "correcto", message= "CV Generado exitosamente", html= cv_rendered_template, file= output_pdf)
        except Exception:
            raise
        
    def get_cv_file_path(self, person_name: str, language_enum_name: str, file_extention: str) -> str:
        current_date_corelative = datetime.now().strftime("%d%m%Y")
        
        output_file_name = fr"CV_{person_name}_{language_enum_name}_{current_date_corelative}{file_extention}"
        
        if not os.path.exists(OUTPUT_DIR_PATH):
            os.makedirs(OUTPUT_DIR_PATH)
            
        output_path = fr"{OUTPUT_DIR_PATH}//{output_file_name}"
        return output_path
    
    def get_formatted_person_name(self, person_name: str) -> str:
        try:
            short_name = convert_person_fullname_to_short(person_name)
            name = convert_str_to_normalized(short_name)
            return name
        except Exception:
            raise        
        