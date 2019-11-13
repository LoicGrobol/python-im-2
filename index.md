---
title: Python — M2 Ingénierie Multilingue 2019
---
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/LoicGrobol/python-im-2/master)

## Pratique

- Loïc Grobol [\<loic.grobol@gmail.com\>](mailto:loic.grobol@gmail.com)
- Yoann Dupont [\<yoa.dupont@gmail.com\>](mailto:yoa.dupont@gmail.com)
- Le mercredi de 9h à 12h en salle 7,03 (Inalco PLC, 65 rue des Grands Moulins Paris) sauf
  indication contraire
- Cette page : <https://loicgrobol.github.io/python-im-2>
- [Consignes pour les projets](/assignments/projets.md)

## Objectifs

Ce cours a pour objectif de faire de vous des développeuses et des développeurs opérationnels en
Python, il suppose que vous êtes déjà en grande partie autonomes dans pour une utilisation simple de
Python, ce qui correspond essentiellement aux acquis [du cours de
M1](https://clement-plancq.github.io/python-im/m1-2018/) (même si des rappels seront faits aux
moments opportuns).

Vous y seront présentés des concepts et de fonctions avancées du langage, ainsi que des outils de
développement standards, en insistant sur les bonnes pratiques, la collaboration et la
réutilisabilité.
L’accent sera mis sur le traitement de données textuelles et les problèmes liés aux données
multilingues.

## Programme

