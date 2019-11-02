""" Matrice adjacente et graphe non-orienté """

A = [[0, 0, 1, 0, 1],
     [0, 0, 1, 0, 1],
     [1, 1, 0, 1, 1],
     [0, 0, 1, 0, 0],
     [1, 1, 1, 0, 0]]


def arete(matrice, s1, s2):
    if matrice[s1][s2] == 1:
        return True
    else:
        return False


def voisins(matrice, sommet):
    print("\nSommet ", sommet, " a comme voisin : ")
    s = 0
    while s < len(matrice):
        if arete(matrice, s, sommet):
            print("s", s)
        s = s + 1

# Programme principal

print('> Arete entre sommets S0 et S2 ? ', arete(A, 0, 2))
print('> Arete entre sommets S2 et S0 ? ', arete(A, 2, 0))

print('> Arete entre sommets S1 et S3 ? ', arete(A, 1, 3))
print('> Arete entre sommets S3 et S1 ? ', arete(A, 3, 1))

s = 0
while s < 5:
    voisins(A, s)
    s = s + 1