"""Listes:methodes et indicage."""

nombres = [17, 38, 10, 25, 72]
print(" Liste initiale ".center(50, '-'))
print(nombres, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Tri ".center(50, '-'))
nombres.sort()
print(nombres, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Ajout d'un element ".center(50, '-'))
nombres.append(12)
print(nombres, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Retournement ".center(50, '-'))
nombres.reverse()
print(nombres, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Indice d'un element ".center(50, '-'))
print(nombres.index(17), '\n')

suite = input('Taper "Entree" pour la suite')

print(" Retrait d'un element ".center(50, '-'))
nombres.remove(38)
print(nombres, '\n')

suite = input('Taper "Entree" pour la suite')

print(" Indicage ".center(50, '-'))
print("> nombres[1:3] = ", nombres[1:3])
print("> nombres[:2] = ", nombres[:2])
print("> nombres[2:] = ", nombres[2:])
print("> nombres[:] = ", nombres[:])
print("> nombres[-1] = ", nombres[-1])