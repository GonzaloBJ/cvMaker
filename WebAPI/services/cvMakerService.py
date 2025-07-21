import json
#from config import ROOT_DIR
from models.cvMakerModel import Template
from repositories.cvMakerRepository import cvMakerRepository
from blueprints.cvMaker.models import DefaultResponse
import jinja2
import pdfkit

class cvMakerService():
    def __init__(self):
        self.cvMaker_repo = cvMakerRepository()
        self.template_loader = jinja2.FileSystemLoader('./')
        self.template_env = jinja2.Environment(loader=self.template_loader)

    def make_pdf_cv(self, cv_template: Template, cv_context: any, output_pdf: str):
        try:
            template = self.template_env.get_template(cv_template.html_path)
            template_str = template.render(cv_context)
            
            config_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
            ##config_path = '/usr/local/bin/wkhtmltopdf'
            config = pdfkit.configuration(wkhtmltopdf=config_path)
            
            pdfkit.from_string(template_str, output_pdf, configuration=config, css=cv_template.style_path)
            
            return DefaultResponse(id= 0, message= "CV Generado exitosamente", data= template_str)
        except Exception:
            raise
        
        
    def generate_test(self):
        self.cvMaker_repo.generate_pdf_from_json_file('','')
        
    def get_template( name: str):
        if name == 'basic': 
            templateBasic = Template(
                name= 'basic', 
                html_path='./templates/basic/basicTemplate.html',
                style_path='./templates/basic/basicStyles.css'
            )
            return templateBasic
        elif name == 'simpleA':
            templateSimpleA = Template(
                name= 'simpleA', 
                html_path='./templates/simpleA/simpleA.html',
                style_path='./templates/simpleA/simpleA.css'
            )
            return templateSimpleA
        elif name == 'simpleB':
            templateSimpleB = Template(
                name= 'simpleB', 
                html_path='./templates/simpleB/simpleB.html',
                style_path='./templates/simpleB/simpleB.css'
            )
            return templateSimpleB
        else: raise IndexError('template no encontrado')
    
    def get_cv_context():
        default_path = "./cvData.json"
        try:
            with open(default_path, 'r', encoding='utf-8') as cvJson:
                cv_context = json.load(cvJson)
                
                return cv_context
        except Exception:
            raise