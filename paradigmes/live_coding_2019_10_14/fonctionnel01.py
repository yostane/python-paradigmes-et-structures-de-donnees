import random


def additionner(x, y):
    return x + y


def calculer(x, y, operation):
    resultat = operation(x, y)
    return resultat


f = additionner
print(0)
x = calculer(7, 1, additionner)
print(x)
print(calculer(7, 1, f))
print(calculer(5, 6, lambda x, y: x * y))
print(additionner(3, 4))
x = f(5, 10)
print(x)


# calcul de factorielle
num = 4
fact = 1
for i in range(num):
    fact = fact * (i + 1)

print(fact)


def calculer_factorielle(x):
    if x <= 1:
        return 1
    else:
        return x * calculer_factorielle(x - 1)


print(calculer_factorielle(4))

# Non pure
def generer_aleatoire(x):
    return random.randint(0, 10) + x


print(generer_aleatoire(4), generer_aleatoire(4), generer_aleatoire(4))
