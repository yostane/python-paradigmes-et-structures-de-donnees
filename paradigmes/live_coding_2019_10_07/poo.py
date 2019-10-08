
class Pokemon:
    # propriété
    # variable d'instance
    # attribut (moins utilisé)
    pv = 0
    _nom = ""

    # constructeur
    def __init__(self, points_de_vie, nom):
        self.pv = points_de_vie
        self._nom = nom

    # permet de définir l'affichage dans un print
    def __str__(self):
        return "Pokemon pv = " + str(self.pv)

    def get_nom(self):
        return self._nom

    # méthode de la classe
    def crier(self):
        print("POKEMOOOON. J'ai ", self.pv, " PV")


pikachu_de_catherine = Pokemon(100, "pika")
# pikachu_de_catherine.pv = 100
pikachu_de_catherine.crier()
print(pikachu_de_catherine)
pikachu_de_martine = Pokemon(25, "salameche")
# pikachu_de_martine.pv = 25
pikachu_de_martine.crier()
print(pikachu_de_martine.get_nom())
