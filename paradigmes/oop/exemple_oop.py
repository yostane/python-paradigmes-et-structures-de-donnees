class Personnage:

    hp = 100
    attaque = 10
    niveau = 1

    def augmenterNiveau(self):
        self.niveau += 1
        self.attaque += 1
        self.hp += 10
    
    def donnerStatut(self):
        print("HP", self.hp, "Attaque", self.attaque)

class Monstre(Personnage):
    hp = 30

    def augmenterNiveau(self):
        self.niveau += 1
        self.attaque += 2
        self.hp += 5

class Hero(Personnage):
    hp = 500
    attaque = 5

class Assistant(Personnage):
    hp = 1000
    attaque = 5
    nom = ""

    def __init__(self, nom):
        self.nom = nom

    def donnerStatut(self):
        super().donnerStatut()
        print("nom", self.nom)

m = Monstre()
m.donnerStatut()
m.augmenterNiveau()
m.donnerStatut()
h = Hero()
h.donnerStatut()
h.augmenterNiveau()
h.donnerStatut()

a = Assistant("Toto")
a.donnerStatut()