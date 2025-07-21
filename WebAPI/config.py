from os import getenv, path
from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# api variables
HOST = getenv("HOST")
PORT = getenv("PORT")
AUTH_TOKEN = getenv("AUTH_TOKEN")

ROOT_DIR = path.dirname(path.abspath(__file__))