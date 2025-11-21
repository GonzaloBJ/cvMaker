# 🚀 Gestión de Tareas (TODO)

Este archivo sirve como un registro centralizado de las funcionalidades, mejoras y correcciones pendientes para el proyecto. Utilizamos la sintaxis de casillas de verificación de Markdown para un seguimiento rápido y visual.

---

## 📋 Lista de Tareas Pendientes
Las tareas se marcan como pendientes (`[❌]`) o completadas (`[✅]`).

* **Configuración y Modelos:**
    * [❌] Orígenes de `dataJson` por archivo de configuración.
    * [❌] Para los `templatesData` las rutas se deben construir desde una ruta *root* + *path*.
    * [❌] Implementar `toml` (Tom's Obvious, Minimal Language) para configuraciones.
    * [❌] `Registry` para `templatesData.json` y `cvData`.
    * [❌] Crear carpeta `core` para guardar configuraciones (`env`, `apiconf`, `pdfkit`, `gettemplates`, `dataJson`).
    * [✅] En `models` cambiar `cvmodel` por `cvData`.
    * [❌] Refactorizar la implementacion del `cvMakerService` por repository y limpiar blueprint.
    * [❌] Actualizar `utils`.
* **Contenido y Datos (CV):**
    * [❌] En la sección `skills` agregar atributos para **iconos y nivel** de conocimiento.
    * [❌] Agregar `location` (ubicación) a los trabajos en la experiencia.
    * [❌] Agregar detalles por experiencia (descripciones más ricas).
* **Implementación de Templates:**
    * [❌] Completar los templates `fullAts` y `2columnas`.
    * [❌] Crear template básico con referencia de `templateATS.txt`.
    * [❌] Crear carpeta `colorScheme` para cada template.
* **Mejoras Visuales:**
    * [❌] Incorporar estilo de sublista en listados (Tarea completada).
    * [❌] Revisar estilo de títulos con línea.
* **Flujo de Trabajo:**
    * [✅] Ruta para archivos PDF generados.
    * [✅] Renombrar archivo con el formato: `cv_nombrepersona_idioma_ddmmyyyy.pdf`.
    * [❌] Cambiar `get` del `main` por algo como **Swagger** o una interfaz de API.
    * [✅] Cambiar formato del `Resquests.http`.
    * [✅] Remover `__init__.py` innecesarios.
* **Testing:**
    * [✅] Remover `generate_test`.
    * [❌] Agregar test unitarios.
* **Limpieza y Documentación:**
    * [❌] Limpiar `.gitignore` para una gestión de archivos adecuada.
    * [❌] Buscar y reemplazar formato de `readme` (refinar el estilo y contenido).
    * [❌] Validar y documentar uso de `setup.sh`.

---

> **Nota:** Las tareas marcadas con `[✅]` ya están fusionadas con la rama principal.