import random   #import de la librairie random
import numpy as np
import matplotlib.pyplot as plt

#Liste de string possible pour le spectre
liste_type_plastique = ["orange_pp","white_pe","blue_pp","bottle","white_polyester"]

# ORANGE PP ROPE UNROLLED
liste_data_orange_pp = [0.07,0.06,0.07,0.08,0.1,0.12,0.13,0.1,0.15,0.4,0.54,0.58,0.6,0.6,0.6,0.6,0.6,0.58,0.6,0.61,0.61,0.6,0.6,0.6,0.58,0.55,0.56,0.6,0.64,0.62,0.6,0.58,0.62,0.63,0.63,0.64,0.62,0.6,0.5,0.45,0.4,0.42,0.5,0.55,0.59,0.6,0.6,0.58,0.5,0.42,0.4,0.43,0.47,0.5,0.51,0.53,0.56,0.59,0.59,0.57,0.56,0.51,0.5,0.5,0.4,0.25,0.27,0.24,0.3,0.33,0.33,0.33,0.35,0.39,0.39,0.39,0.4,0.4,0.39,0.38,0.5,0.52,0.53,0.53,0.53,0.54,0.55,0.55,0.52,0.5,0.48,0.47,0.44,0.22,0.15,0.17,0.1,0.15,0.12,0.13,0.13]

## WHITE PE-LD CUP FLAT
liste_data_white_pe = [0.6,0.75,0.77,0.75,0.74,0.73,0.72,0.72,0.71,0.71,0.71,0.71,0.71,0.7,0.7,0.695,0.69,0.69,0.685,0.68,0.68,0.675,0.67,0.67,0.655,0.65,0.65,0.645,0.64,0.64,0.635,0.63,0.63,0.625,0.63,0.615,0.61,0.6,0.58,0.53,0.51,0.515,0.55,0.55,0.55,0.55,0.54,0.53,0.53,0.5,0.48,0.48,0.48,0.48,0.48,0.48,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.45,0.39,0.39,0.41,0.42,0.43,0.44,0.42,0.42,0.42,0.42,0.42,0.42,0.42,0.42,0.44,0.45,0.46,0.47,0.48,0.48,0.49,0.49,0.48,0.48,0.47,0.47,0.46,0.4,0.37,0.36,0.34,0.35,0.35,0.36,0.36,0.38]

## BLUE PP ROPE UNROLLED
liste_data_blue_pp = [0.1,0.12,0.14,0.17,0.17,0.14,0.12,0.08,0.05,0.05,0.05,0.05,0.06,0.06,0.06,0.05,0.07,0.08,0.12,0.15,0.18,0.2,0.2,0.21,0.21,0.21,0.21,0.22,0.23,0.23,0.23,0.22,0.25,0.25,0.24,0.24,0.22,0.22,0.21,0.18,0.18,0.2,0.23,0.25,0.26,0.26,0.24,0.23,0.21,0.2,0.2,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.28,0.28,0.27,0.25,0.24,0.24,0.2,0.12,0.12,0.13,0.16,0.17,0.18,0.17,0.18,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.22,0.23,0.24,0.24,0.24,0.24,0.24,0.24,0.23,0.21,0.22,0.23,0.17,0.1,0.09,0.1,0.08,0.09,0.07,0.09,0.1]

#PET BOTTLE
liste_data_bottle = [0.18,0.18,0.18,0.18,0.17,0.17,0.16,0.15,0.15,0.15,0.16,0.16,0.15,0.17,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.18,0.16,0.17,0.17,0.17,0.17,0.17,0.17,0.17,0.17,0.17,0.17,0.17,0.17,0.16,0.15,0.14,0.16,0.16,0.16,0.16,0.16,0.16,0.16,0.16,0.16,0.16,0.13,0.12,0.13,0.15,0.12,0.15,0.15,0.16,0.16,0.16,0.16,0.17,0.17,0.14,0.15,0.15,0.14,0.15,0.15,0.16,0.16,0.16,0.15,0.16,0.12,0.11,0.13,0.14,0.15,0.12,0.1,0.08,0.09,0.1,0.08,0.07,0.08,0.1,0.1]

