import sys
import math

# On pourrait faire joujou avec `ord` et `char` mais c'est pas le but
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_indices(s):
    return {l: i for i, l in enumerate(s)}


alphabet_indices = get_indices(alphabet)


def shift(n, s, encode=True):
    out = []
    for i, l in enumerate(s):
        if encode:
            shifted_indice = (alphabet_indices[l] + i + n) % len(alphabet)
        else:
            shifted_indice = (alphabet_indices[l] - i - n) % len(alphabet)
        shifted = alphabet[shifted_indice]
        out.append(shifted)
    return "".join(out)


def apply_rotor(rotor, s, encode=True):
    rotor_indices = get_indices(rotor)
    if encode:
        table = str.maketrans(alphabet, rotor)
    else:
        table = str.maketrans(rotor, alphabet)
    return s.translate(table)


operation = input()
pseudo_random_number = int(input())

rotors = []
for i in range(3):
    rotors.append(input().strip())
message = input()


# Note: on pourrait faire plus propre avec des fonctions partielles
if operation == "DECODE":
    rotors.reverse()
else:
    message = shift(pseudo_random_number, message)

for r in rotors:
    message = apply_rotor(r, message, operation == "ENCODE")

if operation == "DECODE":
    message = shift(pseudo_random_number, message, False)

print(message)

