from flask import current_app, jsonify, render_template, request
from flask import Blueprint
from DTOs.CVGenerationRequest import CVGenerationRequest
from blueprints.cvMaker.models import DefaultResponse, QueryParams
from config import API_INTERFACE_PATH
from services.CVMakerService import CVMakerService
from strategies.CVDataFromInternalFileStrategy import CVDataFromInternalFileStrategy
from strategies.CVTemplateFromInternalFileStrategy import CVTemplateFromInternalFileStrategy
from strategies.CVToPDFDocumentStrategy import CVToPDFDocumentStrategy

cvMaker = Blueprint('cvMaker',__name__,  url_prefix='/cvMaker')


@cvMaker.route('/', methods=['GET'])
def home():
    return render_template(API_INTERFACE_PATH)

@cvMaker.route('/cvDesdeArchivo', methods=['GET'])
def cv_from_json():
    try:
        # Get request parameters
        request_query = QueryParams(**request.args.to_dict())
         # Get enums from request parameters
        language_enum = request_query.lang_to_enum()
        color_scheme = request_query.color_to_enum()
        
        # Set strategy to CVMakerService
        cv_maker_service: CVMakerService = current_app.config["cv_maker_service"]
        cv_maker_service.set_strategy(
            cv_data_strategy=CVDataFromInternalFileStrategy(), 
            cv_output_document_strategy=CVToPDFDocumentStrategy(), 
            cv_template_strategy=CVTemplateFromInternalFileStrategy()
            )
        
        # Generate CV
        request_data = CVGenerationRequest(
            language_name=language_enum.name,
            color_scheme=color_scheme,
            person_acronym=request_query.person,
            template_name=request_query.template
        )
        
        try:
            cv_object = cv_maker_service.make_cv_from_template(request_data)
            if cv_object is None:
                print("cv_object es None")
                return jsonify(DefaultResponse.fail("El documento no pudo ser generado.").model_dump()), 400
        except Exception as e:
            return jsonify(DefaultResponse.fail(str(e)).model_dump()), 500
        
        return jsonify(DefaultResponse.success(
            message="CV Generado exitosamente", 
            html=cv_object['html'], 
            file=cv_object['file']).model_dump()), 200
    except Exception as e:
        print("Error generating CV:", e)
        return jsonify(DefaultResponse.fail(e).model_dump()), 500

if __name__ == "__main__":
    cvMaker.run(debug=True)