# coding: utf-8
 
"""
classe qui permet de générer un mot de passe, de longueur variable et caractère différent.

- longueur par défaut de 6 à 25 caractères, modifiable

- mot de passe peux etre que des chiffres, ou lettre + chiffre ou lettre + chiffre + caractère spéciaux

    -- liste des caractères autorisés:
        ABCDEFGHIJKLMNOPQRSTUVWXYZ 
        abcdefghijklmnopqrstuvwxyz 
        0123456789 
        &([-_@)]=+*$%!?

    soit: nombre compris entre 33 et 125 

    n° interdit: 96 ( | ) , 94 ( ^ ), 92 ( "\" ), 60 ( < ), 62 ( < ), 58 ( : ), 59 ( ; ), 47 ( / ), 44 ( , ), 39 ( ' ), 35 ( # ), 34 ( " ), 32 ( espace ) 
        + choix personnel de retirer les accolades car n° 123 ( { ) et n° 125 ( } )


--------------------------------------------------------------
conversion nombre -> ascii python:
    ord('char') : ascii vers int

    str(chr(nombre)) : int vers ascii

"""
from random import randint
from random import random
from random import choice
import time

class GenerateurMotDePasse:

    longueurMin = 0
    longueurMax =  0
    motDePasse = ""

    lettreMaj = True
    lettreMin = True
    nombre = True
    caractereSpeciaux = True

    intervalLettreMaj = [65,90]
    intervalLettreMin = [97,122]
    intervalNombre = [48,57]
    intervalCaractereSpeciaux = [33,125] # prend tout en compte, moins difficile à gerer, + exception à gerer



    def __init__(self, longueurMin = 6 , longueurMax = 24):

        self.lettreMin = True
        self.lettreMaj = True
        self.nombre = True
        self.caractereSpeciaux = False

        if (type(longueurMin) == int and type(longueurMax) == int):
            self.longueurMin = longueurMin
            if(longueurMax < longueurMin):
                #Le mot de passe sera d'une taille fixe
                self.longueurMax = longueurMin 
            else:
                self.longueurMax = longueurMax
        else:
            self.longueurMin = 6
            self.longueurMax = 24

        self.motDePasse = ""

    def genereUnCaractere(self):

        tabVal = []
        nombreAleatoire = 0

        if(self.lettreMaj == True):
            tabVal.append(self.intervalLettreMaj)
        if(self.lettreMin == True):
            tabVal.append(self.intervalLettreMin)
        if(self.nombre == True ):
            tabVal.append(self.intervalNombre)

        if(self.caractereSpeciaux == True):
            #si vrai alors on tire simplement un nombre puis on verifie que le nombre soir differente de: 32 34 35 39 44 47 58 59 62 60 92 94           
            nombreAleatoire = randint(self.intervalCaractereSpeciaux[0] , self.intervalCaractereSpeciaux[1])
            if (nombreAleatoire != 32 or nombreAleatoire != 34 or nombreAleatoire != 35 or nombreAleatoire != 39 or nombreAleatoire != 44  or nombreAleatoire != 47 or nombreAleatoire != 58 or nombreAleatoire != 59 or nombreAleatoire != 60 or nombreAleatoire != 62 or nombreAleatoire != 92 or nombreAleatoire != 94):
                return str(chr(nombreAleatoire))
            else:
                return "" 
        else: 
            #dans le cas ou le mdp ne peux pas comporter de caractères spéciaux
            if len(tabVal) == 0 :
                return
            else:
                if len(tabVal) == 1:
                    nombreAleatoire =  randint( tabVal[0][0] , tabVal[0][1])
                else:
                    interval = choice(tabVal)
                    nombreAleatoire = randint( interval[0] , interval[1] )
            return str(chr(nombreAleatoire)) #on renvoi le caractere en ascii

    def genereMotDePasse(self):
        if( self.lettreMaj == False and self.lettreMin == False and self.nombre == False and self.caractereSpeciaux == False):
            self.motDePasse = ""
        else:
            self.motDePasse = "" # on commence par vider la chaine du mot de passe
            longueurMotDePasse = randint(self.longueurMin,self.longueurMax) # on charge aléatoirement la taille du mot de passe
            while len(self.motDePasse) < longueurMotDePasse :  
                self.motDePasse += self.genereUnCaractere()
                time.sleep(0.1)