# Exercices sur la programmation fonctionnelle

## Question 1

En partant d’une liste de n éléments (l=range(n)), on veut produire une nouvelle liste qui contient

1. e+1 pour tous les éléments e de la liste de départ ([0,1,2, ...]→[1,2,3, ...])
2. seulement les éléments pairs de la liste de départ ([0,1,2, ...]→[0,2,4, ...])
3. e+1 pour tous les éléments pairs e de la liste de départ ([0,1,2, ...]→[1,3,5, ...])

Pour chacun de ces cas, écrire

– Une version avec une boucle for
– Une version avec map et/ou filter
– Une version avec une list comprehension

## Question 2

Utilisant les compréhensions construire la liste des nombres premiers de 1 à 100.

## Question 3

Construire une fonction calculant la valeur en 0 d’une fonction d’entiers.

## Question 4

Construire une fonction prenant un prédicat sur les entiers et un ensemble d’entiers et
construisant l’ensemble des entiers de l’ensemble vérifiant ce prédicat.
Un prédicat sur les entier est une fonction des entiers vers les booléens.

## Question 5

Écrire une fonction qui filtre une liste d’URLs en ne gardant que les accessibles

1. en utilisant filter
2. avec une list comprehension

Exemple :

```python
urls = [
’https://www.he−arc.ch’,
’http://google.com’ ,
’www.he−arc’,
’http://www.cff.ch’,
’hh://inexistant’ ,
]
for u in checkurls(urls):
    print u
```

doit donner:

- https://www.he-arc.ch
- http://google.com
- http://www.cff.ch
