"""Implementation d'une queue FIFO avec une liste. Un menu (utilisant un dictionnaire) appelle des procedures sans argument."""
# initialisation
queue = []

# fonctions
def enQueue():
    queue.append(int(input("Entrez un entier:")))
def deQueue():
        if len(queue) == 0:
            print("\nImpossible : la queue est vide!")
        else:
            print("\nElement '{:d}' supprime".format(queue.pop(0)))

def afficheQueue():
    print("\nqueue:",queue)

# programme principal

CMDs = {'a':enQueue, 'v':afficheQueue, 's':deQueue}
menu = """
(A)jouter
(V)oir
(S)upprimer
(Q)uitter

    Votre choix : """

while True:
    while True:
        try:
            choix = input(menu).strip()[0].lower()
        except:
            choix='q'
        if choix not in 'avsq':
            print("Option invalide ! Reessayez")
        else:
            break

    if choix == 'q':
        print("\n Au revoir ! ")
        break
    CMDs[choix]()