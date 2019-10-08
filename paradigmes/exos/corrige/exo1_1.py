l = range(10)

l1_for = []
l2_for = []
l3_for = []
for i in l:
    l1_for.append(i + 1)
    l2_for.append(i * 2)
    if i % 2 == 0:
        l3_for.append(i + 1)


# on peut définir de façon consice les fonctions qui return une seule ligne de code
def ajotuer_un(x):
    return x + 1


def doubler(x):
    return x * 2


def est_pair(x):
    return x % 2 == 0


l1_map_filter = list(map(ajotuer_un, l))
l2_map_filter = list(map(doubler, l))
l3_map_filter = list(map(ajotuer_un, filter(est_pair, l)))

print(l1_for, l1_map_filter)
print(l2_for, l2_map_filter)
print(l3_for, l3_map_filter)
