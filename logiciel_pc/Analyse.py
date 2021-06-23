from typing import Counter
import numpy as np
from Spectre import *
from Plage import *

class Analyse:

    def __init__(self):
        self.list_wavelength = self.creation_list_wavelength()
        # CREATION DES MATRICE REFLECTANCE REFERENCE + LONGUEUR D'ONDE POUR LA COMPARAISON
        self.list_wavelength = np.reshape(self.list_wavelength,(512,1))
        self.liste_data_pet = np.reshape(liste_data_pet,(512,1))
        self.liste_data_pvc = np.reshape(liste_data_pvc,(512,1))
        self.liste_data_inkCartridge = np.reshape(liste_data_inkCartridge,(512,1))
        self.liste_data_pla = np.reshape(liste_data_pla,(512,1))
        self.liste_data_peld = np.reshape(liste_data_peld,(512,1))
        self.liste_data_pp = np.reshape(liste_data_pp,(512,1))
        self.liste_data_sable = np.reshape(liste_data_sable,(512,1))
        
        self.matrix_ref_pet = np.append(self.list_wavelength,self.liste_data_pet,axis=1)
        self.matrix_ref_pvc = np.append(self.list_wavelength,self.liste_data_pvc,axis=1)
        self.matrix_ref_inkCartridge = np.append(self.list_wavelength, self.liste_data_inkCartridge, axis=1)
        self.matrix_ref_pla = np.append(self.list_wavelength, self.liste_data_pla, axis=1)
        self.matrix_ref_peld = np.append(self.list_wavelength, self.liste_data_peld, axis=1)
        self.matrix_ref_pp = np.append(self.list_wavelength, self.liste_data_pp, axis=1)
        self.matrix_ref_sable = np.append(self.list_wavelength,self.liste_data_sable,axis=1)


    def creation_list_wavelength(self):
        # LISTE LONGUEURES D'ONDES DE 400 A 2400 nm
        list_wavelength = []   
        list_wavelength.append(-80)
        for i in range (1,512):
            list_wavelength.append(list_wavelength[i-1]+4)
        return list_wavelength

    # RECUPERATION DES DONNEES
    def find_nearest(self, wavelength, value):
        """ Trouver la valeur la plus proche dans une liste
        Parametres
        ----------
        wavelength : array
            la liste
        value : int
            le nombre dont on souhaite trouver la valeur la plus proche dans la liste
        
        Return :
        --------
        idx
            l'indice dans la liste de la valeur la plus proche de celle passée en paramètre
        """
        idx = (np.abs(wavelength-value)).argmin()
        return idx

    def init_matrix_to_studied(self,wavelength,values,list_wavelength):
        """ Initialiser la matrice du spectre dont nous souahitons analyser les valeurs
        Parametres
        ----------
        wavelenght : array
            la liste de l'ensemble des longueur d'onde du spectre étudié (la taille de cette liste dépend de la résolution)
        list_wavelength : array
            la liste des longueur d'onde du spectre de référence (de 400nm à 2400nm par pas de 20nm)
        
        Return
        ------
        matrix_to_studied : array
            une matrice donc la première colonne contient les longueur d'ondes les plus proches de celles de la liste
            et la deuxième colonne, les valeur de réflectance associées
        """
        new_wavelength = []
        new_reflectance = []
        for i in range(len(list_wavelength)):
            idx = self.find_nearest(wavelength,list_wavelength[i])
            new_wavelength.append(wavelength[idx])
            new_reflectance.append(values[idx])

        new_wavelength = np.reshape(new_wavelength,(512,1))
        new_reflectance = np.reshape(new_reflectance,(512,1))
        matrix_to_studied = np.append(new_wavelength,new_reflectance,axis=1)

        return matrix_to_studied

    def mse (self,matrix_ref,matrix_to_studied) :
        """ Calcul de l'erreur quadratique moyenne entre le spectre du matériaux inconnu et celui d'un matériau de référence
        Parametres
        ----------
        matrix_ref : array
            longueur d'onde + réflectance de référance
        matrix_to_studied : array
            longueur d'onde + réflectance du spectre que l'on étudie
        
        Return
        ------
        mse : float
            valeur de l'erreur quadratique moyenne
        """
        mse = []
        for i in range(len(matrix_ref)) :
            erreur = np.abs(matrix_ref[i][1]-matrix_to_studied[i][1])/len(matrix_ref)
            mse.append(erreur)
        mse=sum(mse)
        return mse

    def analysis(self,matrix_to_studied, liste_matrix_ref,row,case):
        """ Calcul de la mse entre le materiau étudié et tous les materiaux de référence
            La mse la plus faible permettra de conclure sur la nature de l'objet
        Parametres
        ----------
        matrix_to_studied : array
            longueur d'onde + réflectance du spectre que l'on étudie
        liste_matrix_ref : array
            liste de l'ensemble des matériaux de référence
        
        Return
        ------
        erreur : float
            valeur de l'erreur quadratique moyenne minimale 
        """

        erreur = []
        for i in range(len(liste_matrix_ref)):            
            if (i == 0):
                matrix_ref = self.matrix_ref_pet
                erreur.append(self.mse(matrix_ref,matrix_to_studied))
            elif (i == 1):
                matrix_ref = self.matrix_ref_pvc
                erreur.append(self.mse(matrix_ref,matrix_to_studied))
            elif (i == 2):
                matrix_ref = self.matrix_ref_inkCartridge
                erreur.append(self.mse(matrix_ref,matrix_to_studied))
            elif (i == 3):
                matrix_ref = self.matrix_ref_peld
                erreur.append(self.mse(matrix_ref,matrix_to_studied))
            elif (i==4):
                matrix_ref = self.matrix_ref_pla
                erreur.append(self.mse(matrix_ref,matrix_to_studied))
            elif (i==5):
                matrix_ref = self.matrix_ref_pp
                erreur.append(self.mse(matrix_ref,matrix_to_studied))
            elif (i==6):
                matrix_ref = self.matrix_ref_sable
                erreur.append(self.mse(matrix_ref,matrix_to_studied))       

        
        idx = erreur.index(min(erreur))
        erreur = min(erreur)

        return erreur, idx

    def scan_plage(self, my_plage, liste_matrix_ref) : 
        wavelength=[]
        values=[]
        x = my_plage.get_dim_plage()[0]
        y = my_plage.get_dim_plage()[1]
        liste_erreur = []

        for row in range(0,x):
            for case in range(0,y):
                wavelength = my_plage.get_specific_Case(row,case).get_spectre().get_longeur_donde()
                values = my_plage.get_specific_Case(row,case).get_spectre().get_reflectance()
                matrix_to_studied = self.init_matrix_to_studied(wavelength,values,self.list_wavelength)
                result = self.analysis(matrix_to_studied,liste_matrix_ref,row,case)
                liste_erreur.append((result[0],result[1],row,case)) # pour chaque case liste avec l'erreur, l'indice du matériau, la position
        
        return liste_erreur

    def affichage_scan (self, my_plage, liste_matrix_ref):
        liste_erreur = self.scan_plage(my_plage,liste_matrix_ref)
        count_global = 0
        count_PET = 0
        count_ink = 0
        count_PLA = 0
        count_PELD = 0
        count_PVC = 0
        count_PP = 0
        count_sable = 0

        x = my_plage.get_dim_plage()[0]
        y = my_plage.get_dim_plage()[1]

        erreur_detec = 105

        for i in range(len(liste_erreur)):
            if (liste_erreur[i][0] > erreur_detec):
                print("Erreur quadratique moyenne minimale : ", liste_erreur[i][0])
                print("  => Conclusion sur la nature de l'objet : matériau non référencé dans la base de donnée")
                my_plage.get_specific_Case(liste_erreur[i][2],liste_erreur[i][3]).typePlastique = "inconnu"
                print("  => Localisation : ", liste_erreur[i][2],liste_erreur[i][3])
            else:
                print("Erreur quadratique moyenne minimale : ", liste_erreur[i][0])
                print("  => Conclusion sur la nature de l'objet : ", liste_matrix_ref[liste_erreur[i][1]])  
                my_plage.get_specific_Case(liste_erreur[i][2],liste_erreur[i][3]).typePlastique = liste_matrix_ref[liste_erreur[i][1]]
                print("  => Localisation : ",liste_erreur[i][2],liste_erreur[i][3])
                        
            if(liste_erreur[i][1] <=  5 and liste_erreur[i][0] < erreur_detec):
                count_global += 1
            if(liste_erreur[i][1] == 0 and liste_erreur[i][0] < erreur_detec):
                count_PET += 1
            if(liste_erreur[i][1] == 1 and liste_erreur[i][0] < erreur_detec):
                count_PVC += 1
            if(liste_erreur[i][1] == 2 and liste_erreur[i][0] < erreur_detec):
                count_ink += 1
            if(liste_erreur[i][1] == 3 and liste_erreur[i][0] < erreur_detec):
                count_PLA += 1
            if(liste_erreur[i][1] == 4 and liste_erreur[i][0] < erreur_detec):
                count_PELD += 1
            if(liste_erreur[i][1] == 5 and liste_erreur[i][0] < erreur_detec):
                count_PP += 1

            
        dim = x * y
        print ("--------------------------------")
        print ("La plage contient",'{0:.0%}'.format(count_global/dim),"de plastique.")

        my_plage.pourcentage = count_global/dim
        my_plage.PET = count_PET/count_global
        my_plage.INK = count_ink/count_global
        my_plage.PLA = count_PLA/count_global
        my_plage.PELD = count_PELD/count_global
        my_plage.PVC = count_PVC/count_global
        my_plage.PP = count_PP/count_global
        
        if(count_global != 0):
            print ("Détails des plastiques détectés : ")
            print ("--------------------------------")
        if(count_PET != 0):
            print ("Polytéréphtalate d'éthylène (PET) : ",'{0:.0%}'.format(count_PET/count_global))
        if(count_PP != 0):
            print ("Polypropylène (PP) : ",'{0:.0%}'.format(count_PP/count_global))
        if (count_PVC!=0):
            print ("Chlorure de polyvinyle (PVC) : ",'{0:.0%}'.format(count_PVC/count_global))
        if (count_PLA != 0):
            print ("Acide polyactique (PLA) : ",'{0:.0%}'.format(count_PLA/count_global))
        if (count_PELD!=0):
            print ("Plastique basse densité (PELD) : ",'{0:.0%}'.format(count_PELD/count_global))
        if(count_ink != 0):
            print ("Polyéthylène haute densité (PEHD) : ",'{0:.0%}'.format(count_ink/count_global))