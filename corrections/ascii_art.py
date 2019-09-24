# la version ici est réalisable avec la mise-à-niveau 1
l = int(input())  # la largeur de chaque lettre
h = int(input())  # la hauteur de l'affichage sur l'écran
t = input().upper()  # on met en majuscules
caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
char2ascii = {}
for i in range(h):  # pour chaque ligne d'affichage à l'écran...
    row = input()
    i = 0
    for carac in caracteres:  # char est une fonction built-in, il faut utiliser un autre nom
        if carac not in char2ascii.keys():  # la clé n'existe pas : on créé une liste vide
            char2ascii[carac] = []
        char2ascii[carac].append(row[i*l : (i+1)*l]) # on ajoute la sous-chaine qui représente le caractère
        i += 1
for i in range(h):  # pour chaque ligne d'affichage à l'écran...
    for letter in t:  # .. on va afficher le morceau de texte qui correspond à la lettre
        if letter in char2ascii.keys():
            print(char2ascii[letter][i], end="")
        else:
            print(char2ascii["?"][i], end="")
    print()


# la version ici est réalisable avec la mise-à-niveau 2
import collections

l = int(input())
h = int(input())
t = input().upper()  # on met en majuscules
caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
char2ascii = collections.defaultdict(list)
# un dictionnaire qui utilisera une liste vide par défaut si la clé n'existe pas.
for i in range(h):
    row = input()
    for i, carac in enumerate(caracteres):
        char2ascii[carac].append(row[i*l : (i+1)*l])
for i in range(h):
    for letter in t:
        print(char2ascii.get(letter, char2ascii["?"])[i], end="")
    print()
