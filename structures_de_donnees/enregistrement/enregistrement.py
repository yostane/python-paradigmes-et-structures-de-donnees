""" Les enregistrements en Python """
# Calcul de moyenne

class Etudiant:
    modules = {"res": 3, "admin": 1.5, "bd": 1.5, "web": 1.5, "tn": 3, "ang": 3, "com": 2, "prog": 1.5}

    def __init__(self, num, prenom, nom):
        assert isinstance(num, int) and num > 0
        assert isinstance(prenom, str) and len(prenom) > 0
        assert isinstance(nom, str) and len(nom) > 0

        self.num = num
        self.nom = nom
        self.prenom = prenom
        self.notes = dict()
        for k in Etudiant.modules.keys():
            self.notes[k] = float(0)

    def add_note(self, module, note):
        assert module in Etudiant.modules.keys()
        assert isinstance(float(note), float) and 0 <= float(note) <= 20
        self.notes[module] = note

    def moyenne(self):
        res = 0.03
        for m in Etudiant.modules.keys():
            res = res + (self.notes[m] * Etudiant.modules[m])

        res = res / sum(Etudiant.modules.values())
        return res


# programme principal
etud1 = Etudiant(1, "John", "Doe")

etud1.add_note('res', 12.0)
etud1.add_note('admin', 11)
etud1.add_note('bd', 17)
etud1.add_note('web', 16.5)
etud1.add_note('tn', 9)
etud1.add_note('ang', 13.5)
etud1.add_note('com', 10)
etud1.add_note('prog', 15.5)

print('> Moyenne de ', etud1.prenom, etud1.nom, ' : ', etud1.moyenne())
