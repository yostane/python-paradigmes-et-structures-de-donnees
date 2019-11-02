import functools
l = [1, 2, 3, 4, 5, 6, 7]


def est_pair(x):
    return x % 2 == 0


liste_filtree = filter(lambda x: x > 5, l)
print(list(liste_filtree))

print(list(filter(lambda x: x > 5, l)))

print(list(filter(est_pair, l)))

res = filter(lambda x: x > 5, filter(est_pair, l))
print(list(res))

res = filter(lambda x: x > 5 and est_pair(x), l)
print(list(res))


def calculer_double(x):
    return x * 2


res = map(calculer_double, l)
print(list(res))

res1 = filter(lambda x: x > 5, l)
res2 = map(calculer_double, res1)
print(list(res2))
print(list(map(calculer_double, filter(lambda x: x > 5, l))))

res = [calculer_double(x) for x in l if x > 5]
print(res)
