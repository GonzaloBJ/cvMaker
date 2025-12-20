from os import getenv, path
from dotenv import load_dotenv
from flask import json

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# api variables
ENVIRONMENT = getenv("ENVIRONMENT")
HOST = getenv("HOST")
PORT = getenv("PORT")
AUTH_TOKEN = getenv("AUTH_TOKEN")

ROOT_DIR = path.dirname(path.abspath(__file__))

# cvMaker rutas
CV_DATA_SOURCES = "./cvDataSource.json"
TEMPLATES_SOURCE = "./templatesData.json"
TEMPLATES_CONFIG_SOURCE = "./templatesConfig.json"
OUTPUT_DIR_PATH = ".//static//outputCV"
API_INTERFACE_PATH = ".//index.html"

# pdfkit
# HTML_TO_PDF_CONFIG = '/usr/local/bin/wkhtmltopdf'
HTML_TO_PDF_CONFIG = getenv("HTML_TO_PDF_CONFIG") 

# Generador formato cv data
OUTPUT_NAME_CV_DATA_FORMAT = "CV_DATA_FORMAT_FILE.json"
OUTPUT_DIR_CV_DATA_FORMAT = ".//static//cvDataFormat//"
CV_DATA_FORMAT_FILE = json.load(open('./cvDataFormatFile.json', 'r', encoding='utf-8'))