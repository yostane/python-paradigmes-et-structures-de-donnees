## Dictionnaire : Travaux pratiques

1. Écrire une fonction 'compter_mots' ayant un argument, une chaîne de caractères, et qui renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.

2. Le type dictionnaire (ou tableau associatif) permet de représenter des tableaux structurés. En effet, à chaque clé un dictionnaire associe une valeur, et cette valeur peut elle-même être une structure de donnée (liste, tuple ou un dictionnaire...).

  Soit le tableau suivant représentant des informations physico-chimiques sur des éléments simples (température d’ébullition (Te) et de fusion (Tf), numéro (Z) et masse(M) atomique :
  --------------------------------
  |    | Te/Tf | 2970 |  1063    |
  | Au |--------------------------
  |    | Z/A   |  79  |  196.967 |
  --------------------------------
  |    | Te/Tf | 2237 |  29.8    |
  | Ga |--------------------------
  |    | Z/A   |  31  |  69.72   |
  --------------------------------

  Affectez les données de ce tableau à un dictionnaire 'dico' python de façon à pouvoir écrire par exemple :

  ```bash
  >>> print dico["Au"]["Z/A"][0] # affiche:79
  ```