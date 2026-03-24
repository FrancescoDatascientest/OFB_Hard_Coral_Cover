import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import numpy as np

# --------- Configuration de la page ---------
st.set_page_config(page_title="Analyse de la couverture coralienne en Australie", layout="wide")

# --------- Chemin du CSV ---------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "GBR_ltmp.csv"

# --------- Lecture des données ---------
df = pd.read_csv(DATA_PATH)

df.replace({-999: np.nan, "-999": np.nan}, inplace=True)

# --------- Sidebar ---------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Accueil", "Analyse descriptive", "Analyse prédictive"])

st.sidebar.markdown("---")
st.sidebar.subheader("Membres de l'équipe")
st.sidebar.markdown("""
- [Francesco](https://www.linkedin.com/in/francesco-madrisotti-7281a0ba/)
- [Rova](https://www.linkedin.com/in/rovatiana-raboanarijaona/)
""")

# --------- Page : Accueil ---------
if page == "Accueil":
    st.title("Analyse de la couverture coralienne en Australie")
    st.markdown("""
    À travers ce support, nous présentons nos résultats de notre étude. 
    Nous avons 3 sessions : 
    - Dans la première, nous présentons la démarche et la donnée
    - Dans la deuxième, nous présentons l'analyse descriptive de la donnée
    - Dans la troisième, nous présentons l'analyse prédictive
    """)
    st.subheader("Aperçu des données")
    st.dataframe(df.head())

# --------- Page : Analyse descriptive ---------
elif page == "Analyse descriptive":
    st.title("Analyse descriptive")
    
    # Mapping des clusters
    cluster_mapping = {'CL1': 'Porites-A', 'CL2': 'Mixed', 'CL3': 'Soft-coral', 'CL4': 'Acropora'}
    df['Clust_names'] = df['CLUSTER'].map(cluster_mapping)
    
    # 1️⃣ Nombre de récifs par cluster
    st.subheader("Nombre de récifs distincts par cluster")
    st.markdown("Nous étudions le nombre de récif par cluster")
    reef_per_cluster = df.groupby("Clust_names")["REEF_NAME"].nunique().sort_values(ascending=True).reset_index()
    fig1 = px.bar(
        reef_per_cluster,
        x="REEF_NAME",
        y="Clust_names",
        orientation='h',
        text="REEF_NAME",
        labels={"REEF_NAME":"Nombre de récifs distincts", "Clust_names":"Cluster"},
        color="Clust_names"
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # 2️⃣ Évolution HC par type de corail
    st.subheader("Évolution de la couverture coralienne par type de corail")
    st.markdown("Nous examinons la couverture coralienne entre 1995 et 2015 par type de corail")
    table = df.groupby(["REPORT_YEAR", "Clust_names"])["HC"].mean().reset_index()
    fig2 = px.line(
        table,
        x="REPORT_YEAR",
        y="HC",
        color="Clust_names",
        markers=True,
        labels={"HC":"HC moyen", "REPORT_YEAR":"Année", "Clust_names":"Cluster"}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # 3️⃣ Évolution HC par plateau récifal
    st.subheader("Évolution de la couverture coralienne par plateau récifal")
    st.markdown("Nous examinons l'évolution de la couverture coralienne par plateau récifal entre 1995 et 2015")
    table_shelf = df.groupby(["REPORT_YEAR", "SHELF"])["HC"].mean().reset_index()
    fig3 = px.line(
        table_shelf,
        x="REPORT_YEAR",
        y="HC",
        color="SHELF",
        markers=True,
        labels={"HC":"HC moyen", "REPORT_YEAR":"Année", "SHELF":"Plateau récifal"}
    )
    st.plotly_chart(fig3, use_container_width=True)

# --------- Page : Analyse prédictive ---------
elif page == "Analyse prédictive":
    st.title("Analyse prédictive")
    
    st.markdown("""
    Dans cette section, nous présentons les résultats de notre modèle de prédiction basé sur Random Forest.
    """)
    
    # Résultats du modèle
    st.subheader("Résultats du modèle Random Forest")
    st.markdown("""
    Les résultats de notre modèle Random Forest sont les suivants :
    
    - **MSE** : 87.17  
    - **MAE** : 6.90  
    - **R²** : 0.63  
    """)

    # --------- Section évaluation ---------
    st.subheader("Évaluation du modèle")
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    IMG_PATH = BASE_DIR / "images"

    st.markdown("### Relation entre les prédictions et les vraies valeurs")
    st.markdown("Ici nous visualisons la relation entre les prédictions et les vraies valeurs.")
    st.image(str(IMG_PATH / "pred_vs_errors.png"))

    st.markdown("### Analyse sur Chicken Reef")
    st.markdown("Nous voulons visualiser les prédictions sur un récif, notamment Chicken Reef.")

    st.markdown("**Vraies valeurs :**")
    st.image(str(IMG_PATH / "chicken_reef.png"))

    st.markdown("**Prédictions :**")
    st.image(str(IMG_PATH / "chicken_reef_pred.png"))

    st.markdown("### Importance des variables (SHAP)")
    st.markdown("""
    Enfin, nous étudions comment les variables influencent la prédiction du modèle à l’aide des valeurs SHAP.
    """)
    st.image(str(IMG_PATH / "shap.png"))