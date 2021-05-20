import numpy as np;
import matplotlib.pyplot as plt
import random

resolution = 0.02 #Float
borne_inf = 400 #Int
borne_sup = 2400 #Int
bruit = 0.0005 #float

longeur_donde_pics_caracteritiques = [1192,1394,1730] #Int*
reflectance_pics_caracteritiques =   [0.39, 0.4,0.24] #Float*

longeur_donde_spectre_type =     [[400,590] , [590,610], [610,1100],[1100,1350],[1350,1590],[1590,1650],[1650,1900],[1900,2160],[2160,2300],[2300,2400]]
reflectance_donde_spectre_type = [[0.07,0.1],[0.1,0.58],[0.58,0.63],[0.63,0.56],[0.56,0.55], [0.55,0.5], [0.5,0.35],[0.35,0.42],[0.42,0.17],[0.17,0.15]]

type_plastique = "Orange PP rope unrolled"

plage_longueur_d_onde = np.linspace(borne_inf,borne_sup, int((1/resolution)*(borne_sup-borne_inf)))
reflectance = []

for nb in range(0,len(longeur_donde_spectre_type)):
    nb_valeur = int((1/resolution)*(longeur_donde_spectre_type[nb][1]-longeur_donde_spectre_type[nb][0]))
    pas = (reflectance_donde_spectre_type[nb][1] - reflectance_donde_spectre_type[nb][0])/nb_valeur
    for i in range(0,nb_valeur):
        reflectance.append((reflectance_donde_spectre_type[nb][0]+pas*i)+random.uniform(-bruit,bruit))

## reflectance = np.sinc(plage_longueur_d_onde) + reflectance   ##Pour le bruit

'''for nb in range(0,2):
    borne_inf_bruit = round(random.uniform(borne_inf,borne_sup-100),0) #on arrondi a l'unite
    print(borne_inf_bruit)
    borne_sup_bruit = round(borne_inf_bruit + random.uniform(20,100),0)
    print(borne_sup_bruit)
    position_born_inf = int((borne_inf_bruit*resolution - borne_inf*resolution))
    position_born_sup = int((borne_sup_bruit - borne_inf)*resolution)
    milieu = int(position_born_inf + (position_born_sup - position_born_inf)/2)
    reflectance_modif = reflectance[milieu] + random.uniform(-0.5,0.5)
    
    nb_valeur = int((1/resolution)*(milieu - position_born_inf))
    pas = (reflectance_modif - reflectance[position_born_inf])/nb_valeur
    for i in range(0,nb_valeur):
        reflectance[position_born_inf+i] = reflectance[position_born_inf] + pas

    nb_valeur = int((1/resolution)*(position_born_sup - milieu))
    pas = (reflectance[position_born_sup] - reflectance_modif)/nb_valeur
    for i in range(0,nb_valeur):
        reflectance[milieu+i] = reflectance[milieu] + pas'''



plt.plot(plage_longueur_d_onde, reflectance)
plt.show()