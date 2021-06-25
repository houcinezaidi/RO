import random 

def lancer_de():
    
    a = random.randint(1,6)
    
    print("le nombre  "+str(a))


def lancer_de_n_fois():
    
    n = input("Donner nombre de fois : ")
    liste = []
    i=0

    while i < int(n):
        nombre = random.randint(1,6)
        liste.append(nombre)
        i = i+1
    print(liste)

    return liste
    print(liste)




def nombre_6():

    liste = lancer_de_n_fois()
    print("liste : ",liste)
    print(" 6 est appare : ",liste.count(6)," fois")


def nombre_6_avant_obtenir():
    
    liste = []
    
    while 1 :
        
        nombre = random.randint(1,6)
        liste.append(nombre)

        if nombre == 6 :
            break
    print("liste : ",liste)
    print("nombre lancement ",len(liste))


def piece_monnaie():
    piece = ["pile","face"]

    n = input("Donner nombre de fois : ")
    liste = []
    i=0

    while i < int(n):

        nombre = random.choice(piece)
        liste.append(nombre)
        i = i+1

    print(liste)


print(" \n1)lancer_de")
lancer_de()
print(" \n2)lancer_de_n_fois")
lancer_de_n_fois()
print(" \n3)nombre_6")
nombre_6()
print(" \n4)nombre_6_avant_obtenir")
nombre_6_avant_obtenir()
print(" \n5)piece_monnaie")
piece_monnaie()