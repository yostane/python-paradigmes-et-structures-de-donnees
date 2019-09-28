"""Listes:methodes et indicage."""

nombres = [17, 38, 10, 25, 72]
print("Listeinitiale".center(50,'-'))
print(nombres,'\n')

suite = input('"Entree"')

print("Tri".center(50,'-'))
nombres.sort()
print(nombres,'\n')

suite = input('"Entree"')

print("Ajout d'un element".center(50,'-'))
nombres.append(12)
print(nombres,'\n')

suite = input('"Entree"')

print("Retournement".center(50,'-'))
nombres.reverse()
print(nombres,'\n')

suite = input('"Entree"')

print("Indice d'un element".center(50,'-'))
print(nombres.index(17),'\n')

suite = input('"Entree"')

print("Retrait d'un element".center(50,'-'))
nombres.remove(38)
print(nombres,'\n')

suite = input('"Entree"')

print("Indicage".center(50,'-'))
print("nombres[1:3]=",nombres[1:3])
print("nombres[:2]=",nombres[:2])
print("nombres[2:]=",nombres[2:])
print("nombres[:]=",nombres[:])
print("nombres[-1]=",nombres[-1])