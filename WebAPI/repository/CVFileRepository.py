from datetime import datetime
import os
import pdfkit
from blueprints.cvMaker.models import DefaultResponse
from config import HTML_TO_PDF_CONFIG, OUTPUT_DIR_PATH
from interfaces.core.ICVFileRepository import ICVFileRepository


class CVFileRepository(ICVFileRepository):
    def __init__(self):
        super().__init__()
        self.DATE_CORELATIVE_FORMAT = "%d%m%Y"
        
    def make_pdf_from_html(self, cv_rendered_template: str, css_files: list[str], output_pdf: str) -> DefaultResponse:
        try:
            config = pdfkit.configuration(wkhtmltopdf=HTML_TO_PDF_CONFIG)
                        
            pdfkit.from_string(cv_rendered_template, output_pdf, configuration=config, css=css_files)
           
            return DefaultResponse(status= "correcto", message= "CV Generado exitosamente", html= cv_rendered_template, file= output_pdf)
        except Exception:
            raise
        
    def get_cv_file_path(self, person_name: str, language_enum_name: str, file_extention: str) -> str:
        current_date_corelative = datetime.now().strftime(self.DATE_CORELATIVE_FORMAT)
        
        output_file_name = fr"CV_{person_name}_{language_enum_name}_{current_date_corelative}{file_extention}"
        
        if not os.path.exists(OUTPUT_DIR_PATH):
            os.makedirs(OUTPUT_DIR_PATH)
            
        output_path = fr"{OUTPUT_DIR_PATH}//{output_file_name}"
        return output_path
    