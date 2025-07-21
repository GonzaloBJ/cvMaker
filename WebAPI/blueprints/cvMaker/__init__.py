from flask import jsonify, request
from flask import Blueprint
from models.cvMakerModel import Template
from services.cvMakerService import cvMakerService
#from datetime import datetime

cvMaker = Blueprint('cvMaker',__name__,  url_prefix='/cvMaker')

@cvMaker.route('/cvDesdeArchivo', methods=['GET'])
def cv_from_json():
    try:
        template_name = request.args.get('template', 'basic')
        
        cvMaker_service = cvMakerService()
        
        output_pdf = './cv_generated.pdf'
        cv_context = cvMakerService.get_cv_context()
        cv_template = cvMakerService.get_template(template_name)
       
        ##cvMaker_service.generate_test()
       
        cv_object = cvMaker_service.make_pdf_cv(cv_template, cv_context, output_pdf)
        if cv_object is None:
            return jsonify(message="object from json file failure"), 400
        
        response = cv_object.to_dict() if hasattr(cv_object, 'to_dict') else cv_object
        return response
    except Exception as e:
        exceptionMessage = f"Error: {e}"
        return jsonify(message=exceptionMessage), 500

if __name__ == "__main__":
    cvMaker.run(debug=True)