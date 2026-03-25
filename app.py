import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

st.set_page_config(page_title="Analyse Beans & Pods", layout="wide", page_icon="☕")

st.title("☕ Tableau de Bord Analytique - Beans & Pods")
st.markdown("Application interactive pour l'exploration des données de ventes et recommandations stratégiques.")

st.divider() 

chemin_fichier = "BeansDataSet.csv"
df = pd.read_csv(chemin_fichier)

st.header("1. Aperçu des données de ventes")
st.write("Voici un échantillon des transactions récentes :")
st.dataframe(df.head(), use_container_width=True)

st.header("2. Étude Statistique Descriptive")
st.write("Résumé des performances (moyennes, minimums, maximums) par type de café :")
st.dataframe(df.describe(), use_container_width=True)

st.divider()

st.header("3. Visualisation des Tendances")
st.write("Exploration des modèles et tendances dans les données de vente.")

st.subheader("Ventes Totales par Canal (Store vs Online)")
channel_sales = df.groupby('Channel').sum(numeric_only=True).sum(axis=1)
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(x=channel_sales.index, y=channel_sales.values, ax=ax1, palette="Blues")
ax1.set_ylabel("Volume Total (Unités)")
sns.despine() 
st.pyplot(fig1)

st.subheader("Ventes Totales par Région")
region_sales = df.groupby('Region').sum(numeric_only=True).sum(axis=1)
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(x=region_sales.index, y=region_sales.values, ax=ax2, palette="Greens")
ax2.set_ylabel("Volume Total (Unités)")
sns.despine()
st.pyplot(fig2)

st.subheader("Répartition des ventes par type de produit")
product_sales = df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].sum()
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(x=product_sales.index, y=product_sales.values, ax=ax3, palette="magma")
ax3.set_ylabel("Volume de Ventes (Unités)")
sns.despine()
st.pyplot(fig3)

st.divider()

st.header("4. Recommandations pour la Campagne Marketing")
st.info("""
**Analyse des Modèles :**
- Les produits phares comme le **Robusta** et l'**Espresso** génèrent la majorité des revenus.
- Le canal et la région avec les volumes de ventes les plus élevés représentent vos marchés les plus rentables.

**Recommandations pour Angeli VC et les Propriétaires :**
1. **Marketing Ciblé :** Concentrez la nouvelle campagne publicitaire sur les régions dominantes, en priorisant les achats en ligne (Online) ou en magasin (Store) en fonction des tendances observées sur les graphiques ci-dessus.
2. **Ventes Croisées (Cross-Selling) :** Proposez des promotions groupées (ex: un paquet d'Espresso populaire acheté = une remise sur les dosettes Latte moins vendues).

**Données supplémentaires à collecter à l'avenir :**
- **Profil Démographique :** L'âge et le genre des clients pour des publicités plus précises.
- **Dates de Transactions :** Le jour et le mois de l'achat pour identifier la saisonnalité (ex: ventes plus fortes en hiver).
- **Avis Clients :** Un score de satisfaction pour chaque type de café.
""")