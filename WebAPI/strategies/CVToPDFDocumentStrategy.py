from datetime import datetime
import os
from config import OUTPUT_DIR_PATH, HTML_TO_PDF_CONFIG
import pdfkit
from interfaces.strategy.ICVOutputDocumentStrategy import ICVOutputDocumentStrategy


class CVToPDFDocumentStrategy(ICVOutputDocumentStrategy):
    def __init__(self):
        super().__init__()
        self.DATE_CORELATIVE_FORMAT = "%d%m%Y"
        
    def generate_from_rendered_template(self, cv_rendered_template: str, css_files: list[str], output_document: str) -> dict:
        try:
            config = pdfkit.configuration(wkhtmltopdf=HTML_TO_PDF_CONFIG)
                        
            pdfkit.from_string(cv_rendered_template, output_document, configuration=config, css=css_files)
           
            return { 'html': cv_rendered_template, 'file': output_document }
        except Exception:
            raise
        
    def get_cv_document_path(self, person_name: str, language_enum_name: str, file_extention: str) -> str:
        current_date_corelative = datetime.now().strftime(self.DATE_CORELATIVE_FORMAT)
        
        output_file_name = fr"CV_{person_name}_{language_enum_name}_{current_date_corelative}{file_extention}"
        
        if not os.path.exists(OUTPUT_DIR_PATH):
            os.makedirs(OUTPUT_DIR_PATH)
            
        output_path = fr"{OUTPUT_DIR_PATH}//{output_file_name}"
        return output_path
    