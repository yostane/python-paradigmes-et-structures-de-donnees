"""Arbre binaire - Application"""


# Fonctions utilitaires

# fonction 'arbre_binaire(r)'  : construit un arbre sous forme de liste qui contient un noeud racine avec 2 sous-arbres vides (valeur à None)
def arbre_binaire(r):
    return [r, [None], [None]]


# fonction 'change_racine(arbre, valeur)' : change la valeur du noeud racine en la remplaçant par l'élément correspondant au paramètre "valeur"
def change_racine(arbre, valeur):
    arbre[0] = valeur
    return arbre


# fonction 'valeur_racine(arbre)' : affiche la valeur de la racine
def valeur_racine(arbre):
    return arbre[0]


# fonction 'sous_arbre_gauche(arbre)' : retourne le sous-arbre gauche d'un arbre passé en paramètre
def sous_arbre_gauche(arbre):
    return arbre[1]


# fonction 'sous_arbre_droit(arbre)': retourne le sous-arbre droit d'un arbre passé en paramètre
def sous_arbre_droit(arbre):
    return arbre[2]


# fonction 'ajouter_sous_arbre_gauche(arbre)' : ajoute le sous-arbre gauche d'un arbre passé en paramètre
def ajouter_sous_arbre_gauche(arbre, sous_arbre):
    arbre[1] = sous_arbre
    return arbre


# fonction 'ajouter_sous_arbre_droit(arbre)': ajoute le sous-arbre droit d'un arbre passé en paramètre
def ajouter_sous_arbre_droit(arbre, sous_arbre):
    arbre[2] = sous_arbre
    return arbre


# fonction 'prefixe' qui affiche les éléments d'un arbre en parcours préfixe (NGD)
def prefixe(arbre):
    if valeur_racine(arbre) is None:
        print(end='')
    else:
        print([valeur_racine(arbre)], end=' ')
        prefixe(sous_arbre_gauche(arbre))
        prefixe(sous_arbre_droit(arbre))


# fonction 'infixe' qui affiche les éléments d'un arbre en parcours infixe (GND)
def infixe(arbre):
    if valeur_racine(arbre) is None:
        print(end='')
    else:
        infixe(sous_arbre_gauche(arbre))
        print([valeur_racine(arbre)], end=' ')
        infixe(sous_arbre_droit(arbre))


# programme principal

arbre = [15, [7, [6, [None], [None]], [9, [None], [None]]], [20, [None], [25, [None], [None]]]]

prefixe(arbre)

input('\n\nTapez "Entree" pour la suite\n')

infixe(arbre)
