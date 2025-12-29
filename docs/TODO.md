# ☑️ Gestión de Tareas (TODO)

Las tareas se marcan como pendientes (`[❌]`) o completadas (`[✅]`).

* **Configuración y Modelos:**
    * [✅] `Registry` para `templatesData.json` y `cvData`.
    * [✅] refactorizar `cvFileRepository` a `cvOutputStategy` para tener distintas salidas de archivo(pdf, html, word).
    * [✅] Actualizar metodos para usar clases de entrada.
    * [✅] Generar validador de parametros entrada api usando dataclass(arg).
    * [✅] Implementar `toml` (Tom's Obvious, Minimal Language) para configuraciones.
    * [❌] crear `cvToReadmeStrategy` para exportar el template a readme (github).
    * [❌] refactorizar `template_loader` para que tome las rutas del directorio `/templates`.
    * [❌] Agregar metodo de api para generar cv desde url de datos `cvDesdeUrl` usando github /docs.
* **Contenido y Datos (CV):**
    * [✅] Agregar seccion de `Proyects` para incorporar data de proyectos y repos.
    * [✅] En la sección `skills` agregar atributos para **iconos y nivel** de conocimiento.
    * [✅] Agregar `location` (ubicación) a los trabajos en la experiencia.
    * [✅] Agregar detalles por experiencia (descripciones más ricas).
    * [✅] En la sección `skills` agregar atributo **grupos** para ordenar las skills.
    * [✅] En los ragnos de fechas cambiar a `[mm, yyyy]` y dividir por inicio y fin.
    * [✅] Agregar lenguajes a `workModel`.
    * [❌] Completar secciones **formation date, certification date, skills, proyects, workModel, location, dateRange** en el `dataJson`.
* **Implementación de Templates:**
    * [❌] Completar los templates `fullAts` y `2columnas`.
    * [❌] Los templates `fullAts` y `basicAts` deben contener los titulos de las secciones por variable.
    * [❌] Crear template básico con referencia de `templateATS.txt`.
    * [❌] Crear templates para readme (github) uno tipo cv simple y otro con data de proyectos.
* **Mejoras Visuales:**
    * [✅] En interfaz de api cambiar texto de `consejo`, ajustar tamaño de la seccion `cvgenerado`.
    * [❌] Incorporar estilo de sublista en listados (Tarea completada).
    * [❌] Revisar estilo de títulos con línea.
* **Flujo de Trabajo:**
    * [✅] Incorporar `vista` para interfaz de API.
    * [✅] Agregar script generador de dataJson base.
    * [✅] Agregar script para generar rutas de nuevos templates.
    * [✅] Incorporar `github-pages` y dejar todos los documentos en docs y acortar readme mediante enlaces.
* **Testing:**
    * [❌] Agregar test unitarios.
* **Limpieza y Documentación:**
    * [❌] Cambiar `get` del `main` por algo como **Swagger** o una interfaz de API (flask restx).
    * [❌] Validar y documentar uso de `setup.sh`.

---

> **Nota:** Las tareas marcadas con `[✅]` ya están fusionadas con la rama principal.