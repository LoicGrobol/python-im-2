---
title: Python — M2 Ingénierie Multilingue 2018
---
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/LoicGrobol/python-im/master)

## Pratique
  - Loïc Grobol [\<loic.grobol@gmail.com\>](mailto:loic.grobol@gmail.com)
  - Yoann Dupont [\<yoa.dupont@gmail.com\>](mailto:yoa.dupont@gmail.com)
  - Le mercredi de 9h à 12h en salle 304 (Inalco, 2 rue de Lille, Paris) sauf indication contraire
  - Cette page : <https://loicgrobol.github.io/python-im/m2-2018>
  - [Consignes pour les projets](projets.md)

## Objectifs

Le cours a pour objectif de vous rendre autonome en programmation Python : apprendre les bases du langage, utiliser des modules, comprendre les messages d’erreur, trouver et comprendre la documentation.

L’accent sera mis sur le traitement de données textuelles et les problèmes liés aux données multilingues.

## Programme

Tous les supports sont sur [github](https://github.com/loicgrobol/python-im).

### 2018-09-19 : Passage en revue des bases en Python

  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=python-1.ipynb)
  - [Notebook : pierre-feuilles-ciseaux](../chifoumi.ipynb) :
    Télécharger le fichier .ipynb et dans le même dossier taper la commande
    ```bash
    python3 -m jupyter notebook chifoumi.ipynb
    ```
  - Exos : Chifoumi, Devinette ([correction](../exos/guess.py)), [Power of Thor - Episode 1](https://www.codingame.com/training/easy/power-of-thor-episode-1) ([correction](../exos/thor.py))

### 2018-09-26 : Précisions, fichiers et chaînes

  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=python-2.ipynb)
  - [Notebook dictionnaire-rimes](../dico-rimes.ipynb)
  - Exos : [temperatures](https://www.codingame.com/training/easy/temperatures) ([correction](../exos/temperatures.py))

### 2018-10-03 : Structures de données

  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=python-3.ipynb)
  - [Notebook vocabulaire-commun](../voc-commun.ipynb) : [les petits bourgeois](../balzac_petits-bourgeois.txt), [le ventre de Paris](../zola_ventre-de-paris.txt)
  - **Exos**
    - vocabulaire commun (à terminer),
    - À partir du fichier tsv [sem_Ef9POe.conll](../sem_Ef9POe.conll) ([correction](../exos/exo-conll.py))
        1. pour chaque POS listez les types classés par ordre d'occurrence décroissante,
        2. pour chaque type de chunk indiquez les longueurs min et max (en nb de mots).
    - [MIME type](https://www.codingame.com/training/easy/mime-type) ([correction](../exos/mime.py))


### 2018-10-10 (salle Les Salons)

  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=python-4.ipynb)
  - [Notebook multipos](../multipos.ipynb)
  - **Exos**
    - multipos (à terminer) ([correction](../exos/multipos.py)),
    - Lexique ([correction](../exos/lexique-able.py)): le suffixe `-able` (ou `-ible` ou `-uble`) est utilisé pour former des adjectifs à partir des verbes. Vous travaillerez avec les données de [lexique3.81](http://lexique.org/telLexique.php).
        1. Pour chaque verbe du premier groupe (utilisez le lemme) vous vérifierez s'il existe un adjectif en -able. Vous donnerez les décomptes en résultat (combien de verbes avec adjectif -able, combien sans)
        2. Pour chaque adjectif en -able vous vérifierez s'il existe un dérivé négatif (in-X-able, touchable/intouchable par ex.). En plus de l'affichage des comptes vous donnerez le pourcentage d'adjectifs en -able pour lesquels le dérivé négatif est plus fréquent (utilisez la colonne '7_freqlemfilms2).
    - Codin Game : [Racing duals](https://www.codingame.com/ide/puzzle/horse-racing-duals) ([correction](../exos/racing.py))

### 2018-10-17 (salle Les Salons)

  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=python-5.ipynb)
  - Exos :
    - [Scrabble](https://www.codingame.com/training/medium/scrabble) ([correction](../exos/scrabble.py))
    - [Python challenge 1](http://www.pythonchallenge.com/pc/def/map.html) (utiliser translate et maketrans)

### 2018-10-24 (salle Les Salons)
  - [Notebook CoNLL-U](../conllu_parse.ipynb) avec [fr_sequoia-ud-test.conllu](../fr_sequoia-ud-test.conllu) ([correction de la partie 1](../exos/conllu_crade.py))
  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=python-6.ipynb)
  - Exos :
    - [Shadow of the knight](https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1)
    - Finir le notebook CoNLL-U

### 2018-11-07 (salle Les Salons)
  - [Examen](exam.md)

### 2018-11-14
  - [Notebook parseurs](../parseurs.ipynb) ([la lettre de jopéshine](../josephine-1-150119.xml)) ([le notebook complété](../parseurs-complet.ipynb))
  - Exos :
    - exercices 1 et 2 du notebook parseurs
    - [la bataille](https://www.codingame.com/training/medium/winamax-battle)

### 2018-11-21
  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=modules.ipynb)

### 2018-11-28 (salle Les Salons)
  - [Notebooks autocomplete](../autocomplete/autocomplete1.ipynb)
  - données : [index.html](../autocomplete/index.html) et [serve.py](../autocomplete/serve.py)

### 2018-12-05 (salle Les Salons)
  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=modele_vectoriel.ipynb)
    - [Correction exercice 1](../exos/imbow.py)
    - [Correction exercice 2](../exos/imbow2.py)
    - [Correction exercice 3](../exos/tfidf.py)
  - [Mini-corpus imdb](../data/imdb/imdb_smol.tar.gz)

