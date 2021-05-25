import numpy as np
from Spectre import Spectre

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

# LISTE LONGUEURES D'ONDES DE 400 A 2400 nm
list_wavelength = []   
list_wavelength.append(400)
for i in range (1,101):
    list_wavelength.append(list_wavelength[i-1]+20)

# CREATION DES MATRICE REFLECTANCE REFERENCE + LONGUEUR D'ONDE POUR LA COMPARAISON
list_wavelength = np.reshape(list_wavelength,(101,1))
liste_data_blue_pp = np.reshape(liste_data_blue_pp,(101,1))
liste_data_bottle = np.reshape(liste_data_bottle,(101,1)) 
liste_data_orange_pp = np.reshape(liste_data_orange_pp,(101,1))
liste_data_white_polyester = np.reshape(liste_data_white_polyester,(101,1))
liste_data_white_pe = np.reshape(liste_data_white_pe,(101,1))

matrix_ref_blue_pp = np.append(list_wavelength,liste_data_blue_pp,axis=1)
matrix_ref_bottle = np.append(list_wavelength,liste_data_bottle,axis=1)
matrix_ref_orange_pp = np.append(list_wavelength,liste_data_orange_pp,axis=1)
matrix_ref_white_polyester = np.append(list_wavelength,liste_data_white_polyester,axis=1)
matrix_ref_white_pe = np.append(list_wavelength,liste_data_white_pe,axis=1) 

liste_matrix_ref = ["orange_pp","white_pe","blue_pp","bottle","white_polyester"]

# CREATION SPECTRE
spectre = Spectre(True,0.2,0.0005,"white_pe")  
values = spectre.get_reflectance()
wavelength = spectre.get_longeur_donde()
resolution = spectre.get_resolution()

# RECUPERATION DES DONNEES

def find_nearest(wavelength, value):
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

def init_matrix_to_studied(wavelength,list_wavelength):
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
        idx = find_nearest(wavelength,list_wavelength[i])
        new_wavelength.append(wavelength[idx])
        new_reflectance.append(values[idx])

    new_wavelength = np.reshape(new_wavelength,(101,1))
    new_reflectance = np.reshape(new_reflectance,(101,1))
    matrix_to_studied = np.append(new_wavelength,new_reflectance,axis=1)

    return matrix_to_studied

def mse (matrix_ref,matrix_to_studied) :
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

def analysis (matrix_to_studied, liste_matrix_ref):
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
            matrix_ref = matrix_ref_orange_pp
            erreur.append(mse(matrix_ref,matrix_to_studied))
        elif (i == 1):
            matrix_ref = matrix_ref_white_pe
            erreur.append(mse(matrix_ref,matrix_to_studied))
        elif (i == 2):
            matrix_ref = matrix_ref_blue_pp
            erreur.append(mse(matrix_ref,matrix_to_studied))
        elif (i == 3):
            matrix_ref = matrix_ref_bottle
            erreur.append(mse(matrix_ref,matrix_to_studied))
        elif (i == 4):
            matrix_ref = matrix_ref_white_polyester
            erreur.append(mse(matrix_ref,matrix_to_studied))
    
    idx = erreur.index(min(erreur))
    erreur = min(erreur)
    
    if (erreur > 0.5) :
        print("Matériau non référencé dans la base de données.")
     
    print("Erreur quadratique moyenne minimale : ", erreur)
    print("Conclusion sur la nature de l'objet : ", liste_matrix_ref[idx] )

    return erreur


matrix_to_studied = init_matrix_to_studied(wavelength,list_wavelength)
analysis = analysis(matrix_to_studied,liste_matrix_ref)

