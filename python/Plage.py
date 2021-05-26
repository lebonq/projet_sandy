import random   #import de la librairie random
from Spectre import *

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
    
    def get_dim_plage(self):
        x = self.abs
        y = self.ord
        return x,y
    
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
        self.estPlastique = self.set_estPlastique(proba)  # y a t-il du plastique sur cette case ?
        self.spectre = self.set_spectre()           # Spectre lié à cette case, chaque case à un et unique objet Spectre

    # definit le Spectre de la Case en appelant le constructeur de la classe Spectre
    def set_spectre(self):
        spectre = Spectre(self.estPlastique,0.2,0.0005,1)   # si self.isPlastic vaut True, le constructeur de Spectre devra créer un objet Spectre contenant du plastique, sinon, un objet Spectre ne contenant pas de plastique
        return spectre                      # à voir avec Quentin si cela lui va

    def get_spectre(self):
        return self.spectre

    # retourne l'attribut grille de la classe
    def print_spectre(self):
        return self.spectre.afficher()

    # definit si la Case contient du plastique ou non, definit via la variable 'proba'
    def set_estPlastique(self, proba):
        rand = random.random()
        if rand <= proba:
            return True
        else:
            return False
    
    # retourne l'attribut grille de la classe
    def get_estPlastique(self):
        return self.estPlastique

    # definit l'indice de la case selon la formule suivante. /!\ indice servira surement uniquement pour le debugging
    def set_indice(self, xmax):
        return (xmax*self.y+self.x)

    # retourne l'attribut grille de la classe
    def get_indice(self):     
        return self.indice

    # retourne l'attribut grille de la classe
    def get_case(self):
        if self.estPlastique:
            return 'P'
        else:
            return 'N'

    # affiche une description précise de la case, tous les attributs sont affichés. /!\ cette fonction servira surement uniquement pour le debugging
    def print_infos(self):
        print("Informations de la case :")
        print("x = ", self.x)
        print("y = ", self.y)
        print("indice = ", self.get_indice())
        print("isPlastic = ", self.get_estPlastique())
        print("\nInformations du Spectre :")
        print("spectre = voir fenetre")
        self.print_spectre()