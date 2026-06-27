
# importar librerías
import streamlit as st
import pandas as pd

#scikit Learn: 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

#Muestreo aleatorio de árboles de decisión, creados a partir de porciones ligeramente distintas de conjuntos de datos originales
from sklearn.ensemble import RandomForestRegressor 

#cache de forma nativa
import joblib 

# Título y subtítulo, solo es un ejemplo
st.title("Rent Prediktor")
st.subheader("Predictor de Valor de Arriendos")

# Cachear modelo

@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_arriendos.pkl")

# carga *.cvs para presentarlo en un dataframe
datos = pd.read_csv("data/arriendos.csv")
st.write ('Data Frame de archivo *.csv para entrenamiento')
st.dataframe(datos)


# --------------------------
# FORMULARIO
# --------------------------

st.header("Predecir")

# presenta valores distintos, eliminando repetidos desde columna barrio
barrios = sorted(datos["barrio"].unique())

# crear caja de selección con barrios
barrio = st.selectbox(
    "Barrio", barrios
)

# crea caja de selección con tipos
tipo = st.selectbox(
    "Tipo",
    ["casa", "departamento", "local", "bodega","oficina","industrial","parcela","estacionamiento"]
)

superficie = st.number_input(
    "Superficie (m²)",
    min_value=9,
    value=42
)

estacionamientos = st.number_input(
    "Estacionamientos",
    min_value=0,
    value=1
)

dormitorios = st.number_input(
    "Dormitorios",
    min_value=0,
    value=1
)

banos = st.number_input(
    "Baños",
    min_value=1,
    value=1
)


# --------------
# BOTÓN PREDECIR
# --------------

if st.button("Predecir valor de arriendo"):

    try:

        modelo = joblib.load("modelo_arriendos.pkl") #carga de caché sino desde modelo en el disco

        nuevo = pd.DataFrame({
            "barrio": [barrio],
            "tipo": [tipo],
            "superficie": [superficie],
            "estacionamientos": [estacionamientos],
            "dormitorios": [dormitorios],
            "banos": [banos]
        })

        prediccion = modelo.predict(nuevo)

        #muestra resultado si la predicción es exitosa
        st.success(
            f"Arriendo estimado: ${prediccion[0]:,.0f} pesos chilenos"
        )

    # entrena al modelo primero o cachéalo primero antes de predecir
    except FileNotFoundError:
        st.error(
            "Primero debes entrenar el modelo."
        )


# --------------------------------
# FORMULARIO AGREGAR ENTRENAMIENTO
# --------------------------------

st.header("Agregar línea al entrenamiento")
st.write("En este formulario, envía datos reales arriendos en diferentes barrios de Puerto Montt, para poder aprender y generar una excelente predicción")

# presenta valores distintos, eliminando repetidos desde columna barrio
barrioX = st.text_input(
    "BarrioX",
    max_chars=30
)

# crea caja de selección con tipos
tipoX = st.selectbox(
    "TipoX",
    ["casa", "departamento", "local", "bodega","oficina","industrial","parcela","estacionamiento"]
)

superficieX = st.number_input(
    "SuperficieX (m²)",
    min_value=9,
    value=42
)

estacionamientosX = st.number_input(
    "EstacionamientosX",
    min_value=0,
    value=1
)

dormitoriosX = st.number_input(
    "DormitoriosX",
    min_value=0,
    value=1
)

banosX = st.number_input(
    "BañosX",
    min_value=1,
    value=1
)

arriendoX = st.number_input(
    "Valor arriendoX",
    min_value=10000,
    value=350000
)

#----------------------
# AGREGAR ENTRENAMIENTO
#----------------------

if st.button("Agregar datos al entrenamiento"):

    nuevo = pd.DataFrame({
        "barrio":[barrioX.lower()],
        "tipo":[tipoX.lower()],
        "superficie":[superficieX],
        "estacionamientos":[estacionamientosX],
        "dormitorios":[dormitoriosX],
        "banos":[banosX],
        "arriendo":[arriendoX]
    })

    datos = pd.concat([datos, nuevo], ignore_index=True)

    datos.to_csv("data/arriendos.csv", index=False)

    st.success("Registro agregado.")

#---------------
# BOTÓN ENTRENAR
#---------------

if st.button("Volver a entrenar modelo generativo"):

    # separa las variables de entrada (x) y la variable esperada (y)
    X = datos.drop(columns=["arriendo"])
    y = datos["arriendo"]

    # preprocesamiento transforma selecciones 'barrio' 'tipo' a datos binarios
    preprocesador = ColumnTransformer(
        transformers=[
            (
                "categoricas",
                OneHotEncoder(handle_unknown="ignore"),
                ["barrio", "tipo"] # datos que no representan un rango numérico.
            )
        ],
        remainder="passthrough"
    )

    # entrena modelo de regresión (Random Forest)
    modelo = Pipeline([
        ("prep", preprocesador),
        ("modelo", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ])

    #entrena de forma optimizada
    modelo.fit(X, y)

    # guarda archivo binario
    joblib.dump(modelo, "modelo_arriendos.pkl")

    st.success("Modelo entrenado correctamente.")