# WHITE POLYESTER
liste_data_white_polyester = [0.54,0.56,0.6,0.61,0.61,0.61,0.61,0.61,0.6,0.6,0.59,0.58,0.58,0.57,0.57,0.57,0.57,0.57,0.57,0.57,0.57,0.56,0.56,0.56,0.54,0.55,0.55,0.55,0.55,0.55,0.55,0.54,0.55,0.56,0.57,0.55,0.55,0.5,0.47,0.51,0.5,0.52,0.54,0.55,0.55,0.55,0.55,0.54,0.52,0.48,0.47,0.46,0.46,0.46,0.5,0.5,0.52,0.53,0.53,0.53,0.53,0.52,0.5,0.4,0.29,0.3,0.37,0.38,0.4,0.43,0.44,0.42,0.42,0.45,0.44,0.4,0.42,0.44,0.41,0.44,0.44,0.45,0.45,0.43,0.4,0.38,0.36,0.28,0.3,0.32,0.35,0.3,0.23,0.2,0.24,0.23,0.22,0.2,0.2,0.22,0.22]

## Sable
liste_data_sable = []


# Notre objet Plage, il contient les cases faisant lien avec notre plage.
class Plage:  

    # constructeur, abs correspond a la longueur (ou x), ord correspond à la largeur(ou y) et proba est la probabilité d'avoir du plastique sur cette case
    def __init__(self, abs, ord, proba):
        self.abs = abs
        self.ord = ord
        self.grille = self.set_grille(proba)
    
    # definit la grille, cette fonction est appelée dans le constructeur et n'est censée servir qu'une fois
    def set_grille(self, proba):
        grille = [[0] * self.abs for i in range(self.ord)]
        for y in range(self.ord):
            for x in range(self.abs):
                grille[y][x] = Case(x, y, self.abs, proba)
        return grille
    
    # retourne l'attribut grille de la classe
    def get_grille(self):
        return self.grille

    # affiche chaque case de la plage avec précision. Cette fonction affiche tous les attributs de la case, pour chaque case. /!\ ne pas utiliser sur de trop grand tableaux, devient illisible
    def print_infos_plage(self):
        for y in range(self.ord):
            for x in range(self.abs):
                self.grille[y][x].print_infos()
        return
    
    # affiche une description concise de la plage, chaque case est definit par la présence ou non de plastique dedans.
    def print_plage(self):
        for y in range(self.ord):
            for x in range(self.abs):
                print("--", end="", flush=True)
            print("-")
            for x in range(self.abs):
                print("|", end="", flush=True)
                print(self.grille[y][x].get_case(), end="", flush=True)
            print("|")
        for x in range(self.abs):
            print("--", end="", flush=True)
        print("-")

    def get_specific_Case(self,x,y):
        return self.grille[y][x]
    
    def print_specific_Case_infos(self,x,y):
        self.grille[y][x].print_infos()


# Notre objet Case, contient différents attributs permettant de définir la case
class Case:

    # constructeur, x correspond a la longueur, y correspond à la largeur, xmax est la longueur de la plage et proba est la probabilité d'avoir du plastique sur cette case
    def __init__(self, x, y, xmax, proba):
        self.x = x
        self.y = y
        self.indice = self.set_indice(xmax)         # indice est le numéro de la case, par exemple, pour une plage en 3x3, les cases sont numérotées de 0 à 8
        self.estPlactique = self.set_estPlactique(proba)  # y a t-il du plastique sur cette case ?
        self.spectre = self.set_spectre()           # Spectre lié à cette case, chaque case à un et unique objet Spectre

    # definit le Spectre de la Case en appelant le constructeur de la classe Spectre
    def set_spectre(self):
        spectre = Spectre(self.estPlactique,0.2,1)   # si self.isPlastic vaut True, le constructeur de Spectre devra créer un objet Spectre contenant du plastique, sinon, un objet Spectre ne contenant pas de plastique
        return spectre                      # à voir avec Quentin si cela lui va

    # retourne l'attribut grille de la classe
    def print_spectre(self):
        return self.spectre.afficher()

    # definit si la Case contient du plastique ou non, definit via la variable 'proba'
    def set_estPlactique(self, proba):
        rand = random.random()
        if rand <= proba:
            return True
        else:
            return False
    
    # retourne l'attribut grille de la classe
    def get_estPlactique(self):
        return self.estPlactique

    # definit l'indice de la case selon la formule suivante. /!\ indice servira surement uniquement pour le debugging
    def set_indice(self, xmax):
        return (xmax*self.y+self.x)

    # retourne l'attribut grille de la classe
    def get_indice(self):     
        return self.indice

    # retourne l'attribut grille de la classe
    def get_case(self):
        if self.estPlactique:
            return 'P'
        else:
            return 'N'

    # affiche une description précise de la case, tous les attributs sont affichés. /!\ cette fonction servira surement uniquement pour le debugging
    def print_infos(self):
        print("Informations de la case :")
        print("x = ", self.x)
        print("y = ", self.y)
        print("indice = ", self.get_indice())
        print("isPlastic = ", self.get_estPlactique())
        print("\nInformations du Spectre :")
        print("spectre = voir fenetre")
        self.print_spectre()

