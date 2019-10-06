## Arbre : Travaux pratiques

### Exercices

Pour construire un arbre binaire sous Python, on peut utiliser les listes ou autres structures de données.
Dans ce TP, nous faisons le choix d'utiliser les listes pour créer et gérer un arbre binaire.
* la liste sera sous la forme : [Donnée, sous-arbre gauche, sous-arbre droit]
* Une feuille est l'élément d'un arbre dont les sous-arbres gauche et droit égalent None

Soit l'arbre binaire suivant:
    arb = [15, [7, [6, [None], [None]], [9, [None], [None]]], [20, [None], [25, [None], [None]]]]

                     15
                     / \
                   7     20
                  / \      \
                 6   9      25

Soient les fonctions utilitaires suivantes :

* arbre_binaire(r)  : construit un arbre sous forme de liste qui contient un noeud racine avec 2 sous-arbres vides (valeur à None)

        def arbre_binaire(r):
            return [r, [None], [None]]

* change_racine(arbre, valeur) : change la valeur du noeud racine en la remplaçant par l'élément correspondant au paramètre "valeur"

        def change_racine(arbre, valeur):
            arbre[0] = valeur
            return arbre

* valeur_racine(arbre) : affiche la valeur de la racine

        def valeur_racine(arbre):
            return arbre[0]

* sous_arbre_gauche(arbre) : retourne le sous-arbre gauche d'un arbre passé en paramètre

        def sous_arbre_gauche(arbre):
            return arbre[1]

* sous_arbre_droit(arbre) :  retourne le sous-arbre droit d'un arbre passé en paramètre

        def sous_arbre_droit(arbre):
            return arbre[2]

1. Complétez la liste des fonctions utilitaires en implémentant les fonctions suivantes:

    a. 'ajouter_sous_arbre_gauche(arbre, sous_arbre)' : ajoute le sous-arbre gauche, 'sous-arbre', à l'arbre passé en paramètre

    b. 'ajouter_sous_arbre_droit(arbre, sous_arbre)' :  ajoute le sous-arbre droit, 'sous-arbre', à l'arbre passé en paramètre

2. Implémentez différentes formes de parcours

    a. Implémentez une fonction 'prefixe' qui affiche les éléments d'un arbre en parcours préfixe (NGD)

    b. Implémentez une fonction 'infixe' qui affiche les éléments d'un arbre en parcours infixe (GND)

    Conseil : utilisez la récursivité

3. Valider votre implémentation par un programme principal qui utilise l'arbre défini en début d'énoncé
