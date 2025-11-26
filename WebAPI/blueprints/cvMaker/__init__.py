from dataclasses import asdict
from flask import jsonify, request
from flask import Blueprint
from blueprints.cvMaker.models import DefaultResponse
from enums.cvMaker import EColorScheme, EFileExtentions, ELanguages
from models.cvDataModel import Root
from models.cvMakerModel import CVTemplateConfig
from services.cvMakerService import cvMakerService

cvMaker = Blueprint('cvMaker',__name__,  url_prefix='/cvMaker')

@cvMaker.route('/cvDesdeArchivo', methods=['GET'])
def cv_from_json():
    try:
        template_name_param = request.args.get('template', 'basic')
        language_param = request.args.get('lang', 'ESP')
        person_acronym_param = request.args.get('person', 'gb')
        color_scheme_param = request.args.get('color', 'lightBlue')
        
        # Get language enum or default
        try:
            language_enum = ELanguages[language_param]
        except KeyError:
            language_enum = ELanguages.ESP
            
        # Get color scheme enum or default
        try:
            color_scheme = EColorScheme(color_scheme_param).value
        except KeyError:
            color_scheme = EColorScheme.LIGHT_BLUE.value
        
        cvMaker_service = cvMakerService()
        # Get CV context data
        cv_data: Root = cvMakerService.get_cv_data(person_acronym_param)
        # Get CV template configuration
        cv_template_config: CVTemplateConfig = cvMakerService.get_cv_template_config()
        # Add language to context
        cv_template_config.lang = language_enum.name
        # Merge context data and template configuration
        cv_context = asdict(cv_template_config) | asdict(cv_data)
        # Get CV selected template
        cv_template = cvMakerService.get_template(template_name_param, color_scheme)
        # Get formatted person name
        formatted_person_name = cvMakerService.get_formatted_person_name(cv_data.professionalInfo.name)
        # Generate output PDF file name
        output_pdf = cvMakerService.get_cv_file_path(formatted_person_name, language_enum.name, EFileExtentions.PDF.value)
        # Generate PDF CV by specified template and context
        cv_object = cvMaker_service.make_pdf_cv(cv_template, cv_context, output_pdf)
        
        if cv_object is None:
            return jsonify(DefaultResponse(status= "Error", message= "El documento no pudo ser generado.")), 400
        
        response = cv_object.to_dict() if hasattr(cv_object, 'to_dict') else cv_object
        return response
    except Exception as e:
        return jsonify(DefaultResponse(status= "Error", message= e)), 500

if __name__ == "__main__":
    cvMaker.run(debug=True)