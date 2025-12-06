from os import getenv, path
from dotenv import load_dotenv

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
CVS_DATA_SOURCE = "./cvDataSource.json"
TEMPLATES_SOURCE = "./templatesData.json"
TEMPLATES_CONFIG_SOURCE = "./templatesConfig.json"
OUTPUT_DIR_PATH = ".//static//outputCV"

# pdfkit
# HTML_TO_PDF_CONFIG = '/usr/local/bin/wkhtmltopdf'
HTML_TO_PDF_CONFIG = getenv("HTML_TO_PDF_CONFIG") 