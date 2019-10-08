class Vehicule:
    annee_production = 0

    # définition d'un constcteur qui initialise l'année de production
    def __init__(self, annee_production):
        self.annee_production = annee_production

    def demarrer(self):
        print("VROOM VROOM")

    def arreter(self):
        print("STOP")

    def klaxonner(self):
        print("POUET")


class Voiture(Vehicule):  # Voiture hérite de Véhicule
    _couleur = ""
    _modele = ""
    # snake case
    _type_carburant = ""

    def __init__(self, annee_production, couleur, modele, type_carburant):
        super().__init__(annee_production)
        self._couleur = couleur
        self._type_carburant = type_carburant
        self._modele = modele

    # redéfinition (ou spécialisation) de klaxonner pour la Voiture)
    def klaxonner(self):
        print("POUET POUET")


class Camion(Vehicule):  # Voiture hérite de Véhicule
    # redéfinition (ou spécialisation) de klaxonner pour le camio
    def klaxonner(self):
        print("BROOM POUET")


voiture_yassine = Voiture(2018, "vert", "206", "SP95")
print(voiture_yassine)
voiture_yassine.klaxonner()

camion = Camion(2000)
camion.klaxonner()
