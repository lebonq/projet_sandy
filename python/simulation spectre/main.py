#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   
#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Spectre import Spectre      #import de la classe Spectre

spectre = Spectre(True,0.2,0.0005,0,"white_pe")  #les parametres correspondent à : longeur(x), largeur(y), probabilité d'avoir du plastique.
spectre.afficher()          #affiche une description concise de la plage, chaque case est définie par la présence ou non de plastique dedans.
