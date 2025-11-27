from datetime import datetime
import json
import os
from config import CVS_DATA_SOURCE, HTML_TO_PDF_CONFIG, OUTPUT_DIR_PATH, TEMPLATES_CONFIG_SOURCE, TEMPLATES_SOURCE
from models.cvDataModel import Root
from models.cvMakerModel import CVTemplate, CVDataSource, CVTemplateConfig
from blueprints.cvMaker.models import DefaultResponse
import jinja2
import pdfkit

from utils import convert_person_fullname_to_short, convert_str_to_normalized

class CVMakerService():
    def __init__(self):
        self.template_loader = jinja2.FileSystemLoader('./') # todo: set /templates/
        self.template_env = jinja2.Environment(loader=self.template_loader)

    def make_pdf_cv(self, cv_template: CVTemplate, cv_context: any, output_pdf: str) -> DefaultResponse:
        try:
            cv_template_html_path:str = cv_template.get_html_path()
            cv_template_css_path: str = cv_template.get_css_path()
            
            template = self.template_env.get_template(cv_template_html_path)
            template_str = template.render(cv_context)
            
            config = pdfkit.configuration(wkhtmltopdf=HTML_TO_PDF_CONFIG)
            
            css_files = [
                cv_template.colorSchemesPath,
                cv_template_css_path
            ]
            
            pdfkit.from_string(template_str, output_pdf, configuration=config, css=css_files)
           
            return DefaultResponse(status= "correcto", message= "CV Generado exitosamente", html= template_str, file= output_pdf)
        except Exception:
            raise
        
    def get_template(self, name: str, color_scheme:str) -> CVTemplate:
        try:
            with open(TEMPLATES_SOURCE, 'r', encoding='utf-8') as cvJson:
                cv_templates = json.load(cvJson)
                
                template = next((item for item in cv_templates if item["name"] == name), None)

                if template: 
                    cv_template = CVTemplate(**template)
                    cv_template.set_color_scheme_css_path(color_scheme)
                    
                    return cv_template
                else: raise IndexError(f"Template {name} no encontrado.")
        except Exception:
            raise
    
    def get_cv_data(self, person_acronym: str) -> Root:
        try:
            with open(CVS_DATA_SOURCE, 'r', encoding='utf-8') as cv_data_sources:
                cv_data_sources_json = json.load(cv_data_sources)
                cv_person_data = next((item for item in cv_data_sources_json if item["personAcronym"] == person_acronym), None)
                
                if cv_person_data: 
                    cv_data_source = CVDataSource(**cv_person_data)
                    
                    with open(cv_data_source.dataPath, 'r', encoding='utf-8') as cv_data_json:
                        cv_data = Root.from_dict(json.load(cv_data_json))
                        return cv_data
                else: raise IndexError(f"Datos de {person_acronym} no encontrados.")
        except Exception:
            raise
        
    def get_cv_template_config(self) -> CVTemplateConfig:
        try:
            with open(TEMPLATES_CONFIG_SOURCE, 'r', encoding='utf-8') as cv_template_config_str:
                cv_template_config = CVTemplateConfig.from_dict((json.load(cv_template_config_str)))
                
                return cv_template_config
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
        