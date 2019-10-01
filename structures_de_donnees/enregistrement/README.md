## Enregistrement : Travaux pratiques

### Calcul de moyenne

On considère le cas d’une groupe d’étudiants qui suivent une formation en réseaux et télécommunications.
Le tableau 1 donne les coefficients appliqués pour chaque module.
________________________________________________
| Module                  | code  | coefficient |
|_______________________________________________|
| Réseau                  | res   | 3           |
| Adminsitration système  | admin | 1.5         |
| Base de données         | bd    | 1.5         |
| Web                     | web   | 1.5         |
| Transmission numerique  | tn    | 3           |
| Anglais                 | ang   | 3           |
| Communication           | com   | 2           |
| Programmation           | prog  | 1.5         |
-------------------------------------------------

Chaque étudiant doit avoir une note dans chaque module de la formation.
En plus des notes, un étudiant est caractérisé par les attributs suivants :
* num : numéro d'étudiant (numérique)
* nom : nom de l'étudiant
* prenom : prénom de l'étudiant

1. Développer une classe Etudiant qui modélise un étudiant
    a. on définira la liste des modules et coefficients par une propriété "modules" de type dictionnaire.
       Ainsi les modules et leur coefficient respectif seront accessibles de manière "static" (indépendemment de l'instance de la classe) : "Etudiant.modules"

    b. Proposer une méthode constructeur pour la classe Etudiant
       On initialisera les notes d'un étudiant à float(0)

2. Proposer une méthode 'add_note()' qui permet d'affecter une note à un étudiant pour un module donné.

3. Proposer une méthode 'moyenne()' qui calcule la moyenne des notes d’un étudiant.