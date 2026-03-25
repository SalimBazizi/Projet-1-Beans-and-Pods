# Étude Statistique Descriptive : Ventes "Beans & Pods"

## 1. Description du Jeu de Données

Le jeu de données analysé contient 440 enregistrements de transactions de vente. L'analyse porte sur deux variables catégorielles (Canal de vente et Région) et six variables quantitatives continues représentant le volume de ventes de différents types de café.

## 2. Variables Catégorielles (Qualitatives)

- **Channel (Canal de vente) :** Divisé en deux catégories : `Store` (Magasin physique) et `Online` (En ligne). L'analyse de fréquence montre une répartition des volumes d'achat très distincte selon le canal.
- **Region (Région géographique) :** Les transactions sont réparties sur trois zones : `North`, `Central`, et `South`.

## 3. Variables Quantitatives (Performances des Produits)

Une analyse des mesures de tendance centrale (moyenne, médiane) et de dispersion (écarts-types, minimums et maximums) a été générée via la fonction `describe()` de la bibliothèque Pandas. Voici les observations clés :

- **Grains classiques (Robusta et Arabica) :** Ces deux catégories présentent les moyennes de vente les plus élevées du jeu de données, ainsi que la plus forte variance. Les valeurs maximales (pics de ventes) sur ces produits atteignent des dizaines de milliers d'unités par transaction, indiquant qu'ils constituent le cœur de métier historique de Beans & Pods.
- **Dosettes spécialisées (Espresso, Lungo, Latte, Cappuccino) :**
  - L'**Espresso** se détache nettement comme la dosette la plus populaire, avec un volume moyen de ventes très supérieur aux autres.
  - Le **Lungo**, le **Latte** et le **Cappuccino** affichent des médianes beaucoup plus basses. La présence de valeurs minimales proches de zéro ou à un chiffre montre que ces produits ne sont pas systématiquement inclus dans les paniers d'achat.

## 4. Analyse Bivariée (Corrélations préliminaires)

- **Canal vs Volume :** Bien que le canal `Store` génère traditionnellement de gros volumes (achats de gros ou réguliers), le segment `Online` affiche des pics très marqués sur certains produits, soulignant le potentiel de la récente levée de fonds pour l'e-commerce.
- **Région vs Produits :** La répartition géographique n'est pas homogène. Certaines régions surperforment nettement et concentrent la majorité du chiffre d'affaires total.

## 5. Conclusion Statistique

La distribution des données est fortement asymétrique (présence de valeurs extrêmes très élevées, ou "outliers", tirant la moyenne vers le haut). Le catalogue de Beans & Pods repose sur le principe de Pareto : une minorité de références (Robusta, Arabica, Espresso) génère la vaste majorité des volumes traités.
