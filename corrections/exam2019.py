from collections import namedtuple
import re
from statistics import mean

# On va utiliser un tuple nommé pour représenter les enregistrements
# ce n'est pas strictement nécéssaire, on pourrait très bien s'en sortir
# avec juste des tuples par exemple mais ce sera plus lisible
DataRow = namedtuple(
    "DataRow", ("region", "number", "substance", "metric", "unit", "measures")
)


def parse_file(file_path):
    with open(file_path) as in_stream:
        # Ligne d'en-têtes
        # On pourrait s'en servir pour avoir une correspondance propre entre année et mesure mais
        # c'est supeflu ici
        headers = in_stream.readline().strip().split("\t")
        # Pour stocker les lignes de données
        records = []
        # On parcourt en gardant les numéros de ligne pour avoir des exceptions plus lisibles
        for i, row in enumerate(in_stream):
            cols = row.strip().split("\t")
            # Passer les lignes qui ne sont pas tabulaires (les métadonnées à la fin)
            if len(cols) == 1:
                continue
            # Pour les autres lignes le format est
            # "<REGION>\t<NUMÉRO>\tAI08<COMPOSÉ> - <RELEVÉ>\t<UNITÉ>\t<VALEURS>…"
            # On l'extrait proprement avec une affectation étendue
            # Notez l'opérateur « reste » (`*`) sur le dernier élément
            region, number, raw_substance, unit, *measures = cols
            #  Encore des lignes pièges !
            if region == "France entière":
                continue
            # On parse le nom de la substance, avec des groupes nommés !
            m = re.match(r"AI08(?P<substance>.*) - (?P<metric>.*)", raw_substance)
            # Si jamais ça ne marche pas c'est qu'il y a un souci avec la ligne
            if not m:
                raise ValueError(f"Incorrectly formatted row {i}: {row!r}")
            substance = m.group("substance")
            metric = m.group("metric")
            records.append(
                DataRow(
                    region,
                    number,
                    substance,
                    metric,
                    unit,
                    tuple(float(m) if m != "ND" else 0.0 for m in measures),
                )
            )
    # Convertir en tuple n'est pas nécéssaire mais c'est une sécurité : comme ça on est sûr⋅e⋅s de
    # ne jamais le modifier dans la suite
    return tuple(records)


def question1(records):
    """quantité d'ammoniac (en t/an) a été émise en Alsace en 2004"""
    # On code en dur l'indice de colonne de 2004
    col_2004 = 4
    for r in records:
        if (
            r.region == "ALSACE"
            and r.substance == "Ammoniac"
            and r.metric == "Quantités annuelles émises"
            and r.unit == "t/an"
        ):
            return r.measures[col_2004]
    # Si on arrive ici c'est qu'on a pas trouvé, on le signale bruyament
    raise ValueError("Not found")


def question2(records):
    """Combien de noms de régions mentionnées dans ce fichier comportent un nombre de
    lettres supérieur ou égal à 10 (espaces et tirets non compris) ?
    """
    # On déduplique les noms
    noms = set(r.region for r in records)
    # On les nettoie.
    # Attention, ceci est un **générateur**, le nettoyage effectif n'est pas fait ici mais quand on
    # itère dessus
    noms = (re.sub(r"\W", "", n) for n in noms)
    # Feinte du chacal pour compter les éléments d'un itérable qui vérifient une condition sans
    # prendre de place en mémoire
    res = sum(1 for n in noms if len(n) >= 10)
    return res


def max_emission(records, substance, range_key):
    """Renvoie l'enregistrement pour lequel les émissions pour une substance est
    maximale sur une période.
    """
    matching_records = (
        r
        for r in records
        if r.substance == substance and r.metric == "Quantités annuelles émises"
    )
    maximal = max(matching_records, key=range_key)
    return maximal


def question3(records):
    """Quelle est la région pour laquelle les émissions de monoxyde de carbone on été
    maximales en 2008 ?
    """
    # On récupère les lignes qui correspondent
    col_2008 = 8
    maximal = max_emission(
        records,
        substance="Monoxyde de carbone (CO)",
        range_key=lambda r: r.measures[col_2008],
    )
    return maximal.region


def question4(records):
    """Même question que 3., mais pour le total des émissions de monoxyde de carbone
    sur l'ensemble de la période 1999 — 2009
    """
    # On récupère les lignes qui correspondent
    maximal = max_emission(
        records,
        substance="Monoxyde de carbone (CO)",
        range_key=lambda r: sum(r.measures),
    )
    return maximal.region


def question5(records):
    """Donner le contenu de la précision donnée entre parenthèses la plus longue du
    fichier.
    """
    # NOTE: la consigne était ambigue et donnait deux possibilités de réponse finale: `"NOX y
    # compris NO2"` et `"et ses composants"`.
    noms = set(r.substance for r in records)
    max_len = 0
    res = None
    for n in noms:
        precisions = re.findall(r"\((.*?)\)", n)
        max_prec = max(precisions, key=len, default="")
        # En cas d'égalité on garde le max actuel
        if len(max_prec) > max_len:
            max_len = len(max_prec)
            res = max_prec
    return res


def question6(records):
    """Donner, sous forme de liste séparée par des barres `|` et triée par ordre
    alphabétique l'ensemble des noms de composés chimiques ou de catégories de
    composés mentionnés dans ce fichier.
    """
    # Cette fois-ci on commence par nettoyer
    noms = (re.sub(r"\(.*?\)\s?", "", r.substance).strip() for r in records)
    # puis mettre en minuscules
    noms = (n.lower() for n in noms)
    # dédupliquer
    noms = set(noms)
    #  trier
    noms = sorted(noms)
    return "|".join(noms)


def capitalize(nom):
    """Donne la capitalisation correcte pour un nom de région."""
    nom = nom.lower()
    # On split sur les non-mots, en les conservant
    fragments = re.split(r"(\W)", nom)
    cap_frag = []
    for f in fragments:
        if re.match(r"\W", f):
            cap_frag.append(f)
        # On saute les chaines vides
        elif f:
            cap_frag.append(f[0].upper())
            cap_frag.append(f[1:])
    return "".join(cap_frag)


def question7(records):
    """Donner, sous forme de liste séparée par des barres `|` et triée par ordre
    alphabétique l'ensemble des noms de régions présents dans ce fichier en
    capitalisant les débuts de mots
    """
    # On déduplique les noms
    noms = set(r.region for r in records)
    noms = (capitalize(n) for n in noms)
    noms = sorted(noms)
    return "|".join(noms)


def question8(records):
    """Quelle est le composé dont pour lequel la moyenne annuelle des émissions en
    région Basse Normandie a été la plus élevée sur la période 1999–2009 ?
    """
    records_bn = (
        r
        for r in records
        if r.region == "BASSE NORMANDIE" and r.metric == "Quantités annuelles émises"
    )
    max_r = max(
        records_bn, key=lambda r: mean(r.measures) * (1000 if r.unit == "t/an" else 1)
    )
    return max_r.substance


records = parse_file("AI08.txt")

print(question1(records))
print(question2(records))
print(question3(records))
print(question4(records))
print(question5(records))
print(question6(records))
print(question7(records))
print(question8(records))
