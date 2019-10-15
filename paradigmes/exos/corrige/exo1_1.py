l = range(10)

l1_for = []  # e+1
l2_for = []  # les éléments pairs
l3_for = []  # e+1 si e est pair
for i in l:
    l1_for.append(i + 1)

    if i % 2 == 0:
        l2_for.append(i)
        l3_for.append(i + 1)


# on peut définir de façon consice les fonctions qui return une seule ligne de code
def ajotuer_un(x):
    return x + 1


def est_pair(x):
    return x % 2 == 0


l1_map_filter = map(ajotuer_un, l)
l1_comp = [ajotuer_un(x) for x in l]
l2_map_filter = filter(est_pair, l)
l2_comp = [x for x in l if est_pair(x)]
l3_map_filter = map(ajotuer_un, filter(est_pair, l))
l3_comp = [ajotuer_un(x) for x in l if est_pair(x)]
l4_comp = [x + 1 if x % 2 == 0 else x for x in l]  # +1 si pair sinon la valeur initiale

print(l1_for, list(l1_map_filter), l1_comp)
print(l2_for, list(l2_map_filter), l2_comp)
print(l3_for, list(l3_map_filter), l3_comp)
print(l4_comp)
