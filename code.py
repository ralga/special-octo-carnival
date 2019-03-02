# -*-coding:Latin-1 -*
##Partie I :
#Q1
#==> Un liste ou True est la ou se trouve une bagnole et False non.

#Q2
# On definit la liste comme etant une liste vide donc pleine de false ==> cf Notations dans l'enonce
print("Partie I : Q2")
L = 11*[False]
# Puis on definit les cases particulieres manuellement.
L[0] = True
L[2] = True
L[3] = True
L[10] = True
print("L = {}\n".format(L))

#Q3
def occupe(L,i):
    return L[i]

#Q4 
"""
    Chaque case du tableau peut avoir deux etats, occupe ou vide. 
    Par consequent, sur une liste avec une seule case, il y a deux liste possible :
    ==> la case est occupee par une voiture (L[0] = True)
    ==> La case est inoccupee (L[0] = False)

    Dans le cas d'une liste avec deux case, on a alors :
    ==> les deux cases sont inoccupees (L[0] = L[1] = False)
    ==> La premiere case est occupee mais pas la seconde (L[0] = True, L[1] = False)
    ==> La premiere case est vide et la deuxieme occupee (L[0] = False, L[1] = True)
    ==> Les deux cases sont occupees (L[0] = L[1] = True)

    Comme on peut le voir, sur une liste de taille n, on a 2^n listes possibles
"""

#Q5
def egal(L1,L2):
    #Si elles ne sont pas de la meme longueur la question ne se pose pas
    if(len(L1)!=len(L2)):
        return False
    else :
        #On definit un compteur
        i = 0
        #Tant qu'on trouve que deux cases sont egales et que le compteur ne sort pas de la liste 
        while((L1[i]==L2[i]) and i<len(L1)):
            i += 1
        
        #Si toutes les cases sont egales, on a parcouru tout la liste ==> i == len(L1)
        #Si une des cases est differentes entre L1 et L2, alors on s'est arrete avant la fin ==> i<len(L1)
        #Donc si on trouve que i == len(L1), ca veut dire que les eux listes sont bien egales.
        return i == len(L1)

#Q6
"""
    On doit parcourir toute la liste pour pouvoir determiner si les deux listes sont egales.
    Par consequent, pour une liste de taille n, on a une complexite = O(n)
"""

#Q7
"""
    Booleen. DUH !
"""

##Partie II :
#Q8
"""
    A = [True, False, True, True, False, False, False, False, False, False, True]
    B = avancer(A,False) = [False, True, False, True, True, False, False, False, False, False, False]
    D = avancer(B,True)  = [True, False, True, False, True, True, False, False, False, False, False]

    La reponse est la liste D
"""

#Q9
#La on va partir sur des considerations un peu techniques necessaires pour cette question.
print("Partie 2 : Q9 \n\nDigression technique :")
# on cree un liste avec 10 elements tous initialises a False.
L1 = 10 * [False]
# on declare un 2e liste comme etant egale a la premiere
L2 = L1
# On modifie la 5e valeur de L2
L2[5] = True
# A ton avis, que valent L1 et L2 ? 
print("\tL1 = {}".format(L1))
print("\tL2 = {}".format(L2))

"""
    Un peu d'explications :
    La creation de L1 n'a rien de particulier. Mais ce qui nous interesse c'est la declaration de L2, a savoir "L2 = L1"
    Qu'est ce qu'il se passe a ce moment ?
    
    En realite, ce que fait le programme c'est la chose suivant.
    Quand tu lui dis que L2 = L1, il va comprendre ceci :
    Tu as un objet en memoire appele L1. Et L2 = L1, donc ce qu'on va faire c'est dire que L2 c'est le MEME objet que L1.
    Ca a pour consequence que quand tu modifie L2, tu modifie l'objet dans la memoire. Il va modifier L2 et par consequent L1 puisque c'est la meme chose.
    Donc du coup, modifier L2 revient a modifier L1.

    Ce genre de comportement est très variant d'un language à l'autre donc pour les autres languages il faut tester d'abord.o

    Si tu as le temps ou besoin de plus d'informations, fait des recherches autour des pointeurs (Et probablement un peu autours de la programmation orientee objet (c'est le principe de fonctionnement du python)). 
"""
print("Fin de la digression technique \n\n")
# Fin de la digression technique.

