from flask import current_app, jsonify, render_template, request
from flask import Blueprint
from DTOs.CVGenerationRequest import CVGenerationRequest
from blueprints.cvMaker.models import DefaultResponse
from config import API_INTERFACE_PATH
from enums.cvMaker import EColorScheme, ELanguages
from services.CVMakerService import CVMakerService
from strategies.CVDataFromInternalFileStrategy import CVDataFromInternalFileStrategy
from strategies.CVTemplateFromInternalFileStrategy import CVTemplateFromInternalFileStrategy
from strategies.CVToPDFDocumentStrategy import CVToPDFDocumentStrategy

cvMaker = Blueprint('cvMaker',__name__,  url_prefix='/cvMaker')

@cvMaker.route('/', methods=['GET'])
def home():
    # render_template busca 'index.html' automáticamente dentro de la carpeta 'templates'
    return render_template(API_INTERFACE_PATH)

@cvMaker.route('/cvDesdeArchivo', methods=['GET'])
def cv_from_json():
    try:
        # Get request parameters
        template_name_param = request.args.get('template', 'basic')
        language_param = request.args.get('lang', 'ESP')
        person_acronym_param = request.args.get('person', 'gb')
        color_scheme_param = request.args.get('color', 'lightBlue')
        
        # Get injected cvMakerService 
        cv_maker_service: CVMakerService = current_app.config["cv_maker_service"]
        cv_maker_service.set_strategy(
            cv_data_strategy=CVDataFromInternalFileStrategy(), 
            cv_output_document_strategy=CVToPDFDocumentStrategy(), 
            cv_template_strategy=CVTemplateFromInternalFileStrategy()
            )
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

        request_data = CVGenerationRequest(
            language_name=language_enum.name,
            color_scheme=color_scheme,
            person_acronym=person_acronym_param,
            template_name=template_name_param
        )
            
        # Generate CV
        cv_object = cv_maker_service.make_cv_from_template(request_data)
        if cv_object is None:
            print("cv_object es None")
            return jsonify(DefaultResponse(status= "Error", message= "El documento no pudo ser generado.", file=None, html=None).model_dump()), 400
        
        # response = cv_object.to_dict() if hasattr(cv_object, 'to_dict') else cv_object
        return jsonify(cv_object.model_dump()), 200
    except Exception as e:
        print("Error generating CV:", e)
        return jsonify(DefaultResponse(status= "Error", message= e, file=None, html=None).model_dump()), 500

if __name__ == "__main__":
    cvMaker.run(debug=True)