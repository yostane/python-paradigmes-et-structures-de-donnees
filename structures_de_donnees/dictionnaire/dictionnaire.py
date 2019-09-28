"""Les dictionnaires en Python. Extraire les mots d'un texte, et leur frequence."""
# fonction
def compter_mots(texte):
    dict = {}
    liste_mots = texte.split()
    for mot in liste_mots:
        if mot in dict:
            dict[mot] = dict[mot] + 1
        else:
            dict[mot] = 1
    return dict

res = compte_mots("Ala Met Asn Glu Met Cys Asn Glu Hou Ala Met Gli Asn Asn")
for c in res.keys():
    print(c,"-->",res[c])
