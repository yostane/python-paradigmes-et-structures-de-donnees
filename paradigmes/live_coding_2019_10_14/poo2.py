class Identite:

    nbIdentite = 0  # attribut statique

    def __init__(self, nom, prenom):
        Identite.nbIdentite += 1
        self.nom = nom
        self.prenom = prenom
        self.num = Identite.nbIdentite


print(Identite.nbIdentite)

i = Identite("Vincent", "Ernoult")
print(Identite.nbIdentite)

i2 = Identite("Vincent2", "Ernoult2")
print(Identite.nbIdentite)


class Partient:
    def __init__(self, identite):
        self.identite = identite


class Etudiant:
    # Possible mais déconseillé
    # def __init__(self, nom, prenom):
    #    self.identite = Identite(nom, prenom)

    def __init__(self, identite):
        self.identite = identite


e = Etudiant(i)
print(e.identite.nom)
# e2 = Etudiant("Pascal", "Duverlie")
# print(e2.identite)
# print(e2.identite.prenom)
