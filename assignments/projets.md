Projets Python 2019
===================

Votre travail sera de réaliser une ressource, une interface ou une bibliothèque pour Python.
Son thème devra être lié au TAL ou au traitement de données et pourra évidemment
être en lien avec d'autres cours ou d'autres projets.

*Bien entendu rien ne vous empêche de combiner ces options.*

## Consignes

- Projet à rendre le XX janvier *au plus tard*
- Projet collectif, par groupe de 2 ou 3 (sauf exception)

Le rendu devra comporter :

1. Une documentation du projet traitant les points suivants :

   - Les objectifs du projet
   - Les données (origine, format, statut juridique) et les traitements opérés
     sur celles-ci
   - La méthodologie (comment vous vous êtes répartis le travail, comment vous
     avez identifié les problèmes et les avez résolus, différentes étapes du
     projet…)
   - L'implémentation ou les implémentations (modélisation le cas échéant,
     modules et/ou API utilisés, différents langages le cas échéant)
   - Les résultats (fichiers output, visualisations…) et une discussion sur ces
     résultats (ce que vous auriez aimé faire et ce que vous avez pu faire par
     exemple)

   On attend de la documentation technique, pas une dissertation. Elle pourra
   prendre la format d'un ou plusieurs fichiers, d'un site web, d'un notebook de
   démonstration, à votre convenance

2. Le code Python et les codes annexes (JS par ex.) que vous avez produit.
   Le code *doit* être commenté. Des tests ce serait bien. **Évitez les
   notebooks**, préférez les interfaces en ligne de commande ou web (ou
   graphiques si vous êtes très motivé⋅e⋅s)

3. Les éventuelles données en input et en output (ou un échantillon si le volume
   est important)

## Conseils

Écrivez ! Tenez un carnet : vos questions, un compte-rendu de vos discussions,
les problèmes rencontrés, tout est bon à prendre et cela vous aidera à rédiger
la documentation finale.

### Données géo-localisées

Il existe beaucoup de choses pour travailler avec des données géo-localisées.
Allez voir en vrac : [Geo-JSON](http://geojson.org/),
[uMap](http://umap.openstreetmap.fr/fr/) pour créer facilement des cartes en
utilisant les fonds de carte d'OpenStreetMap, [leaflet](http://leafletjs.com/)
une lib JS pour les cartes interactives, [overpass
turbo](http://overpass-turbo.eu/) pour interroger facilement les données
d'OpenStreetMap (il y a une [api !](http://www.overpass-api.de/)).

### Ressources linguistiques

N'hésitez pas à aller fouiller dans [Ortolang](https://www.ortolang.fr/) ou
[Clarin](https://lindat.mff.cuni.cz/repository/xmlui/) des ressources
linguistiques exploitables librement et facilement. Vous pouvez aussi aller voir
du côté de l'API twitter pour récupérer des données (qui ne sont pas
nécessairement uniquement linguistiques)

### Open Data

Quelques sources : [Paris Open Data](https://opendata.paris.fr),
[data.gouv.fr](https://data.gouv.fr), [Google dataset
search](https://toolbox.google.com/datasetsearch)

### Web avec Python

Bye bye CGI. Utilisez un framework : [Flask](http://flask.pocoo.org/),
[Bottle](http://bottlepy.org), [Tornado](http://tornado.readthedocs.io/),
[Django](https://www.djangoproject.com/) si vous utilisez une BD relationnelle.

## Exemples de sujets

### Accès aux données

Réaliser une interface pour exploiter une ressource (linguistique ou autre).

- Soit en rendant lisible des données massives en faisant des stats
- Soit en faisant apparaître des représentations pertinentes de données
  individuelles complexes (syntaxe, entités nommées, sentiment…)
- …

### Conception de ressources

Créer une ressource et en proposer des exploitations simples : par exemple,
autour des midterms 2018, un jeu de données mettant en relation les sondages,
les résultats et l'activité sur Twitter

### Scorers

Implémenter un scorer pour une mesure intéressante : CER, LAS/UAS, accords
inter-annotateurs…

### Formats de données

Conversion entre formats de données pour le TAL, visualiseurs…

### Ressource lexicale

Créer un lexique intentionnel que l'on pourra enrichir ("règles" pour créer des
entrées depuis un lemme).

### Tagger

Créer un POS tagger basé sur le LeFFF.

### Classifieur

Créer un classifieur de documents pour retrouver les [catégories
thématiques](https://fr.wikinews.org/wiki/Page:Sommaire) d'articles wikinews.
