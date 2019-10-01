import cuisine

assert len(dir(cuisine)) > 5

assert cuisine.pasta_types == [
    cuisine.Lasagne,
    cuisine.Tagliatelle,
    cuisine.Pappardelle,
]

for t in cuisine.pasta_types:
    assert issubclass(t, cuisine.Pasta)

main_ingredient = cuisine.Tagliatelle(200)
assert main_ingredient.max_guests <= 2
assert main_ingredient.gluten

salsa = cuisine.Pesto()
assert main_ingredient.compatible_with(salsa)

assert cuisine.cook(seasoning=salsa, base=main_ingredient) == "Tagliatelle al pesto"
assert (
    cuisine.cook(cuisine.Pappardelle(110), cuisine.Tartufo(0.5))
    == "Pappardelle con tartufo"
)

print("Test passé avec succès")
