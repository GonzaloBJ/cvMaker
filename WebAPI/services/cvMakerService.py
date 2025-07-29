import json
#from config import ROOT_DIR
from models.cvMakerModel import CVTemplate
from repositories.cvMakerRepository import cvMakerRepository
from blueprints.cvMaker.models import DefaultResponse
import jinja2
import pdfkit

class cvMakerService():
    def __init__(self):
        self.cvMaker_repo = cvMakerRepository()
        self.template_loader = jinja2.FileSystemLoader('./')
        self.template_env = jinja2.Environment(loader=self.template_loader)

    def make_pdf_cv(self, cv_template: CVTemplate, cv_context: any, output_pdf: str):
        try:
            template = self.template_env.get_template(cv_template.htmlPath)
            template_str = template.render(cv_context)
            
            config_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
            ##config_path = '/usr/local/bin/wkhtmltopdf'
            config = pdfkit.configuration(wkhtmltopdf=config_path)
            
            pdfkit.from_string(template_str, output_pdf, configuration=config, css=cv_template.stylePath)
            
            return DefaultResponse(id= 0, message= "CV Generado exitosamente", data= template_str)
        except Exception:
            raise
        
        
    def generate_test(self):
        self.cvMaker_repo.generate_pdf_from_json_file('','')
        

    def get_template( name: str):
        default_path = "./templatesData.json"
        try:
            with open(default_path, 'r', encoding='utf-8') as cvJson:
                cvTemplates = json.load(cvJson)
                
                template = next((item for item in cvTemplates if item["name"] == name), None)

                if template: 
                    cvTemplate = CVTemplate(**template)
                    return cvTemplate
                else: raise IndexError('template no encontrado')
        except Exception:
            raise
    
    def get_cv_context(context_person: str):
        default_path = "./cvData.json"
        if context_person == "gb":
            default_path = "./cvData.json"
        if context_person == "fu":
            default_path = "./cvDataFer.json"
        try:
            with open(default_path, 'r', encoding='utf-8') as cvJson:
                cv_context = json.load(cvJson)
                
                return cv_context
        except Exception:
            raise