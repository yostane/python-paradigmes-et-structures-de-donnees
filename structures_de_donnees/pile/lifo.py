"""Implementation d'une pile LIFO avec une liste."""


# fonctions
def pile(*args):
    p = []
    if not args:
        return p
    for elem in args:
        p.append(elem)
    return list(p)


def empile(p, a):
    p.append(a)


def depile(p):
    try:
        return p.pop()
    except:
        print("La pile est vide !")


# programme principal
print(" Pile initiale ".center(50, '-'))
lifo = pile(5, 8, 9)
print("lifo:", lifo, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Empilage ".center(50, '-'))
empile(lifo, 11)
print("lifo:", lifo, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Depilages ".center(50, '-'))
for i in range(5):
    depile(lifo)
    print("lifo:", lifo)