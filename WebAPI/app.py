from flask import Flask
from blueprints.cvMaker import cvMaker
from config import HOST, PORT, ENVIRONMENT
from services.CVMakerService import CVMakerService

# # Create Flask app instance
# app = Flask(__name__)

# # Inject CVMakerService instance into app config
# app.config["cv_maker_service"] = CVMakerService()

# # Register blueprints
# app.register_blueprint(cvMaker)

# # Run the app
# if __name__ == "__main__":
#  app.run(host=HOST, port=PORT, debug=(ENVIRONMENT=='development'))


def create_app():
    app = Flask(__name__)

    # Inject CVMakerService instance into app config
    ##app.config["cv_maker_service"] = CVMakerService()
    ##app.service = CVMakerService()
    # Register blueprints
    app.register_blueprint(cvMaker)

    return app

##app = create_app()
# Línea principal para iniciar la aplicación si se ejecuta directamente
if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT, debug=(ENVIRONMENT=='development'))