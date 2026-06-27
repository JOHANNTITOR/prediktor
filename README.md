
# 🏠 Método Predictivo de Precios de Arriendo

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-green)
![Licencia](https://img.shields.io/badge/Licencia-Académica-lightgrey)

> Sistema de predicción de precios de arriendo utilizando Machine Learning, desarrollado con **Scikit-learn**, **Pandas** y **Streamlit**.

---

## 📖 Descripción

Este proyecto implementa un sistema inteligente capaz de **estimar el valor de arriendo de una propiedad** a partir de sus características principales.

El sistema permite además **alimentar continuamente el conjunto de entrenamiento**, incorporando nuevos registros al archivo CSV y reentrenando el modelo para mejorar su capacidad predictiva.

---

## ✨ Características

- 📊 Predicción del precio de arriendo.
- 🏘️ Selección de barrio y tipo de propiedad.
- 📐 Ingreso de superficie.
- 🚗 Número de estacionamientos.
- 🛏️ Número de dormitorios.
- 🚿 Número de baños.
- ➕ Agregar nuevos registros al conjunto de entrenamiento.
- 📁 Almacenamiento automático en CSV.
- 🤖 Reentrenamiento del modelo con nuevos datos.
- ⚡ Interfaz gráfica desarrollada en Streamlit.

---

## 🛠 Tecnologías

| Tecnología | Función |
|------------|---------|
| Python | Lenguaje principal |
| Streamlit | Interfaz gráfica |
| Scikit-learn | Machine Learning |
| Pandas | Manejo de datos |
| NumPy | Operaciones numéricas |
| Joblib | Guardado del modelo |

---

# 📂 Estructura del proyecto

```text
Proyecto
│
├── app.py
├── entrenamiento.py
├── modelo.pkl
├── arriendos.csv
├── requirements.txt
└── README.md
```

---

# 📈 Flujo del sistema

```text
                Datos CSV
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
      Modelo Scikit-learn
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
 Entrenamiento          Predicción
         │                     │
         └──────────┬──────────┘
                    ▼
            Resultado final
```

---

# 📋 Variables utilizadas

| Variable | Tipo |
|----------|------|
| Barrio | Categórica |
| Tipo | Categórica |
| Superficie | Numérica |
| Estacionamientos | Numérica |
| Dormitorios | Numérica |
| Baños | Numérica |

---

# 📊 Conjunto de entrenamiento

El modelo aprende a partir de un archivo CSV con la siguiente estructura:

| barrio | tipo | superficie | estacionamientos | dormitorios | banos | arriendo |
|--------|------|-----------:|-----------------:|------------:|------:|----------:|
| Centro | Casa | 120 | 2 | 3 | 2 | 650000 |

---

# 🤖 Entrenamiento del modelo

El entrenamiento realiza automáticamente:

- Lectura del CSV.
- Limpieza de datos.
- Codificación de variables categóricas.
- Entrenamiento del modelo.
- Guardado del modelo entrenado.

---

# 🔍 Predicción

El usuario ingresa:

- Barrio
- Tipo de propiedad
- Superficie
- Estacionamientos
- Dormitorios
- Baños

El sistema entrega una estimación del valor del arriendo.

---

# ➕

## Agregar nuevos datos

La aplicación permite ingresar nuevos registros al archivo CSV mediante un formulario.

Cada nuevo registro pasa a formar parte del conjunto de entrenamiento para futuras actualizaciones del modelo.

---

# 🔄 Reentrenamiento

Cuando se agregan nuevos datos, el modelo puede ser reentrenado para incorporar la nueva información.

Este proceso permite mantener la precisión del sistema a medida que aumenta la cantidad de datos disponibles.

---

# 💡 Futuras mejoras

- 📍 Geolocalización por coordenadas.
- 🗺️ Distancia a colegios y supermercados.
- 📈 Historial de precios.
- 📷 Análisis mediante imágenes.
- 🧠 Modelos más avanzados (Random Forest, XGBoost).
- ☁️ Base de datos SQL.
- 🌐 Publicación en la nube.

---

# ▶️ Ejecución

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
streamlit run prediktor.py
```

---

# 📦 Dependencias

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

# 👨‍💻 Autor

**Juan Andrés Sánchez Dodero**

Proyecto Desarrollo de Inteligencia Artificial orientado a Empresas (2026)

---

# 📄 Licencia

Este proyecto ha sido desarrollado con fines académicos y de investigación.
Regulada mediante la ley Chilena de Protección de Datos.