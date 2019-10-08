
def additionner(x, y):
    return x + y


def calculer(x, y, operation):
    resultat = operation(x, y)
    return resultat


f = additionner
print(additionner(2, 4))
print(f(4, 5))
print(calculer(1, 3, f))
print(calculer(1, 3, additionner))
print(calculer(1, 3, lambda toto, tutu: toto * tutu))

# calcul de factorielle
num = 4
fact = 1
for i in range(num):
    fact = fact * (i + 1)

print("factorielle", fact)

# si x est négatif, la factorielle est égale à 0


def calculer_factorielle(x):
    if x < 0:
        return 0

    if x <= 1:
        return 1
    else:
        return x * calculer_factorielle(x - 1)


print(calculer_factorielle(4))
