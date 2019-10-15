l = [1, 2, 3, 4, 5, 6, 7]


def est_pair(x):  # retourne true si x est pair
    return x % 2 == 0


liste_filtree = filter(est_pair, l)
print(list(liste_filtree))  # je dois repréciser que c une liste
print(list(filter(lambda y: y >= 5, l)))
print(list(map(lambda x: x * 2, l)))  # le double de chaque élément

liste_resultat = map(lambda x: x * 2, filter(est_pair, filter(lambda x: x >= 5, l)))
liste_resultat = map(lambda x: x * 2, filter(lambda x: x >= 5 and x % 2 == 0, l))
print(list(liste_resultat))  # le double des éléments >= 5
liste_resultat = [x * 2 for x in l if x >= 5 and x % 2 == 0]  # compréhension de liste
print(liste_resultat)

pokemons = ["pikachu", "salameche", "rondoudou"]
resultat = map(lambda mot: len(mot), pokemons)
print(list(resultat))  # on peut trasformer vers un autre type avec map
print([len(x) for x in pokemons])

import functools

total = functools.reduce(lambda x, y: x + y, l, 0)
print(total)

print(functools.reduce(lambda x, y: x * y, l, 1))
y
