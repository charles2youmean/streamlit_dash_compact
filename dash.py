import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Configuration large pour une meilleure mise en page
st.set_page_config(layout="wide")

# Titre principal
st.title("Maquette de tableau de bord avec cartes zoomables")

# Bande grise latérale
with st.sidebar:
    st.header("Connexion et navigation")
    st.text("Interface de connexion utilisateur")
    st.text("Navigation dans les projets")

# Menu déroulant pour les options
col_menu1, col_menu2 = st.columns(2)
with col_menu1:
    menu_option1 = st.selectbox("Sélectionnez une catégorie :", ["Option 1", "Option 2", "Option 3"])
with col_menu2:
    menu_option2 = st.selectbox("Sélectionnez une métrique :", ["Métrique A", "Métrique B", "Métrique C"])

# Mise en page avec des colonnes pour les cartes
col1, col2, col3 = st.columns([1, 1, 1])

# Carte 1 : Histogramme 1
with col1:
    with st.expander("Histogramme 1 : Répartition des catégories"):
        st.write("Cet histogramme montre la répartition des catégories pour un ensemble de données fictives.")
        data1 = pd.DataFrame({
            "Catégorie": [f"Cat {i+1}" for i in range(8)],
            "Valeur": [10, 23, 45, 12, 34, 56, 27, 30]
        })
        fig1 = px.bar(data1, x="Catégorie", y="Valeur", title="Histogramme 1", text_auto=True)
        st.plotly_chart(fig1, use_container_width=True)

# Carte 2 : Histogramme 2
with col2:
    with st.expander("Histogramme 2 : Comparaison des valeurs"):
        st.write("Cet histogramme compare les valeurs entre différents groupes fictifs.")
        data2 = pd.DataFrame({
            "Groupe": [f"Groupe {i+1}" for i in range(8)],
            "Score": [15, 28, 34, 20, 40, 50, 25, 35]
        })
        fig2 = px.bar(data2, x="Groupe", y="Score", title="Histogramme 2", text_auto=True)
        st.plotly_chart(fig2, use_container_width=True)

# Carte 3 : Camembert
with col3:
    with st.expander("Camembert : Part des segments"):
        st.write("Ce camembert illustre la répartition des segments dans l'ensemble de données.")
        pie_data = pd.DataFrame({
            "Segment": [f"Segment {i+1}" for i in range(5)],
            "Pourcentage": [20, 15, 25, 30, 10]
        })
        fig3 = px.pie(pie_data, names="Segment", values="Pourcentage", title="Camembert")
        st.plotly_chart(fig3, use_container_width=True)

# Carte 4 : Radial tree et Nuage de mots (même ligne)
col_radial, col_cloud = st.columns(2)

with col_radial:
    with st.expander("Radial Tree : Visualisation hiérarchique"):
        st.write("Ce graphique montre une hiérarchie fictive dans les données.")
        data_tree = {
            "name": "Root",
            "children": [
                {"name": "Branch 1", "children": [
                    {"name": "Leaf 1"},
                    {"name": "Leaf 2"}
                ]},
                {"name": "Branch 2", "children": [
                    {"name": "Leaf 3"},
                    {"name": "Leaf 4"}
                ]}
            ]
        }
        fig4 = go.Figure(go.Sunburst(
            labels=["Root", "Branch 1", "Branch 2", "Leaf 1", "Leaf 2", "Leaf 3", "Leaf 4"],
            parents=["", "Root", "Root", "Branch 1", "Branch 1", "Branch 2", "Branch 2"],
            values=[10, 20, 30, 5, 5, 10, 10],
        ))
        fig4.update_layout(margin=dict(t=10, l=10, r=10, b=10))
        st.plotly_chart(fig4, use_container_width=True)

with col_cloud:
    with st.expander("Nuage de mots : Fréquence des mots"):
        st.write("Ce nuage montre les mots les plus fréquents dans un corpus fictif.")
        words = "Streamlit Data Visualization Python Dashboard Interactive" * 10
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(words)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

# Carte 5 : Histogramme large
with st.expander("Histogramme large : 25 entrées"):
    st.subheader("Histogramme large : 25 entrées")
    st.write("Ce graphique illustre un histogramme large avec 25 catégories fictives.")
    data_large = pd.DataFrame({
        "Catégorie": [f"Cat {i+1}" for i in range(25)],
        "Valeur": [i * 10 % 40 + 10 for i in range(25)]
    })
    fig_large = px.bar(data_large, x="Catégorie", y="Valeur", title="Histogramme large", text_auto=True)
    st.plotly_chart(fig_large, use_container_width=True)

# Résumé texte
with st.expander("Résumé texte"):
    st.subheader("Résumé texte")
    st.write("Voici un résumé fictif de 15 lignes expliquant les résultats du tableau de bord.")
    long_text = """
    1. Les histogrammes montrent une répartition variée des catégories et groupes.
    2. Le camembert illustre les parts relatives des segments étudiés.
    3. Les catégories Cat 3 et Cat 6 se démarquent par leurs valeurs élevées.
    4. Le Groupe 6 possède le score le plus élevé, suivi du Groupe 5.
    5. La répartition des segments est globalement équilibrée.
    6. Le Segment 4 représente la part la plus importante.
    7. Des variations significatives sont visibles entre les catégories.
    8. Les données sont fictives et utilisées à titre d'exemple.
    9. L'interface est conçue pour une navigation intuitive.
    10. L'agencement compact facilite la visualisation des résultats.
    11. Le radial tree fournit une vue hiérarchique des données.
    12. Les valeurs extrêmes méritent une analyse plus approfondie.
    13. Les histogrammes mettent en évidence les contrastes clés.
    14. Le camembert simplifie la compréhension des proportions.
    15. Ce tableau de bord est une démonstration des capacités de Streamlit.
    """
    st.text(long_text)
