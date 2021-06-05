#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   Création de la plage puis affichage minimaliste de la plage (P pour plastique, N pour Non-plastique)
#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Plage import Plage       #import de la classe Plage

my_plage = Plage(2,2,0.5)     #les parametres correspondent à : longeur(x), largeur(y), probabilité d'avoir du plastique.
my_plage.print_plage()          #affiche une description concise de la plage, chaque case est définie par la présence ou non de plastique dedans.
my_plage.print_specific_Case_infos(0,1)


