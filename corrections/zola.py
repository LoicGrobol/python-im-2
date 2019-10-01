import re

from collections import Counter

with open("../data/zola_ventre-de-paris.txt") as in_stream:
    content = in_stream.read()

split = content.split()
print(f"Nombre de mots: {len(split)}")

counts = Counter(split)
plus_courants = ", ".join([repr(e[0]) for e in counts.most_common(10)])
print(f"Mots les plus courants: {plus_courants}")

with open("zola_ventre-de-paris_recollé.txt", "w") as out_stream:
    out = re.sub(r"¬\s+", "", content)
    out_stream.write(out)
