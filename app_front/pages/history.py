import streamlit as st
import requests
import pandas as pd

st.title("📜 Historique des calculs")

if st.button("Actualiser les données"):
    try:
        response = requests.get("http://backend:8000/data")
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                st.table(df)  # Affiche un joli tableau
            else:
                st.info("La base de données est vide.")
        else:
            st.error("Erreur lors de la récupération des données.")
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")
