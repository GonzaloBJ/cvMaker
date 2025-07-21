from flask import Flask, jsonify
from blueprints.cvMaker import cvMaker
from config import HOST, PORT

app = Flask(__name__)

app.register_blueprint(cvMaker)
  
@app.route("/")
async def home():
    return jsonify({"message": "Hello Bigger Applications!"})

if __name__ == "__main__":
 app.run(host=HOST, port=PORT)

    