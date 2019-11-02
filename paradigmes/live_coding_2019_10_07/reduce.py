import functools


def calculer_double(x):
    return x * 2


l = [5, 2, 3, 4, 5, 6, 7]
res = [calculer_double(x) for x in l if x > 5]
print(res)


somme = functools.reduce(lambda x, y: x + y, res, 0)
print(somme)

produit = functools.reduce(lambda x, y: x + y, l)
print(produit)
