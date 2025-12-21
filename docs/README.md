# 📝 cvMaker
Este proyecto es una API construida con **Python** y **Flask**, preparada para ejecutarse en un entorno virtual.
En base a un template y datos de cv elegidos, construye un CV en PDF y HMTL.  
Incluye instrucciones completas para instalación, configuración y ejecución.

<!-- # Python Web API (Flask)

API REST desarrollada en Python utilizando **Flask**, diseñada bajo principios de arquitectura limpia y buenas prácticas de ingeniería de software. Este proyecto sirve como base profesional para la creación de servicios web livianos, mantenibles y listos para producción. -->
---

## 📌 Características
<!-- <details>
 <summary><strong>Click to expand list</strong></summary>

</details> -->
<!-- * Arquitectura modular y desacoplada -->
<!-- * Manejo centralizado de errores -->
* 💻 UI para api
* 👌 Validación de datos
* ⚙ Configuración por entorno
* 📚 Gestión de templates
* 📇 Gestión de datos cv
* 🎨 Selección de esquema de color
<!-- * Estructura preparada para testing y despliegue -->

---

## ✅ TODO
[Ver TODO](TODO.md)

---

## 🛠️ Tecnologías

* **Python 3.10+**
* **Flask** (framework web)
* **python-dotenv** (variables de entorno)
* **Jinja2** (templates html)
* **pdfkit** (coversion a pdf)
* **pydantic** (modelo de datos y validación)

<!-- * **Flask-RESTful / Blueprints** (organización de endpoints) -->
<!-- * **Marshmallow** (serialización y validación) -->

<!-- * **pytest** (testing) -->

---

<!-- ## 📂 Estructura del Proyecto

```text
app/
├── api/
│   ├── routes/
│   │   └── example_routes.py
│   └── __init__.py
├── core/
│   ├── config.py
│   └── exceptions.py
├── models/
│   └── example_model.py
├── schemas/
│   └── example_schema.py
├── services/
│   └── example_service.py
├── __init__.py
├── app.py

 tests/

.env.example
requirements.txt
README.md
``` 

---
-->
## 📦 Prerequisitos
* **Python 3.10^**
* **wkthmltopdf**

---

## ⚙️ Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/GonzaloBJ/cvMaker.git
cd WebAPI
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
source venv\\Scripts\\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Variables de entorno

Ajusta los valores según tu entorno:

```env
ENVIRONMENT=development
HOST=localhost
PORT=4200
HTML_TO_PDF_CONFIG=C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe
```

---

## ▶️ Ejecución
Ejecutar usando Flask Cli:
```bash
flask run
```
Ejecutar Flask Server
```bash
flask --app app run     # ejecuta compilado
flask --app app run --debug     # ejecuta con refresco de cambios
```

La API estará disponible en:

* **API**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
<!-- * **Swagger UI**: [http://127.0.0.1:5000/swagger](http://127.0.0.1:5000/swagger) -->

---

<!-- ## 🧪 Tests

Para ejecutar las pruebas:

```bash
pytest
```

--- -->

<!-- ## 🚀 Despliegue

La aplicación es compatible con despliegues en:

* Docker
* VPS (Linux)
* Servicios cloud (Azure, AWS, GCP)

Para producción se recomienda ejecutar Flask sobre:

* **Gunicorn**

Ejemplo:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app.app:app
```

--- -->

## 📐 Buenas Prácticas Aplicadas

* Separación de responsabilidades
* Uso de Blueprints
* Principios SOLID
* Configuración por entorno
* Manejo centralizado de errores

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Ver el archivo `LICENSE` para más información.

---

## 👤 Autor

**Gonzalo Barahona**
Software Developer

---

## 📬 Contacto

Para consultas o colaboraciones, puedes contactarme vía GitHub.
