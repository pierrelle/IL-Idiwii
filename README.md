# IL-Idiwii

  
## Notebooks

Les notebooks intéressants sont placés dans le dossier `src`

- `DatasetMetrics`: fournit des statistiques sur les datasets situés dans le fichier `data` 
- `Visualization`: donne des visuels sur un modèle qui tourne en local sur la machine
- `SpacyModel` : crée un modèle SpaCy français pour de la classification d'intention, l'entraîne sur les jeux de données du fichier `data`, et enregistre le modèle

  
  

## Execution

  

### Préalable

  

Pour executer n'importe quel notebook, il est nécéssaire de placer préalablement les fichiers `training_set.json` et `testing_set.json` dans un dossier "data", qui doit être situé à la racine du projet. 
Ensuite, après avoir créer un environnement virtuel et vous être placé dedans, les librairies et modèles peuvent être installés grâce à la commande `make init`.

  

### Image docker

  

Pour utiliser le notebook `visualization.ipynb`, il faut que l'image docker d'un modèle tourne en local sur la machine. Pour cela ouvrez un terminal pour y saisir :

  

`docker pull <nom du modèle>` avec pour nom de modèle "wiidiiremi/projet_industrialisation_ia_3a" pour le modèle fourni par Idiwii, ou "pcroissant/il_idiwii" pour le modèle crée avec SpaCy

puis `docker images` pour obtenir l'ID de l'image

et enfin `docker run -p 8080:8080 <id de l'image>`.

  Si l'image tourne bien, le notebook `visualization.ipynb` est alors prêt à l'utilisation.
