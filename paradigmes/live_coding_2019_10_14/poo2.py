class Identite:
    def __init__(self, nom, prenom):
        self.nom = ""
        self.prenom = ""


i = Identite("Vincent", "Ernoult")


class Partient:
    def __init__(self, identite):
        self.identite = identite


class Etudiant:
    def __init__(self, nom, prenom):
        self.identite = Identite(nom, prenom)

    def __init__(self, identite):
        self.identite = identite


e = Etudiant(i)
e2 = Etudiant("Pascal", "Duverlie")
print(e.identite.nom)
