from datetime import datetime
import json
import os
from models.cvMakerModel import CVTemplate
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
            
            config_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
            ##config_path = '/usr/local/bin/wkhtmltopdf'
            config = pdfkit.configuration(wkhtmltopdf=config_path)
            
            css_files = [
                cv_template.stylePath,
                cv_template.colorSchemePath
            ]
            
            pdfkit.from_string(template_str, output_pdf, configuration=config, css=css_files)
            
            return DefaultResponse(id= 0, message= "CV Generado exitosamente", data= template_str)
        except Exception:
            raise
        
    def get_template( name: str, colorScheme:str):
        default_path = "./templatesData.json"
        try:
            with open(default_path, 'r', encoding='utf-8') as cvJson:
                cvTemplates = json.load(cvJson)
                
                template = next((item for item in cvTemplates if item["name"] == name), None)

                if template: 
                    cvTemplate = CVTemplate(**template)
                    cvTemplate.colorSchemePath = cvTemplate.rootPath + colorScheme + '.scheme.css'
                    
                    return cvTemplate
                else: raise IndexError('template no encontrado')
        except Exception:
            raise
    
    def get_cv_context(context_person: str):
        default_path = "./cvData.json"
        if context_person == "gb":
            default_path = "./cvDataBAK.json"
        if context_person == "fu":
            default_path = "./cvDataFer.json"
        try:
            with open(default_path, 'r', encoding='utf-8') as cvJson:
                cv_context = json.load(cvJson)
                
                return cv_context
        except Exception:
            raise
        
    def get_cv_file_path(cv_template_name: str, person_name: str, language_enum_name: str, file_extention: str):
        current_date_corelative = datetime.now().strftime("%d%m%Y")
        
        output_file_name = fr"CV_{person_name}_{language_enum_name}_{current_date_corelative}.{file_extention}"
        print("file name:", output_file_name)
        
        output_path = ".//outputCV"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        output_path = fr"{output_path}//{output_file_name}"
        return output_path
    
    def get_formatted_person_name(person_name: str):
        try:
            short_name = convert_person_fullname_to_short(person_name)
            name = convert_str_to_normalized(short_name)
            return name
        except Exception:
            raise        
        