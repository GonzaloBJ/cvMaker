import encodings
from os import getenv, path
from dotenv import load_dotenv
from flask import json
from utils import open_toml

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Variables globales
ENVIRONMENT = getenv("ENVIRONMENT")
ROOT_DIR = path.dirname(path.abspath(__file__))
UNIVERSAL_ENCODING = encodings.utf_8.getregentry().name

##APi Config
HOST = getenv("HOST")
PORT = getenv("PORT")

# cvMaker rutas y configuraciones
CV_DATA_SOURCES = open_toml("./cvDataSource.toml")
TEMPLATES_SOURCE = "./templatesData.json"
TEMPLATES_CONFIG = open_toml("./templatesConfig.toml")
OUTPUT_DIR_PATH = ".//static//outputCV"
API_INTERFACE_PATH = ".//index.html"

# pdfkit
# HTML_TO_PDF_CONFIG = '/usr/local/bin/wkhtmltopdf'
HTML_TO_PDF_CONFIG = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"

# Generador formato cv data
OUTPUT_NAME_CV_DATA_FORMAT = "CV_DATA_FORMAT_FILE.json"
OUTPUT_DIR_CV_DATA_FORMAT = ".//static//cvDataFormat//"
CV_DATA_FORMAT_FILE = json.load(open('./cvDataFormatFile.json', 'r', encoding='utf-8'))