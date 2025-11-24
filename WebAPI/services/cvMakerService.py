from datetime import datetime
import json
import os
from config import CVS_DATA_SOURCE, HTML_TO_PDF_CONFIG, OUTPUT_DIR_PATH, TEMPLATES_SOURCE
from models.cvMakerModel import CVTemplate, CVDataSource
from blueprints.cvMaker.models import DefaultResponse
import jinja2
import pdfkit

from utils import convert_person_fullname_to_short, convert_str_to_normalized

class cvMakerService():
    def __init__(self):
        self.template_loader = jinja2.FileSystemLoader('./')
        self.template_env = jinja2.Environment(loader=self.template_loader)

    def make_pdf_cv(self, cv_template: CVTemplate, cv_context: any, output_pdf: str):
        try:
            template = self.template_env.get_template(cv_template.htmlPath)
            template_str = template.render(cv_context)
            
            config = pdfkit.configuration(wkhtmltopdf=HTML_TO_PDF_CONFIG)
            
            css_files = [
                cv_template.stylePath,
                cv_template.colorSchemePath
            ]
            
            pdfkit.from_string(template_str, output_pdf, configuration=config, css=css_files)
            
            return DefaultResponse(id= 0, message= "CV Generado exitosamente", data= template_str)
        except Exception:
            raise
        
    def get_template( name: str, colorScheme:str):
        try:
            with open(TEMPLATES_SOURCE, 'r', encoding='utf-8') as cvJson:
                cvTemplates = json.load(cvJson)
                
                template = next((item for item in cvTemplates if item["name"] == name), None)

                if template: 
                    cvTemplate = CVTemplate(**template)
                    cvTemplate.colorSchemePath = cvTemplate.rootPath + colorScheme + '.scheme.css'
                    
                    return cvTemplate
                else: raise IndexError(f"template {name} no encontrado")
        except Exception:
            raise
    
    def get_cv_context(person_acronym: str):
        try:
            with open(CVS_DATA_SOURCE, 'r', encoding='utf-8') as cv_data_config:
                cv_data_source_json = json.load(cv_data_config)
                cv_person_data = next((item for item in cv_data_source_json if item["personAcronym"] == person_acronym), None)
                
                if cv_person_data: 
                    cv_data_source = CVDataSource(**cv_person_data)
                    
                    with open(cv_data_source.dataPath, 'r', encoding='utf-8') as cv_data:
                        cv_context = json.load(cv_data)
                        return cv_context
                else: raise IndexError(f"datos de {person_acronym} no encontrados")
        except Exception:
            raise
        
    def get_cv_file_path(cv_template_name: str, person_name: str, language_enum_name: str, file_extention: str):
        current_date_corelative = datetime.now().strftime("%d%m%Y")
        
        output_file_name = fr"CV_{person_name}_{language_enum_name}_{current_date_corelative}.{file_extention}"
        
        if not os.path.exists(OUTPUT_DIR_PATH):
            os.makedirs(OUTPUT_DIR_PATH)
            
        output_path = fr"{OUTPUT_DIR_PATH}//{output_file_name}"
        return output_path
    
    def get_formatted_person_name(person_name: str):
        try:
            short_name = convert_person_fullname_to_short(person_name)
            name = convert_str_to_normalized(short_name)
            return name
        except Exception:
            raise        
        