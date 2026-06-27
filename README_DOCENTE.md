# 🏠 Método Predictivo de Precios de Arriendos

### Proyecto complementario de aprendizaje en Machine Learning con Scikit-learn

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-success)
![Licencia](https://img.shields.io/badge/Licencia-Académica-lightgrey)

---

## 📖 Descripción

Este proyecto implementa un **modelo predictivo de precios de arriendo** utilizando técnicas de **Machine Learning** con **Scikit-learn** y una interfaz desarrollada en **Streamlit**.

Su principal objetivo es **servir como plataforma de aprendizaje y experimentación**, permitiendo comprender el ciclo completo de construcción de un modelo predictivo:

* Preparación de datos.
* Preprocesamiento de variables.
* Entrenamiento del modelo.
* Predicción.
* Actualización del conjunto de entrenamiento.
* Reentrenamiento del modelo.

Más que un proyecto inmobiliario, este desarrollo constituye un **laboratorio práctico** para adquirir experiencia con herramientas de aprendizaje automático que posteriormente serán aplicadas en un proyecto de mayor complejidad.

---

# 🎯 Objetivo

Este proyecto fue desarrollado como un **complemento de aprendizaje** para el proyecto principal de título:

> **Lectura OCR de tickets de peajes e interpretación inteligente de datos mediante Inteligencia Artificial.**

El propósito es comprender en profundidad cómo funcionan los modelos de Machine Learning antes de incorporarlos al sistema OCR, donde serán utilizados para apoyar tareas como la clasificación, interpretación y análisis de la información extraída desde documentos.

---

# 🧠 ¿Por qué desarrollar este proyecto?

El sistema OCR requiere combinar diversas etapas:

* Captura de imágenes.
* Reconocimiento óptico de caracteres (OCR).
* Limpieza de texto.
* Interpretación de información.
* Clasificación automática.
* Predicción y apoyo a la toma de decisiones.

Antes de integrar estas funcionalidades en el proyecto principal, resulta conveniente trabajar con un problema controlado y de menor complejidad, permitiendo comprender el funcionamiento de las herramientas utilizadas.

La predicción de precios de arriendo ofrece un escenario ideal para aprender conceptos fundamentales como:

* Ingeniería de características (Feature Engineering).
* Variables categóricas y numéricas.
* Preprocesamiento de datos.
* Codificación mediante One-Hot Encoding.
* Entrenamiento supervisado.
* Persistencia de modelos.
* Evaluación de resultados.
* Flujo completo de entrenamiento y predicción.

---

# 🚀 Funcionalidades

* 🏘️ Predicción del valor de arriendo de una propiedad.
* 📊 Entrenamiento del modelo mediante Scikit-learn.
* 📁 Lectura automática del conjunto de datos desde un archivo CSV.
* ➕ Incorporación de nuevos registros al conjunto de entrenamiento.
* 🔄 Reentrenamiento del modelo cuando existen nuevos datos.
* 💾 Almacenamiento del modelo entrenado.
* 🖥️ Interfaz gráfica desarrollada con Streamlit.

---

# ⚙️ Tecnologías utilizadas

| Tecnología   | Propósito                 |
| ------------ | ------------------------- |
| Python       | Lenguaje principal        |
| Scikit-learn | Machine Learning          |
| Pandas       | Manipulación de datos     |
| NumPy        | Procesamiento numérico    |
| Streamlit    | Interfaz web              |
| Joblib       | Almacenamiento del modelo |

---

# 📊 Flujo del sistema

```text
          Archivo CSV
               │
               ▼
      Lectura con Pandas
               │
               ▼
   Preprocesamiento de datos
               │
               ▼
      ColumnTransformer
               │
               ▼
      OneHotEncoder
               │
               ▼
 Modelo de Machine Learning
               │
      ┌────────┴─────────┐
      ▼                  ▼
 Entrenamiento      Predicción
      │                  │
      └────────┬─────────┘
               ▼
     Valor estimado de arriendo
```

---

# 📂 Variables consideradas

* 🏘️ Barrio
* 🏠 Tipo de propiedad
* 📐 Superficie
* 🚗 Estacionamientos
* 🛏️ Dormitorios
* 🚿 Baños

Estas variables permiten al modelo aprender patrones presentes en el conjunto de entrenamiento y estimar un valor de arriendo para nuevas propiedades.

---

# 🔄 Aprendizaje continuo

Una característica importante del proyecto es la posibilidad de ampliar el conjunto de entrenamiento.

El usuario puede agregar nuevos registros al archivo CSV y posteriormente volver a entrenar el modelo para incorporar esa información.

Este proceso simula el ciclo habitual de mejora de un sistema de Machine Learning basado en datos cada vez más completos y representativos.

---

# 🎓 Relación con el proyecto principal

Los conocimientos adquiridos durante este desarrollo serán aplicados posteriormente al proyecto:

**Lectura OCR de tickets de peajes e interpretación inteligente de datos mediante IA**, donde el Machine Learning complementará el reconocimiento óptico de caracteres para mejorar el procesamiento de documentos.

Este proyecto constituye una etapa de formación práctica orientada a comprender las herramientas y metodologías que luego serán reutilizadas en un contexto documental más complejo.

---

# 🚀 Próximas mejoras

* Modelos de regresión adicionales para comparar resultados.
* Evaluación de métricas de desempeño.
* Validación cruzada.
* Optimización de hiperparámetros.
* Integración con bases de datos.
* Publicación en la nube.
* Incorporación de información geográfica.
* Visualización de estadísticas y gráficos.

---

# 👨‍💻 Autor

**Juan Andrés Sánchez Dodero**

Proyecto de aprendizaje desarrollado como apoyo al Proyecto de 'Reconocimiento de Tickets de Peajes y Visión Artificial e Interpretación de datos'. (2026)

---

> *"Antes de construir sistemas inteligentes capaces de interpretar documentos complejos, es fundamental comprender cómo aprenden los humanos que sustentan dichas decisiones. 'Human First'"*
