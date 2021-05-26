from Plage import Plage       #import de la classe Plage
from Analyse import *

my_plage = Plage(2,2,0.3)     #les parametres correspondent à : longeur(x), largeur(y), probabilité d'avoir du plastique.
my_plage.print_plage()

my_analyse = Analyse()
my_analyse.scan_plage(my_plage,liste_matrix_ref)