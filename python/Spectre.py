import numpy as np;
import matplotlib.pyplot as plt
import random

#Liste de string possible pour le spectre
liste_matrix_ref = ["orange_pp","white_pe","blue_pp","bottle","white_polyester","sable"]
liste_matrix_plastique = ["orange_pp","white_pe","blue_pp","bottle","white_polyester"]

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
liste_data_sable = [0.05,0.065,0.1,0.125,0.130,0.15,0.175,0.21,0.23,0.24,0.25,0.26,0.27,0.275,0.28,0.283,0.285,0.29,0.3,0.305,0.32,0.325,0.325,0.329,0.329,0.335,0.339,0.339,0.342,0.342,0.344,0.346,0.35,0.352,0.354,0.356,0.359,0.36,0.362,0.367,0.368,0.37,0.372,0.374,0.05,0.065,0.1,0.125,0.130,0.15,0.175,0.21,0.23,0.24,0.25,0.26,0.27,0.275,0.28,0.283,0.285,0.29,0.3,0.305,0.32,0.325,0.325,0.329,0.329,0.335,0.339,0.339,0.342,0.342,0.344,0.346,0.35,0.352,0.354,0.356,0.359,0.36,0.362,0.367,0.368,0.37,0.372,0.374,0.352,0.354,0.356,0.359,0.36,0.362,0.367,0.368,0.37,0.372,0.374,0.372,0.374]

#Classe spectre qui permet de simuler un spectrometre
class Spectre: 

    def __init__(self, plastique,resolution,petit_bruit,grand_bruit):
        self.plastique = plastique #boolean permet de savoir si le spectre est plastique ou non
        self.borne_inf = 400 #Int
        self.borne_sup = 2420 #Int
        self.resolution = resolution #resolution de la courbe
        self.petit_bruit = petit_bruit # une valeur float comme par exemple 0.0005
        self.type_plastique = self.plastique_aleatoire() #string avec le nom du plastique (cf)
        self.grand_bruit = grand_bruit #0 si pas de bruit, 1 si bruit
        self.reflectance = [] #Tableau qui contient la reflectance pour chaque longeur d'onde de plage_longeur_donde
        self.plage_longueur_d_onde = [] #tableai qui contient toute les longeurs d'ondes
        self.creer_spectre()

    # retourne l'attribut isPlastic de la classe
    def est_plastique(self):
        return self.plastique

    #retoure un type de plastique aléatoire
    def plastique_aleatoire(self):
        return random.choice(liste_matrix_plastique)

    #peut etre appeler pour recreer le spectre selon vos besoins
    def creer_spectre(self):
        liste_data = []

        if(self.plastique == True):
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
            #print("Creation spectre plastique")
        else:
            liste_data = liste_data_sable
            #print("Creation spectre sable")


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

        self.reflectance = np.sinc(self.plage_longueur_d_onde*random.uniform(0.0,0.4))*self.grand_bruit + np.sinc(self.plage_longueur_d_onde*random.uniform(0.4,0.9))*self.grand_bruit + np.sinc(self.plage_longueur_d_onde*5) + self.reflectance   ##Pour le bruit

    def afficher(self):# affiche le spectre dans une fenetre numpy
        
        plt.plot(self.plage_longueur_d_onde, self.reflectance)
        plt.show()
    
    def get_reflectance(self):#permet de recupere le tableau avec toute la valeur des reflectances selon la resolution donnee
        return self.reflectance
    
    def get_longeur_donde(self):
        return self.plage_longueur_d_onde
    
    def get_resolution(self):
        return self.resolution
