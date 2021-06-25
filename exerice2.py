import numpy
def vecteur_stochastique(vecteur) : 
    
    vecteur = numpy.array(vecteur)
    s = numpy.sum(vecteur)
   
    if s == 1 : 
        return True   
    else :
       return False

def matrice_stochastique(matrix):
    l = True
    for vecteur in matrix :
        print(vecteur_stochastique(vecteur))
        if vecteur_stochastique(vecteur) == False:
            l = False
            break
    if l == True :
        return True
    else : 
        return False


v = vecteur_stochastique([0.1,0.3,0.2,0,0.4])
print("vecteur : ",v)

m = [[0,0.2,0,0.8],
     [0.2,0.3,0.1,0.4],
     [0,0.9,0,0.1],
     [0,0.3,0.2,0.5]]

k = matrice_stochastique(m)
print("matrice : ",k)