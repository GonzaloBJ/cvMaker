from dataclasses import asdict
from DTOs.CVGenerationRequest import CVGenerationRequest
from enums.cvMaker import EFileExtentions
from interfaces.strategy.ICVOutputDocumentStrategy import ICVOutputDocumentStrategy
from interfaces.strategy.ICVTemplateStrategy import ICVTemplateStrategy
from interfaces.strategy.ICVDataStrategy import ICVDataStrategy
from models.cvDataModel import CVData
from models.cvMakerModel import CVDataSource, CVTemplateConfig

from utils import convert_person_fullname_to_short, convert_str_to_normalized

class CVMakerService():
    def __init__(self, cv_template_strategy: ICVTemplateStrategy, cv_data_strategy: ICVDataStrategy, cv_output_document_strategy: ICVOutputDocumentStrategy):
        self.cv_template_strategy = cv_template_strategy
        self.cv_data_strategy = cv_data_strategy
        self.cv_output_document_strategy = cv_output_document_strategy
        
    def set_strategy(self, cv_template_strategy: ICVTemplateStrategy, cv_data_strategy: ICVDataStrategy, cv_output_document_strategy: ICVOutputDocumentStrategy):
        self.cv_template_strategy = cv_template_strategy
        self.cv_data_strategy = cv_data_strategy
        self.cv_output_document_strategy = cv_output_document_strategy
        
    def make_cv_from_template(self, request: CVGenerationRequest) -> dict:
        try:
            # Get CV context data
            cv_data_path: CVDataSource = self.cv_data_strategy.get_person_data_source_by_acronym(request.person_acronym)
            cv_data: CVData = self.cv_data_strategy.get_cv_data_by_path(cv_data_path.dataPath)
            # Get CV template configuration
            cv_template_config: CVTemplateConfig = self.cv_template_strategy.get_config(request.language_name)
             # Merge context data and template configuration
            cv_context = asdict(cv_template_config) | asdict(cv_data)
            # Get CV selected template
            cv_template = self.cv_template_strategy.get_by_name_and_color(request.template_name, request.color_scheme)
            # Get rendered template
            cv_rendered_template = self.cv_template_strategy.get_rendered_template(cv_template, cv_context) 
            # Get formatted person name
            formatted_person_name = self._get_formatted_person_name(cv_data.professionalInfo.name)
            # Generate output PDF file name
            output_pdf = self.cv_output_document_strategy.get_cv_document_path(formatted_person_name, request.language_name, EFileExtentions.PDF.value)
            # Generate PDF CV by specified template and context
            cv_object = self.cv_output_document_strategy.generate_from_rendered_template(cv_rendered_template.html_template_str, cv_rendered_template.css_files, output_pdf)
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
        
