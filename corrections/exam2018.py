# Reading the data
noms = dict()
with open("noms2008nat_txt.txt") as in_stream:
    # On gère la colonne d'en-tête à part
    years = next(in_stream).strip().split("\t")[1:]
    for line in in_stream:
        n, *y = line.strip().split("\t")
        if n == "AUTRES NOMS":
            continue
        noms[n] = list(map(int, y))

# 1.
most_pop = max(noms, key=lambda x: noms[x][-1])

print(most_pop)

# 2.
# 2.1
biggest_delta = max(noms, key=lambda x: noms[x][-1] - noms[x][-2])

print(biggest_delta)

# 2.2
biggest_lambda = max(
    (n for n in noms if noms[n][-2] != 0),
    key=lambda n: (noms[n][-1] - noms[n][-2]) / (noms[n][-2]),
)

print(biggest_lambda)

# 3
print(sum(1 for n in noms if " " in n or "-" in n))

# 4
print(sum(1 for n in noms if n[0] == n[-1]))

# Pour la suite on va construire une liste de noms pour chaque département
# La structure est {département: {nom: [naissances]}}
deps = dict()
# Reading the data
with open("noms2008dep_txt.txt") as in_stream:
    years = next(in_stream).strip().split("\t")[2:]
    for line in in_stream:
        n, d, *y = line.strip().split("\t")
        if n == "AUTRES NOMS" or d == "XX":
            continue
        # On aurait aussi pu utiliser un defaultdict mais c'est plus propre
        # comme ça
        deps.setdefault(d, dict())[n] = [int(i) for i in y]

# 1.1
breizh_deps = ["22", "29", "35", "56"]
breizh_names = {}
for d in breizh_deps:
    for n, y in deps[d].items():
        v = breizh_names.get(n, 0)
        breizh_names[n] = v + y[-1]

most_pop = max(breizh_names, key=lambda x: breizh_names[x])

print(most_pop)

# 1.2
france_names = {}
for d in (d for d in deps if d not in breizh_deps):
    for n, y in deps[d].items():
        v = france_names.get(n, 0)
        france_names[n] = v + y[-1]

most_pop = max(france_names, key=lambda x: france_names[x])

print(most_pop)

# 2.
most_names = max(deps, key=lambda x: len(deps[x]))
print(most_names)

# 3.
# Reading the data, taking `"AUTRES NOMS"` into account
deps = {}
with open("noms2008dep_txt.txt") as in_stream:
    years = next(in_stream).strip().split("\t")[2:]
    for line in in_stream:
        n, d, *y = line.strip().split("\t")
        if d == "XX":
            continue
        deps.setdefault(d, dict())[n] = list(map(int, y))

total_birth = {d: sum(y[-1] for y in v.values()) for d, v in deps.items()}

max_birth = max(total_birth, key=lambda x: total_birth[x])
print(max_birth)
