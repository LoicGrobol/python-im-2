# -*- coding: utf-8 -*-

"""
Helps parsing a conllu file into sentences and words
See http://universaldependencies.org/format.html 
"""


class Word:
    """
    A word (i.e. a line of a conll file) with its features
    """

    def __init__(
        self,
        nid="_",
        form="_",
        lemma="_",
        upos="_",
        xpos="_",
        feats="_",
        head="_",
        dep_rel="_",
        deps="_",
        misc="_",
    ):
        self.nid = nid
        self.form = form
        self.lemma = lemma
        self.upos = upos
        self.xpos = xpos
        self.feats = feats
        self.head = head
        self.dep_rel = dep_rel
        self.deps = deps
        self.misc = misc

    def __str__(self):
        text = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            self.nid,
            self.form,
            self.lemma,
            self.upos,
            self.xpos,
            self.feats,
            self.head,
            self.dep_rel,
            self.deps,
            self.misc,
        )
        return text


class Sentence:
    """
    A sentence is composed of a list of Word objects and a list of comments (str)
    """

    def __init__(self):
        self.words = []
        self.sent_id = ""
        self.text = ""

    def __str__(self):
        lines = ""
        lines += "# sent_id = "
        lines += self.sent_id + "\n"
        lines += "# text = "
        lines += self.text + "\n"
        for word in self.words:
            lines += str(word)
            lines += "\n"
        return lines

    def add_word(self, line):
        """
        Add a Word to the words list
        Args:
            line (str): a line of an orfeo file with a word informations
        """
        pass  # TODO: remplacer par du vrai code !


def parse_file(filename):
    """
    Turns a file into a list of sentences
    Args: 
        filename (str): the file path
    Return:
        list of dicts (sents) of tuples (words)
    """
    pass # TODO: remplacer par du vrai code !


def number_of_tokens(sentences, category=None):
    """
    Count the number of words in sentences
    If category is given, only count words of this category, otherwise count all
    Args:
        sentences (list) : the list of Sentence objects
        category (str, default None) : the category to count
    Return:
        the count of words in sentences of category
    """
    pass # TODO: remplacer par du vrai code !


def ments_not_adv(sentences):
    """
    Count the number of words in sentences that end with "ment" but are not ADV
    Args:
        sentences (list) : the list of Sentence objects
    Return:
        the list of words
    """
    pass # TODO: remplacer par du vrai code !


sentences = parse_file('fr_gsd-ud-test.conllu')
assert len(sentences) == 416
assert number_of_tokens(sentences) == 10300
pos = input(f"\n\nLes tokens de quel POS voulez-vous compter ? ")
nb_tokens = number_of_tokens(sentences, pos)
print(f"Le fichier contient {nb_tokens} tokens annotés {pos}.")
assert number_of_tokens(sentences, "NOUN") == 1852
ments = ments_not_adv(sentences)
assert len(ments) == 54
# affichez les -ments non ADV triés par forme et par fonction
