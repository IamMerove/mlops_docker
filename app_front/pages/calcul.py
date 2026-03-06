import streamlit as st
import requests
import os

st.title("🧮 Calculateur MLOps")

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Formulaire de saisie
with st.form("compute_form"):
    number = st.number_input("Entrez un nombre", value=0.0)
    operation = st.selectbox("Choisissez l'opération", ["square", "add", "sub"])
    submit = st.form_submit_button("Calculer et Enregistrer")

if submit:
    # L'URL de ton API (qui tourne sur le port 8000)
    api_url = f"{BACKEND_URL}/compute/{operation}"

    try:
        response = requests.post(api_url, params={"value": number})
        if response.status_code == 200:
            res_data = response.json()
            st.success(f"Résultat : {res_data['data']['result']}")
            st.balloons()
        else:
            st.error(f"Erreur API : {response.status_code}")
    except Exception as e:
        st.error(f"Impossible de contacter l'API : {e}")
