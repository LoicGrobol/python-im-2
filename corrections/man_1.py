def la_plus_grande(longueur1, longueur2, longueur3):
    """Renvoie la plus grande longueur."""
    # cette fonction existe déjà en python, pensez à lire la doc,
    # il n'y a pas toujours besoin de recréer la roue !
    return max(longueur1, longueur2, longueur3)

def est_equilateral(longueur1, longueur2, longueur3):
    """Renvoie si un triangle est équilatéral."""
    return longueur1 == longueur2 and longueur2 == longueur3
    # ou, comme python le permet:
    # return longueur1 == longueur2 == longueur3

def est_isocele(longueur1, longueur2, longueur3):
    """Renvoie si un triangle est isocele."""
    deux_egales = longueur1 == longueur2 or longueur1 == longueur3 or longueur2 == longueur3
    return deux_egales and not est_equilateral(longueur1, longueur2, longueur3)
    # ou sinon :
    # utiliser des parenthèses ici permet d'écrire sur plusieurs lignes,
    # c'est très utile quand on doit écrire une instruction assez longue.
    # return (
    #    (longueur1 == longueur2 or longueur1 == longueur3 or longueur2 == longueur3)
    #    and not est_equilateral(longueur1, longueur2, longueur3)
    #)

def est_triangle(longueur1, longueur2, longueur3):
    """Renvoie si les longueurs données font bien un triangle."""
    maxi = la_plus_grande(longueur1, longueur2, longueur3)
    somme = longueur1 + longueur2 + longueur3
    return maxi <= (somme - maxi)  # la somme des deux côtés est au plus maxi

def caracteristiques(longueur1, longueur2, longueur3):
    """Affiche les caractéristiques d'un triangle.
    Les caractéristiques d'un triangle sont :
        - sa nature
        - la taille de son plus grand côté.

    On dira qu'un triangle est `quelconque` s'il n'est ni équilatéral ni isocèle.

    Affiche `pas un triangle` si les longueurs données ne font pas un triangle
    (la longueur du plus grand côté est supérieure à celle des deux autres).
    """
    if not est_triangle(longueur1, longueur2, longueur3):
        print("pas un triangle")
    else:
        maxi = la_plus_grande(longueur1, longueur2, longueur3)
        if est_equilateral(longueur1, longueur2, longueur3):
            print("equilatéral", end=" ")
        elif est_isocele(longueur1, longueur2, longueur3):
            print("isocèle", end=" ")
        else:
            print("quelconque", end=" ")
        print(maxi)


print("-" * 64)
print(" triangles")
print("-" * 64)
caracteristiques(1, 1, 1) # equilatéral 1
caracteristiques(1, 1, 2) # isocèle 2
caracteristiques(1, 2, 1) # isocèle 2
caracteristiques(2, 1, 1) # isocèle 2
caracteristiques(2, 3, 1) # quelconque 3
caracteristiques(2, 3, 6) # pas un triangle
caracteristiques(6, 3, 2) # pas un triangle
caracteristiques(2, 6, 3) # pas un triangle


def heures(secondes):
    """Prend un nombre de secondes (entier) et le convertit en heures, minutes
    et secondes sous le format `H:M:S` où `H` est le nombre d'heures,
    `M` le nombre de minutes et `S` le nombre de secondes.

    On suppose que secondes est positif ou nul (secondes >= 0).
    """
    H = secondes // 3600
    M = (secondes % 3600) // 60
    S = secondes % 60
    return f"{H}:{M}:{S}"

def secondes(heure):
    """Prend une heure au format `H:M:S` et renvoie le nombre de secondes
    correspondantes (entier).

    On suppose que l'heure est bien formattée. On aura toujours un nombre
    d'heures valide, un nombre de minutes valide et un nombre de secondes valide.
    """
    H, M, S = heure.split(":")
    return (3600 * int(H)) + (60 * int(M)) + int(S)


print()
print("-" * 64)
print(" heures")
print("-" * 64)
print(heures(0)) # 0:0:0
print(heures(30)) # 0:0:30
print(heures(60)) # 0:1:0
print(heures(66)) # 0:1:6
print(heures(3600)) # 1:0:0
print(heures(86466)) # 24:1:6
print(secondes('0:0:0')) # 0
print(secondes('6:6:6')) # 21966
print(secondes(heures(86466))) # 86466
print(heures(secondes('24:1:1'))) # 24:1:1


def gagne_couleur(carte1, carte2, carte3, carte4):
    """Affiche la carte qui remporte le pli en faisant attention aux couleurs :
        - la carte du premier joueur `carte1` donne la couleur attendue.
        - une carte qui n'est pas à la bonne couleur perd automatiquement.

    On ne gèrera pas certains cas incohérents comme une carte ou un pli invalide.
    """
    def gagne(carte1, carte2, couleur):  # on peut aussi définir une fonction dans une fonction
        if carte2[0] != couleur:
            return carte1
        elif int(carte1[1:]) < int(carte2[1:]):  # carte1 est forcément valide, pas besoin de vérifier
            return carte2
        else:
            return carte1
    couleur = carte1[0]
    gagnante = carte1
    for carte in [carte2, carte3, carte4]:
        gagnante = gagne(gagnante, carte, couleur)
    print(gagnante)


print()
print("-" * 64)
print(" cartes")
print("-" * 64)
gagne_couleur('S1', 'S2', 'S3', 'S4') # S4
gagne_couleur('S4', 'S3', 'S2', 'S1') # S4
gagne_couleur('S1', 'D2', 'C3', 'H4') # S1
gagne_couleur('S1', 'D2', 'S13', 'S10') # S13
