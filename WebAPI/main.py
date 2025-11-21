from flask import Flask
from blueprints.cvMaker import cvMaker
from config import HOST, PORT, ENVIRONMENT

app = Flask(__name__)

app.register_blueprint(cvMaker)
  
print(f"Starting server in {ENVIRONMENT} mode...")

if __name__ == "__main__":
 app.run(host=HOST, port=PORT, debug=(ENVIRONMENT=='development'))

    