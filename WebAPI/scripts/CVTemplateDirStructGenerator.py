import os
from pathlib import Path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate(name: str):
    try:
        # Definimos la base: templates/nombre_del_template
        base_path = Path("templates") / name
        
        # Definimos las rutas de los archivos
        archivos = [
            base_path / "colorSchemes" / "lightBlue.css",
            base_path / "colorSchemes" / "darkRed.css",
            base_path / f"{name}.css",
            base_path / f"{name}.html"
        ]
        
        for ruta_archivo in archivos:
            # Crea los directorios padres si no existen (parents=True)
            ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            
            # Crea el archivo vacío
            ruta_archivo.touch()
            print(f"Creado: {ruta_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al generar las rutas: {e}")

# Ejecutar la función para generar las rutas        
generate("githubBasicResume")