# Cree une liste L2 differente en memoire mais avec les memes valeurs que L.
def create_new_list(L):
    L2 = len(L)*[False]
    i = 0
    while(i<len(L)):
        L2[i] = L[i]
        i+=1
    return L2

def avancer_fin(L,m):
    #On cree un liste L2 differente de L (Voir digression technique)
    L2 = create_new_list(L)
    # Quoi qu'il arrive, la voiture de la derniere case sort de la liste. Si il y a pas voiture, la case ne change pas de valeur.
    L2[len(L2)-1] = False
    # On parcours la liste L2 depuis l'avant derniere case vers m
    i = len(L2)-2
    while(i>=m):
        #Il n'est pas necessaire de verifier si la case suivante est disponible. Par definition elle l'est.
        #L2[i] = False
        L2[i+1] = L2[i]
        i-=1
    #Quoi qu'il arrive, la voiture en m en aura bougé dans cette situation
    L2[m]=False
    return L2

#Q10
def avancer_debut(L,b,m):
    #On cree un liste L2 differente de L (Voir digression technique)
    L2 = create_new_list(L)
    
    #On parcours la liste depuis m-1 jusqu'au debut
    m-=1
    while(m>=0):
        #Il n'est pas necessaire de verifier si la case suivante est disponible. Par definition elle l'est.
        #L2[m] = False
        L2[m+1] = L2[m]
        m-=1
    # On attribue b a la premiere valeur de L2
    L2[0] = b
    return L2

#Q11
def avancer_debut_bloque(L, b, m):
    L2 = create_new_list(L)

    #La case m est bloquee donc si il y a une voiture en m-1, elle ne peut pas bouger, on commence donc en m-2
    m-=2
    while(m>=0):
        #On verifie si la case suivante est disponible
        if(not L2[m+1]):
            L2[m+1] = L2[m]
        m-=1
    # On attribue b a la premiere valeur de L2
    L2[0] = b
    return L2

##Partie III
print("Partie III\n")
#Q12
def avancer_files(L1, b1, L2, b2):
    # On cree les nouvelles listes
    R1 = create_new_list(L1)
    R2 = create_new_list(L2)
    #On definit le point d'intersection
    m = len(L1)/2

    #On fait avancer la fin de R1
    R1 = avancer_fin(R1,m)
    #On fait avancer la fin de R2
    R2 = avancer_fin(R2,m)

    #On fait avancer le debut de R1 sans verifier si m est libre puisque par défaut elle l'est
    R1 = avancer_debut(R1,b1,m)
 
    #On fait avancer le debut de R2 en verifiant si m est libre
    if(R1[m]):
        R2 = avancer_debut_bloque(R2,b1,m)
    else:
        R2 = avancer_debut(R2,b1,m)     
    return(R1,R2)
#Q13
print("Question 13")    
D = [False, True, False, True, False]
E = [False, True, True, False, False]
(R1,R2) = avancer_files(D,False,E,False)
print("D = {}".format(D)+"\nE = {}".format(E))
print("\nLes réponses sont : \nR1 = {}".format(R1)+"\nR2 = {}\n".format(R2))


##Partie IV
print("Partie IV :")
#Q14

'''
    Bah les voitures de L2 sont bloquées tant qu'il y a des voitures qui arrivent a l'intersection dans L1. 
'''

#Q15
"""
    4 étapes pour pouvoir commencer a bouger L2 + 5 pour mettre L2 dans la position voulue => 9 étapes
"""

#Q16
"""

"""