class Spectre: 

    def __init__(self, plastique,resolution,grand_bruit):
        self.plastique = plastique #boolean permet de savoir si le spectre est plastique ou non
        self.borne_inf = 400 #Int
        self.borne_sup = 2420 #Int
        self.resolution = resolution #resolution de la courbe
        #self.petit_bruit = petit_bruit # une valeur float comme par exemple 0.0005
        self.petit_bruit = self.petit_bruit_aleatoire()
        #self.type_plastique = type_plastique #string avec le nom du plastique (cf)
        self.type_plastique = self.plastique_aleatoire()
        self.grand_bruit = grand_bruit #0 si pas de bruit, 1 si bruit
        self.creer_spectre()

    # retourne un bruit aléatoire
    def petit_bruit_aleatoire(self):
        rand = random.uniform(0.00010,0.00099)
        return rand

    #retoure un type de plastique aléatoire
    def plastique_aleatoire(self): 
        plastique = ["orange_pp", "white_pe", "blue_pp", "bottle", "white_polyester"]
        return random.choice(plastique)

    # retourne l'attribut isPlastic de la classe
    def est_plastique(self):
        return self.plastique

    #peut etre appeler pour recreer le spectre selon vos besoins
    def creer_spectre(self):
        liste_data = []

        if(self.est_plastique):
            if(self.type_plastique == "orange_pp"):
                liste_data = liste_data_orange_pp
            elif(self.type_plastique == "white_pe"):
                liste_data = liste_data_white_pe
            elif(self.type_plastique == "blue_pp"):
                liste_data = liste_data_blue_pp
            elif(self.type_plastique == "bottle"):
                liste_data = liste_data_bottle
            elif(self.type_plastique == "white_polyester"):
                liste_data = liste_data_white_polyester
            else:
                print("Erreur type plastique")
                return
        else:
            liste_data = liste_data_sable


        list_wavelength = []   

        list_wavelength.append([400.0,420.0])
        for i in range (1,101):
            list_wavelength.append([list_wavelength[i-1][1],list_wavelength[i-1][1]+20.0])

        data1 = np.zeros(101)
        data2 = np.zeros(101)

        for i in range (101):
            data1[i] = liste_data[i]

        for i in range (100):
            data2[i] = liste_data[i+1]

        data2[100] = data1[100]

        data1 = np.reshape(data1,(101,1))
        data2 = np.reshape(data2,(101,1))
        matrix_data = np.append(data1,data2,axis=1)

        longeur_donde_spectre_type = list_wavelength
        reflectance_donde_spectre_type = matrix_data

        self.plage_longueur_d_onde = np.linspace(self.borne_inf,self.borne_sup, int((1/self.resolution)*(self.borne_sup-self.borne_inf)))
        self.reflectance = []

        for nb in range(len(longeur_donde_spectre_type)):
            nb_valeur = int((1/self.resolution)*(longeur_donde_spectre_type[nb][1]-longeur_donde_spectre_type[nb][0]))
            pas = (reflectance_donde_spectre_type[nb][1] - reflectance_donde_spectre_type[nb][0])/nb_valeur
            for i in range(nb_valeur):
                self.reflectance.append((reflectance_donde_spectre_type[nb][0]+pas*i)+random.uniform(-self.petit_bruit,self.petit_bruit))#Pour le petit bruit

        self.reflectance = np.sinc(self.plage_longueur_d_onde*0.02)*self.grand_bruit + np.sinc(self.plage_longueur_d_onde*0.05)*self.grand_bruit + np.sinc(self.plage_longueur_d_onde*5) + self.reflectance   ##Pour le bruit

    def afficher(self):# affiche le spectre dans une fenetre numpy
        plt.plot(self.plage_longueur_d_onde, self.reflectance)
        plt.show()
    
    def get_reflectance(self):#permet de recupere le tableau avec toute la valeur des reflectances selon la resolution donnee
        return self.reflectance
    
    def get_longeur_donde(self):
        return self.plage_longueur_d_onde
    
    def get_resolution(self):
        return self.resolution