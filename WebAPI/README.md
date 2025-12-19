# 🚀 CV Maker
Este proyecto es una API construida con **Python** y **Flask**, preparada para ejecutarse en un entorno virtual.
En base a un template y datos de cv elegidos, construye un CV en PDF y HMTL.  
Incluye instrucciones completas para instalación, configuración y ejecución.
---

## 📦 Requisitos
- Python 3.10^
- wkthmltopdf
---

[Ver TODO](TODO.md)

## 🧪 Crear y activar entorno virtual

### 1️⃣ Crear ambiente virtual
```sh
python -m venv venv
```

### 2️⃣ Activar ambiente virtual
Activar en PowerShell
```sh
venv\Scripts\Activate.ps1
```
Activar en Bash (Windows)
```sh
source venv/Scripts/activate
```
Activar en Bash (Linux)
```sh
source venv/bin/activate
```

### 3️⃣ Desactivar entorno virtual
```sh
deactivate
```

## 📥 Instalación de dependencias
Instalar módulos desde requirements.txt:
```sh
pip install -r requirements.txt
```

## 📄 Generar requirements.txt
Solo con paquetes instalados manualmente

### 1️⃣ Instalar pipreqs:
```sh
pip install pipreqs
```

### 2️⃣ Generar archivo:
```sh
pipreqs --force
```
Con todos los paquetes instalados (incluye dependencias)
```sh
python -m pip freeze > requirements.txt
```

## ▶️ Ejecutar la API
Ejecutar api directamente
```sh
flask run
```
Ejecutar Flask Server
```sh
flask --app app run
```
Ejecutar Flask Server con refresco de cambios
```sh
flask --app app run --debug
```
Ejecutar archivo Python directamente
```sh
python app.py
```

## 📚 Documentación de Endpoints

### 📄 GET /cvMaker/cvDesdeArchivo
Genera un CV utilizando una plantilla, un archivo de datos y parámetros de personalización.

URL
```bash
GET http://127.0.0.1:5000/cvMaker/cvDesdeArchivo
```

### 🔧 Parámetros (Query Params)
Parámetro	Tipo	Obligatorio	Descripción
template	string	Sí	Nombre de la plantilla a utilizar (ej: SimpleCustomA)
lang	string	Sí	Idioma del CV (ESP, ENG, etc.)
person	string	Sí	Identificador de la persona o archivo de datos (ej: fu)
color	string	No	Color base de la plantilla (ej: lightBlue)

### 📌 Ejemplo completo de llamada
```bash
GET http://127.0.0.1:5000/cvMaker/cvDesdeArchivo?template=SimpleCustomA&lang=ESP&person=fu&color=lightBlue
```

### 📤 Respuesta esperada
La API genera un archivo final (PDF o similar) basado en la plantilla y los datos seleccionados.

#### Ejemplo de respuesta (JSON)
```json
{
  "status": "correcto",
  "message": "CV generado correctamente.",
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>CV<header></html>",
  "file": "output/fu_SimpleCustomA.pdf"
}
```
