""" Les dictionnaires en Python (2/2)."""
dico = {"Au":
            {"Te/Tf": (2970, 1063),
             "Z/A": (79, 196.967)},
        "Ga":
            {"Te/Tf": (2237, 29.8),
             "Z/A": (31, 69.72)}}

print("> Propriétés de l'or : ", dico["Au"], "\n")
print("> Température ébulition & fusion du Gallium : ", dico["Ga"]["Te/Tf"], "\n")
print("> Numero atomique de l'or:", dico["Au"]["Z/A"][0], "\n")
print("> Masse atomique de l'or:", dico["Au"]["Z/A"][1])