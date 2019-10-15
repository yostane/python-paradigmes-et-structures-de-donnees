class Pokemon:
    pv = 0  # attribut
    nom = ""

    def __init__(self, points_de_vie):  # constructeur
        self.pv = points_de_vie
        print("hello")

    def __str__(self):
        return "Objet de la classe Pokemon. J'ai " + str(self.pv) + "PV"

    def crier(self):  # méthode "crier"
        print(self.nom, self.nom)

    def afficher_statut(self):
        print("Mes PV", self.pv)
        self.crier()


pikachu_de_vincent = Pokemon(100)
salameche_de_aurore = Pokemon(200)
pikachu_de_vincent.nom = "ERNOULD"
pikachu_de_vincent.pv = 50
pikachu_de_vincent.crier()
print(pikachu_de_vincent.pv)
pikachu_de_vincent.afficher_statut()
print(pikachu_de_vincent)
