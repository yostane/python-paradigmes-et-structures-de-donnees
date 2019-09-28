""" Les dictionnaires en Python (2/2)."""
dico = {"Au":
            {"Te/Tf":(2970, 1063),
             "N/Matomique":(79, 196.967)},
        "Ga":
            {"Te/Tf":(2237, 29.8),
             "N/Matomique":(31, 69.72)}}

print(dico["Au"],"\n")
print(dico["Ga"] ["Te/Tf"],"\n")
print("Numero atomique de l'or:", dico["Au"] ["N/Matomique"] [0],"\n")
print("Masse atomique de l'or:", dico["Au"] ["N/Matomique"] [1])