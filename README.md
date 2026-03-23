# Hard Coral Cover Project

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange?logo=jupyter&logoColor=white)
 
Ce dépôt contient tous les éléments nécessaires pour reproduire les analyses réalisées sur les données du projet **Hard Coral Cover**.

---

## Structure du projet

- **`notebooks/`** : contient les notebooks Jupyter pour les différentes analyses :  
  - `ofb_00_exploration.ipynb` – Notebook d’exploration des données.  
  - `ofb_01_analysis.ipynb` – Notebook de la première analyse.  
  - `ofb_02_advanced_ml.ipynb` – Analyse avancée utilisant des méthodes de **machine learning**.  
  - `ofb_02_advanced_bayesian.ipynb` – Analyse avancée utilisant des modèles **bayésiens**.

- **`data/`** : contient tous les fichiers de données nécessaires pour reproduire les analyses.  
 > **Remarque :** il n’est pas recommandé de stocker les données directement dans le dépôt Git. Les fichiers de données doivent être ajoutés **manuellement** dans ce dossier après avoir été récupérés depuis leur source externe. De manière un peu exceptionnelle, ce dépôt contient les données.

- **`rapports/`** : contient les rapports générés pour la première et la deuxième analyse.

---

## Récupérer le projet

1. **Cloner le dépôt avec Git (recommandé)**  

```bash
git clone https://github.com/FrancescoDatascientest/OFB_Hard_Coral_Cover.git
cd OFB_Hard_Coral_Cover
```

## Télécharger le projet (ZIP)

Si vous ne souhaitez pas utiliser Git, vous pouvez télécharger le projet en ZIP :  

1. Aller sur le dépôt GitHub.  
2. Cliquer sur **Code → Download ZIP**.  
3. Extraire le ZIP sur votre ordinateur.  
4. Ouvrir le dossier extrait `OFB_Hard_Coral_Cover`.  

> **Important :** Gardez la structure des dossiers telle qu’elle est :  
> ```
> OFB_Hard_Coral_Cover/
> ├─ notebooks/
> ├─ data/
> └─ rapports/
> ```

---

## Installer l’environnement Python et les dépendances

1. Créez un environnement conda (ou virtualenv) :  

```bash
conda create -n pymc_ofb python=3.12
conda activate pymc_ofb
```

2. Installez les packages nécessaires :

```bash
pip install -r requirements.txt
```
> Cette étape installe toutes les bibliothèques nécessaires pour exécuter les notebooks.

## Placer les fichiers de données

- Les fichiers `.csv` et `.xlsx` doivent être placés dans le dossier `data/`.  
- **Ne changez pas les noms des fichiers**, sinon les notebooks pourraient ne pas fonctionner.  

> Exemple :  
> ```
> data/
> ├─ GBR_ltmp.csv
> └─ summary_trace.csv
> ```

---

## Lancer les notebooks

- Ouvrez Jupyter Notebook ou JupyterLab :  

```bash
jupyter notebook
```
## Les notebooks

Les notebooks sont dans le dossier `notebooks/` :

- `ofb_00_exploration.ipynb` → exploration des données  
- `ofb_01_analysis.ipynb` → première analyse  
- `ofb_02_advanced_ml.ipynb` → analyse avancée **machine learning**  
- `ofb_02_advanced_bayesian.ipynb` → analyse avancée **bayésienne**  

> Exécutez-les dans l’ordre souhaité pour reproduire les résultats.

---

## Consulter les rapports

Les résultats et conclusions sont disponibles dans le dossier `rapports/` pour chaque analyse.