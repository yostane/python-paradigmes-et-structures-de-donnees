class Identite:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


i = Identite("Vincent", "Ernoult")


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
