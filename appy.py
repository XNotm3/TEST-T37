import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Análisis Determinista de Personalidad",
    layout="wide"
)

st.title("Análisis Determinista Multicapa – Modelo Sapolsky")
st.caption("Este sistema no evalúa libre albedrío. Analiza condiciones causales.")

LIKERT_5 = {
    1: "Muy bajo / Nunca",
    2: "Bajo / Rara vez",
    3: "Moderado",
    4: "Alto / Frecuente",
    5: "Muy alto / Siempre"
}

def likert_question(question, key):
    return st.radio(
        question,
        options=list(LIKERT_5.keys()),
        format_func=lambda x: LIKERT_5[x],
        horizontal=True,
        key=key
    )

st.header("Capa 1 — Inmediata (segundos–minutos)")
c1 = [
    likert_question("Impulsividad ante estímulos inmediatos", "c1_q1"),
    likert_question("Reactividad emocional inmediata", "c1_q2"),
    likert_question("Capacidad de inhibición en caliente", "c1_q3"),
    likert_question("Sensibilidad a hambre / incomodidad", "c1_q4"),
]

st.header("Capa 2 — Hormonal y fisiológica (horas–días)")
c2 = [
    likert_question("Nivel de estrés basal", "c2_q1"),
    likert_question("Calidad del sueño", "c2_q2"),
    likert_question("Energía física diaria", "c2_q3"),
    likert_question("Estabilidad emocional según fatiga", "c2_q4"),
]

st.header("Capa 3 — Experiencias recientes y aprendizaje")
c3 = [
    likert_question("Rigidez de hábitos actuales", "c3_q1"),
    likert_question("Capacidad de modificar rutinas", "c3_q2"),
    likert_question("Dependencia de refuerzos externos", "c3_q3"),
    likert_question("Respuesta adaptativa al error", "c3_q4"),
]

st.header("Capa 4 — Desarrollo temprano")
c4 = [
    likert_question("Inseguridad de apego", "c4_q1"),
    likert_question("Exposición temprana a estrés", "c4_q2"),
    likert_question("Necesidad de control aprendida", "c4_q3"),
    likert_question("Supresión emocional aprendida", "c4_q4"),
]

st.header("Capa 5 — Prenatal y perinatal")
c5 = [
    likert_question("Probable estrés prenatal", "c5_q1"),
    likert_question("Complicaciones perinatales", "c5_q2"),
]

st.header("Capa 6 — Genética y evolutiva")
c6 = [
    likert_question("Carga hereditaria de impulsividad/afectividad", "c6_q1"),
    likert_question("Presencia de patrones familiares repetidos", "c6_q2"),
]

st.header("Capa 7 — Cultural, histórica y ecológica")
c7 = [
    likert_question("Presión cultural disonante con tu biología", "c7_q1"),
    likert_question("Rigidez del entorno social", "c7_q2"),
]

if st.button("Generar análisis determinista"):
    layers = {
        "Capa 1 – Inmediata": np.mean(c1),
        "Capa 2 – Fisiológica": np.mean(c2),
        "Capa 3 – Aprendizaje": np.mean(c3),
        "Capa 4 – Desarrollo temprano": np.mean(c4),
        "Capa 5 – Prenatal": np.mean(c5),
        "Capa 6 – Genética": np.mean(c6),
        "Capa 7 – Cultural": np.mean(c7),
    }

    df = pd.DataFrame.from_dict(layers, orient="index", columns=["Impacto causal"])
    df["Impacto causal"] = df["Impacto causal"].round(2)

    st.subheader("Mapa causal del individuo")
    st.dataframe(df, use_container_width=True)

    st.subheader("Interpretación determinista")

    sorted_layers = df.sort_values("Impacto causal", ascending=False)

    st.markdown("### Capas dominantes (mayor peso causal)")
    for layer, row in sorted_layers.iterrows():
        if row["Impacto causal"] >= 3.5:
            st.markdown(f"- **{layer}** → Alta influencia actual")

    st.markdown("### Capas con mayor modificabilidad práctica")
    for layer in ["Capa 1 – Inmediata", "Capa 2 – Fisiológica", "Capa 3 – Aprendizaje"]:
        score = df.loc[layer, "Impacto causal"]
        st.markdown(f"- **{layer}** | Impacto: {score}")

    st.markdown("### Diagnóstico sintético")
    st.write(
        """
        Tu conducta actual es el resultado predecible de capas profundas (genética, desarrollo temprano),
        moduladas por estados fisiológicos y hábitos recientes.
        
        El cambio real no ocurre por voluntad abstracta, sino por:
        - Reingeniería del entorno inmediato
        - Regulación fisiológica sistemática
        - Rediseño de refuerzos y rutinas
        """
    )

    st.markdown("### Punto crítico")
    st.write(
        "La capa con mayor retorno de inversión conductual es aquella con alto impacto y alta modificabilidad "
        "(generalmente Capa 2 o 3)."
    )
