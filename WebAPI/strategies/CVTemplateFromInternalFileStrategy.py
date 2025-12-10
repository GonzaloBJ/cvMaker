import encodings
from typing import Any
from flask import json
import jinja2
from config import TEMPLATES_CONFIG_SOURCE, TEMPLATES_SOURCE
from interfaces.strategy.ICVTemplateStrategy import ICVTemplateStrategy
from models.cvMakerModel import CVTemplate, CVTemplateConfig, RenderedTemplate


class CVTemplateFromInternalFileStrategy(ICVTemplateStrategy):
    def __init__(self):
        super().__init__()
        self.FILE_ENCODING = encodings.utf_8.getregentry().name
        self.FILE_READ_MODE = 'r'
        self.NAME_ATTR = 'name'
        self.template_loader = jinja2.FileSystemLoader('./') # todo: set /templates/
        self.template_env = jinja2.Environment(loader=self.template_loader)
    
    def get_config(self, language_name: str) -> CVTemplateConfig:
        try:
            with open(TEMPLATES_CONFIG_SOURCE, self.FILE_READ_MODE, encoding=self.FILE_ENCODING) as cv_template_config_str:
                cv_template_config = CVTemplateConfig.from_dict((json.load(cv_template_config_str)))
                
                cv_template_config.lang = language_name
                
                return cv_template_config
        except Exception:
            raise

    def get_by_name_and_color(self, template_name_param: str, color_scheme: str) -> CVTemplate:
        try:
            with open(TEMPLATES_SOURCE, self.FILE_READ_MODE, encoding=self.FILE_ENCODING) as cvJson:
                cv_templates = json.load(cvJson)
                
                template = next((item for item in cv_templates if item[self.NAME_ATTR] == template_name_param), None)

                if template: 
                    cv_template = CVTemplate(**template)
                    cv_template.set_color_scheme_css_path(color_scheme)
                    
                    return cv_template
                else: raise IndexError(f"Template {template_name_param} no encontrado.")
        except Exception:
            raise
    
    def get_rendered_template(self, cv_template: CVTemplate, cv_context: dict[str, Any]) -> RenderedTemplate:
        try:
            cv_template_html_path:str = cv_template.get_html_path()
            cv_template_css_path: str = cv_template.get_css_path()
            
            template = self.template_env.get_template(cv_template_html_path)
            template_str = template.render(cv_context)
            
            css_files = [
                cv_template.colorSchemesPath,
                cv_template_css_path
            ]
            
            return RenderedTemplate(template_str, css_files)
        except Exception:
            raise