### 2018-12-12
  - [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im/master?filepath=visualisation.ipynb)


### 2018-12-19 (salle Les Salons)
  - [Version skorch](../skrch.py)
  - [Tensorflow playground](https://playground.tensorflow.org)

# Outils

Vous aurez besoin d'un interpréteur Python et d'un éditeur de texte.

## Python & co.
Vous travaillerons avec Python 3.

Les supports de cours sont sous forme de diapos html et surtout de notebooks. Pour utiliser les notebooks (anciennement ipython notebook maintenant jupyter notebook) vous aurez besoin d'installer [Jupyter](http://jupyter.org/) sur votre machine de travail.
Je vous incite également à utiliser le shell interactif `ipython` qui est une version améliorée du shell `python` (ipython est inclus dans jupyter).

Deux options pour l'installation :

* installer uniquement les outils nécessaires avec pip :
	1. installer Python3
	```bash
	sudo apt-get install python3
	```

	2. installer pip
	```bash
	sudo apt-get install python3-pip
	```

	3. installer jupyter
	```bash
	python3 -m pip install --user jupyter
	```

* Installer [anaconda](https://www.continuum.io/downloads). La solution de facilité qui comprend python3, pip, jupyter et une foule de modules dont on ne se serivra pas.


## Éditeur de texte
Pas un traitement de texte, pas un IDE, un *[éditeur de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte)*.

# Ressources

Il y a beaucoup, beaucoup de ressources disponibles pour apprendre Python. Ce qui suit n'est qu'une sélection.

## Livres

* How to think like a computer scientist, by Jeffrey Elkner, Allen B. Downey, and Chris Meyers.
Vous pouvez l'acheter. Vous pouvez aussi le lire [ici](http://openbookproject.net/thinkcs/python/english3e/)
* Dive into Python, by Mark Pilgrim.
[Ici](http://www.diveintopython3.net/) vous pouvez le lire ou télécharger le pdf.
* Learning Python, by Mark Lutz.
* Beginning Python, by Magnus Lie Hetland.
* Python Algorithms: Mastering Basic Algorithms in the Python Language, by Magnus Lie Hetland.
Peut-être un peu costaud pour des débutants.
* Programmation Efficace. Les 128 Algorithmes Qu'Il Faut Avoir Compris et Codés en Python au Cours de sa Vie, by Christoph Dürr and Jill-Jênn Vie.
Si le cours vous paraît trop facile. Le code Python est clair, les difficultés sont commentées. Les algos sont très costauds.

## Web

Je vous conseille vivement d'utiliser un (ou plus) des sites et tutoriels ci-dessous.

* [Coding Game](https://www.codingame.com/home). Vous le retrouverez dans les exercices hebdomadaires.
* [Code Academy](https://www.codecademy.com/fr/learn/python)
* [newcoder.io](http://newcoder.io/). Des projets commentés, commencer par 'Data Visualization'
* [Google's Python Class](https://developers.google.com/edu/python/). Guido a travaillé chez eux. Pas [ce Guido](http://vignette2.wikia.nocookie.net/pixar/images/1/10/Guido.png/revision/latest?cb=20140314012724), [celui-là](https://en.wikipedia.org/wiki/Guido_van_Rossum#/media/File:Guido_van_Rossum_OSCON_2006.jpg)
* [Mooc Python](https://www.fun-mooc.fr/courses/inria/41001S03/session03/about#). Un mooc de l'INRIA, carré.
* [Code combat](https://codecombat.com/)

## Licence

 Copyright © 2018 Loïc Grobol [\<loic.grobol@gmail.com\>](loic.grobol@gmail.com)

 Sauf indication contraire, les fichiers présents dans ce dépôt sont distribués selon les termes de la licence [MIT](LICENSE)

 Un résumé simplifié de cette licence est disponible à <https://tldrlegal.com/license/mit-license>.
