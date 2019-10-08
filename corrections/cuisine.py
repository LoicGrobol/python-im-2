from math import floor


class Pasta:
    def __init__(self, weight):
        self.weight = weight
        self.gluten = True
        self.max_guests = floor(self.weight / 100)

    def compatible_with(self, other):
        return True


class Tagliatelle(Pasta):
    _name = "Tagliatelle"


class Lasagne(Pasta):
    _name = "Lasagne"


class Pappardelle(Pasta):
    _name = "Pappardelle"


class Ingredient:
    pass


class Pesto(Ingredient):
    def addon(self, s):
        return f"{s} al pesto"


class Tartufo(Ingredient):
    def __init__(self, quantity):
        self.quantity = quantity

    def addon(self, s):
        return f"{s} con tartufo"


def cook(base, seasoning):
    return seasoning.addon(base._name)


pasta_types = [Lasagne, Tagliatelle, Pappardelle]
