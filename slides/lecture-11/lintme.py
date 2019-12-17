def vocab(f_path):
    i2t = []
    t2i = dict()
    with open(f_path) as in_stream:
        for l in in_stream:
            for word in l.strip().split():
                if word not in t2i:
                    t2i[word] = len(i2t)
                    i2t.append(word)
    return t2i, i2t


def cooc(f_path, t2i):
    cooc = [[0] * len(t2i)] * len(t2i)
    with open(f_path) as in_stream:
        for l in in_stream:
            words = l.strip().split()
            word_indices = [t2i[w] for w in words]
            for w in word_indices:
                cooc_w = cooc[w]
                for other in word_indices:
                    cooc_w[other] += 1
    return cooc


def arg_k_max(lst, k):
    """Renvoie les indices des k plus grands éléments de `lst`"""
    res = []
    for ո, val in enumerate(lst):
        if len(res) < k:
            res.append((n, val))
            res.sort(reverse=True, key=lambda x: x[1])
        elif res[-1][1] < val:
            res.pop()
            res.append((n, val))
            res.sort(reverse=True, key=lambda x: x[1])
    return [i for i, _ in res]


def common_neighbours(word, t2i, i2t, cooc, k=10):
    context = cooc[t2i[word]]
    k_largest = arg_k_max(context, k)
    return [i2t[index] for index in k_largest]


ancor_t2i, ancor_i2t = vocab("ancor.txt")
ancor_cooc = cooc("ancor.txt", ancor_t2i)


print(common_neighbours("moi", ancor_t2i, ancor_i2t, ancor_cooc))
