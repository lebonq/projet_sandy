from Spectre import Spectre      #import de la classe Spectre

spectre = Spectre(True,0.2,1,10)  #les parametres correspondent à : longeur(x), largeur(y), probabilité d'avoir du plastique.
#True =  spectre plastique aleatoire, 0.2 la resolution, petie bruit entre 1 et 10 et grand bruit entre 10 et 100
spectre.afficher()          #affiche une description concise de la plage, chaque case est définie par la présence ou non de plastique dedans.
#print(spectre.type_plastique)