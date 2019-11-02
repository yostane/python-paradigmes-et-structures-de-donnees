## Dictionnaire : Travaux pratiques

### Exercices

1. Écrire une fonction 'compter_mots' ayant en paramètre une chaîne de caractères, et qui renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.

2. Le type dictionnaire (ou tableau associatif) permet de représenter des tableaux structurés. En effet, à chaque clé un dictionnaire associe une valeur, et cette valeur peut elle-même être une structure de donnée (liste, tuple ou un dictionnaire...).

  Soit le tableau suivant représentant des informations physico-chimiques sur des éléments simples (température d’ébullition (Te) et de fusion (Tf), numéro (Z) et masse(M) atomique :
  
  ```bash
  --------------------------------
  |    | Te/Tf | 2970 |  1063    |
  | Au |--------------------------
  |    | Z/M   |  79  |  196.967 |
  --------------------------------
  |    | Te/Tf | 2237 |  29.8    |
  | Ga |--------------------------
  |    | Z/M   |  31  |  69.72   |
  --------------------------------
  ```
  
  Affectez les données de ce tableau à un dictionnaire 'dico' python de façon à pouvoir écrire par exemple :

  ```bash
  >>> print dico["Au"]["Z/A"][0] # affiche:79
  ```
  
### Liens

* [Tutorial sur les dictionnaires en Python](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)