## Graphe : Travaux pratiques

### Exercice - Matrice d'adjacence pour un graphe non-orienté

1. Déclarer une variable A qui remplit la matrice d'adjacence avec le graphe non-orienté suivant :
   
   ```bash
                                  s0               s4
                                     _____________
                                     \          / \
                                      \        /   \
                                       \      /     \
                                        \    /       \
                                         \  /         \
                                       s2 \/___________\ s1
                                         /
                                        /
                                       /
                                      /
                                    s3
     ```
     
2. Ecrire une fonction 'arete(matrice, s1, s2)' qui retourne 'True' s'il y a une arête entre les sommets s1 et s2, et 'False' sinon.

3. Tester votre fonction en l’appelant pour quelques combinaisons de sommets

4. Ecrire une fonction 'voisins(matrice, sommet)' qui affiche les voisins du sommet numéro sommet du graphe représenté par la matrice d’adjacence 'matrice'
   Exemple : "Sommmet s0 a comme voisin : s2 s4"

5. Tester votre fonction en l'appelant pour chaque sommet du graphe.

### Liens

* [Liste imbriquée en Python](https://docs.python.org/fr/3/tutorial/datastructures.html?highlight=matrice#nested-list-comprehensions)
* [Matrice d'adjacence - Wikipedia](https://fr.wikipedia.org/wiki/Matrice_d%27adjacence)