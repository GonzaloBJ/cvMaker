import jinja2
import pdfkit
from datetime import datetime

class cvMakerRepository:
    def __init__(self):
        self.test = ""
        
    def generate_pdf_from_json_file(self, filepath: str, template: str):
        my_name = "Frank Andrade"
        item1 = "TV"
        item2 = "Couch"
        item3 = "Washing Machine"
        today_date = datetime.today().strftime("%d %b, %Y")

        context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
                'today_date': today_date}

        template_loader = jinja2.FileSystemLoader('./')
        template_env = jinja2.Environment(loader=template_loader)

        html_template = './templates/basic/basicTemplate.html'
        template = template_env.get_template(html_template)
        output_text = template.render(context)

        config_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
        ##config_path = '/usr/local/bin/wkhtmltopdf'
        
        config = pdfkit.configuration(wkhtmltopdf=config_path)
        output_pdf = './cv_generated.pdf'
        pdfkit.from_string(output_text, output_pdf, configuration=config, css='./templates/basic/basicStyles.css')