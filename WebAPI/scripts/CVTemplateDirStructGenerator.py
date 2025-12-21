import json
import os
from pathlib import Path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import TEMPLATES_SOURCE

def generate(name: str, description: str):
    try:
        color_schemes_path = "colorSchemes"
        # Definimos la base: templates/nombre_del_template
        base_path = Path("templates") / name
        
        # Definimos las rutas de los archivos
        archivos = [
            base_path / color_schemes_path / "lightBlue.css",
            base_path / color_schemes_path / "darkRed.css",
            base_path / f"{name}.css",
            base_path / f"{name}.html"
        ]
        
        for ruta_archivo in archivos:
            # Crea los directorios padres si no existen (parents=True)
            ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            
            # Crea el archivo vacío
            ruta_archivo.touch()
            print(f"Creado: {ruta_archivo}")
        
        templates_data_source = Path(TEMPLATES_SOURCE)
        if not templates_data_source.exists():
            templates_data_source.touch()
        
        nuevo_registro_template = {
            "name": name,
            "rootPath": fr"./{base_path}/",
            "colorSchemesPath": fr"{color_schemes_path}/",
            "description": description
        }

        with open(templates_data_source, 'r', encoding='utf-8') as templates_data:
            cv_templates = json.load(templates_data)

        cv_templates.append(nuevo_registro_template)

        with open(templates_data_source, 'w', encoding='utf-8') as updated_templates_data:
            json.dump(cv_templates, updated_templates_data, indent=4)
        
        print(f"Actualizado: {TEMPLATES_SOURCE}")
    except Exception as e:
        print(f"Ocurrió un error al generar las rutas: {e}")

# Ejecutar la función para generar las rutas        
generate("githubBasicResume", "Pensado para usar en Github.")