import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from WebAPI.config import OUTPUT_DIR_CV_DATA_FORMAT, OUTPUT_NAME_CV_DATA_FORMAT, CV_DATA_FORMAT_FILE

def generate():
    try:
        ruta_y_nombre_archivo = fr"{OUTPUT_DIR_CV_DATA_FORMAT}{OUTPUT_NAME_CV_DATA_FORMAT}"
        with open(ruta_y_nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(CV_DATA_FORMAT_FILE, archivo, indent=4, ensure_ascii=False)
        print(f"Archivo '{OUTPUT_NAME_CV_DATA_FORMAT}' generado con éxito en la ruta: {OUTPUT_DIR_CV_DATA_FORMAT}.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

# Ejecutar la función para generar el archivo JSON        
generate()