from Plage import Plage       #import de la classe Plage
from Analyse import *

my_plage = Plage(2,2,0.3)     #les parametres correspondent à : longeur(x), largeur(y), probabilité d'avoir du plastique.
my_plage.print_plage()

matrix_to_studied = init_matrix_to_studied(wavelength,list_wavelength)
analysis = analysis(matrix_to_studied,liste_matrix_ref)