Tous les supports sont sur [github](https://github.com/loicgrobol/python-im-2), les liens vers les
slides et les notebooks ci-dessous ouvrent sur Binder pour une utilisation sans rien installer.

### 2019-09-18 : Rappel des bases

- [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/1-man-1.ipynb)
  (énoncés rectifiés!)
- corrections:
  - [exercices du notebook](./corrections/man_1.py)
  - [ASCII art](./corrections/ascii_art.py)

### 2019-09-18 : Rappel des bases (2)

- [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/2-man-2.ipynb)
- Exos:
  - exercices à la fin du notebook sur [le ventre de Paris](./data/zola_ventre-de-paris.txt)
- Corrections:
  - [The descent](/corrections/the_descent.py)
  - [Zola](/corrections/zola.py)

### 2019-10-02 : Objets et modules

- [Slides objets](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/3a-oop.ipynb)
- [Slides modules](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/3b-modules.ipynb)
- Exos:
  - Exercices à la fin du notebook modules, à partir de [`fixme.py`](/data/fixme.py)
  - [Codingame Enigma](https://www.codingame.com/ide/puzzle/encryptiondecryption-of-enigma-machine)

### 2019-10-09 : récursion

- [Slides](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/4a-recursion.ipynb)
- Exo préliminaire:
  - Complétez le [script](./data/parse_conllu.py) qui parse le [fichier
    conll](./data/fr_gsd-ud-test.conllu) et donne le nombre de phrases, le
    nombre de tokens et le nombre de tokens d’une catégorie morpho-syntaxique
    choisie par l’utilisateur. Trouver les tokens dont le lemme se termine en
    ‘ment’ qui ne sont pas des adverbes, les afficher triés par forme et par
    fonction.
- Exos:
  - [Codingame Brackets](https://www.codingame.com/training/easy/brackets-extreme-edition)
  - exercices à la fin du notebook
- Corrections:
  - [Brackets](/corrections/brackets.py)
  - [Arbres binaires](/corrections/recursion.py)

### 2019-10-15 : exoooooos

- [Codingbat](https://codingbat.com/python)
- [Examen 2018](/data/exam-2018.md)

### 2019-10-23 : examen et projets

- [Sujet de l'examen](/exam/exam-2019.md)
- [Consignes pour les projets](/assignments/projets.md)

### 2019-11-04 : ~~git~~ exos et exercice incendie

- [Exercices de décrassage](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/7a-exos.ipynb)
  - [testcase](/data/7.0-testcase.txt) et [cible](/data/7.0-target.txt)


### 2019-11-13 : git
- [Exercices de décrassage](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/8a-exos.ipynb)
- [slides git](https://mybinder.org/v2/gh/loicgrobol/python-im-2/master?filepath=slides/8b-git.ipynb)
- [Learn git branching](https://learngitbranching.js.org/)
- [Exercice git](https://github.com/LoicGrobol/fixme)

## Outils

Vous aurez besoin d'un interpréteur Python et d'un éditeur de texte.

### Python & co

Vous travaillerons avec Python 3.7 et supérieur

Les supports de cours sont essentiellement sous forme de notebooks  [Jupyter](http://jupyter.org/),
les diapos utilisant [RISE](https://github.com/damianavila/RISE).
Pour utiliser les notebooks (anciennement ipython notebook maintenant jupyter notebook) vous aurez
besoin d'installer sur votre machine de travail.
Je vous incite également à utiliser le shell interactif `ipython` qui est une version améliorée du
shell `python` (ipython est inclus dans jupyter).

Deux options pour l'installation :

#### Installer uniquement les outils nécessaires avec pip

1. Installer Python 3, de préférence via le gestionnaire de paquets de votre système, sinon à partir
   de <https://www.python.org/downloads/>.
   Pour les distributions dérivées de Debian (y compris Ubuntu) vous aurez également besoin
   d'installer `pip`

      ```bash
      sudo apt install python3 python3-pip
      ```

2. Installer jupyter

      ```bash
      python3 -m pip install --user jupyter
      ```

#### Utiliser Anaconda

Nous ne le recommandons pas, mais si vous préférez, vous pouvez installer
[anaconda](https://www.continuum.io/downloads), qui gère non-seulement Python et les modules Python,
mais aussi beaucoup d'autres paquets et installera
beaucoup de modules tiers dont on se servira pas

Nous verrons également dans le cours comment utiliser [virtualenv](https://virtualenv.pypa.io) pour
gérer des installations de Python isolées du système pour plus de confort.

### Éditeur de texte

Dans un premier temps : pas un traitement de texte, pas un IDE, un *[éditeur de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte)*.

Une fois que vous êtes à l'aise pour développer dans un éditeur de texte, vous pouvez si vous le
désirez passer à un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement)

## Ressources

Il y a beaucoup, beaucoup de ressources disponibles pour apprendre Python. Ce qui suit n'est qu'une sélection.

## Livres

- How to think like a computer scientist, by Jeffrey Elkner, Allen B. Downey, and Chris Meyers.
Vous pouvez l'acheter. Vous pouvez aussi le lire [ici](http://openbookproject.net/thinkcs/python/english3e/)
- Dive into Python, by Mark Pilgrim.
[Ici](http://www.diveintopython3.net/) vous pouvez le lire ou télécharger le pdf.
- Learning Python, by Mark Lutz.
- Beginning Python, by Magnus Lie Hetland.
- Python Algorithms: Mastering Basic Algorithms in the Python Language, by Magnus Lie Hetland.
Peut-être un peu costaud pour des débutants.
- Programmation Efficace. Les 128 Algorithmes Qu'Il Faut Avoir Compris et Codés en Python au Cours
  de sa Vie, by Christoph Dürr and Jill-Jênn Vie. Si le cours vous paraît trop facile. Le code
  Python est clair, les difficultés sont commentées. Les algos sont très costauds.

## Web

Il vous est vivement conseillé d'utiliser un (ou plus) des sites et tutoriels ci-dessous.

- [Coding Game](https://www.codingame.com/home). Vous le retrouverez dans les exercices
  hebdomadaires.
- [Code Academy](https://www.codecademy.com/fr/learn/python)
- [newcoder.io](http://newcoder.io/). Des projets commentés, commencer par 'Data Visualization'
- [Google's Python Class](https://developers.google.com/edu/python/). Guido a travaillé chez eux.
  Pas [ce
  Guido](http://vignette2.wikia.nocookie.net/pixar/images/1/10/Guido.png/revision/latest?cb=20140314012724),
  [celui-là](https://en.wikipedia.org/wiki/Guido_van_Rossum#/media/File:Guido_van_Rossum_OSCON_2006.jpg)
- [Mooc Python](https://www.fun-mooc.fr/courses/inria/41001S03/session03/about#). Un mooc de
  l'INRIA, carré.
- [Code combat](https://codecombat.com/)

## Licence

Copyright © 2019 Loïc Grobol [\<loic.grobol@gmail.com\>](mailto:loic.grobol@gmail.com) et Yoann
Dupont [\<yoa.dupont@gmail.com\>](mailto:yoa.dupont@gmail.com)

Sauf indication contraire, les fichiers présents dans ce dépôt sont distribués selon les termes de
la licence [MIT](LICENSE)

Un résumé simplifié de cette licence est disponible à <https://tldrlegal.com/license/mit-license>.
