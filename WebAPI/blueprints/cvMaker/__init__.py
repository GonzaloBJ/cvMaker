from flask import jsonify, request
from flask import Blueprint
from enums.cvMaker import EFileExtentions, ELanguages
from services.cvMakerService import cvMakerService

cvMaker = Blueprint('cvMaker',__name__,  url_prefix='/cvMaker')

@cvMaker.route('/cvDesdeArchivo', methods=['GET'])
def cv_from_json():
    try:
        template_name = request.args.get('template', 'basic')
        language_str = request.args.get('lang', 'ESP')
        context_person = request.args.get('context', 'gb')
        colorScheme = request.args.get('color', 'lightBlue')
        # Get language enum or default
        try:
            language_enum = ELanguages[language_str]
        except KeyError:
            language_enum = ELanguages.ESP
        
        cvMaker_service = cvMakerService()
        # Get CV context data
        cv_context = cvMakerService.get_cv_context(context_person)
        # Add language to context
        cv_context["lang"] = language_enum.name
        # Get CV selected template
        cv_template = cvMakerService.get_template(template_name, colorScheme)
        
        formatted_person_name = cvMakerService.get_formatted_person_name(cv_context["professionalInfo"]["name"])
        # Generate output PDF file name
        output_pdf = cvMakerService.get_cv_file_path(cv_template.name, formatted_person_name, language_enum.name, EFileExtentions.pdf.name)
        # Generate PDF CV by specified template and context
        cv_object = cvMaker_service.make_pdf_cv(cv_template, cv_context, output_pdf)
        
        if cv_object is None:
            return jsonify(message="El documento no pudo ser generado."), 400
        
        response = cv_object.to_dict() if hasattr(cv_object, 'to_dict') else cv_object
        return response
    except Exception as e:
        exceptionMessage = f"Error: {e}"
        return jsonify(message=exceptionMessage), 500

if __name__ == "__main__":
    cvMaker.run(debug=True)