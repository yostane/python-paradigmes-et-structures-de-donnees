class Vehicule:
    annee_production = 0

    def demarrer(self):
        print("VROOM")


class Voiture(Vehicule):  # voiture hérite de véhicule
    couleur = ""


clio_de_sophie = Voiture()
clio_de_sophie.annee_production = 2000
clio_de_sophie.demarrer()
clio_de_sophie.couleur = "Bleu"
