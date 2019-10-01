# Créer un classe représentant les nombres rationnels

class Rationnel:
    reel = 0
    imaginaire = 0

    def __init__(self, reel, imaginaire):
        self.reel = reel
        self.imaginaire = imaginaire

    def additionner(self, rationnel):
        r = Rationnel(reel + rationnel.reel, self.imaginaire + rationnel.imaginaire)
        return r

    