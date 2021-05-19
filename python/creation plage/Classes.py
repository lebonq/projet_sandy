class Plage:

    def __init__(self, abs, ord):
        self.abs = abs
        self.ord = ord
        self.grille = self.define_grille()

    def define_grille(self):
        grille = [[0]*self.abs]*self.ord
        for y in range(self.ord):
            for x in range(self.abs):
                grille[y][x] = Case(x, y, self.abs, 1)
        return grille

    def print_plage(self):
        print("nombre de lignes :",len(self.grille),"\nnombre de colonnes : ",len(self.grille[0]) )
        for y in range(self.ord):
            for x in range(self.abs):
                print("x = ",x,"  y = ",y, " xmax = ",self.abs)
                self.grille[y][x].print_indice()
        return

class Case:

    def __init__(self, x, y, xmax, spectre):
        self.x = x
        self.y = y
        self.indice = self.set_indice(x, y, xmax)
        self.spectre = spectre

    def set_indice(self, x, y, xmax):
        print("x = ",x,"  y = ",y, " xmax = ", xmax)
        print("indice = ", xmax*y+x)
        return xmax*y+x

    def print_infos(self):
        print("x = ", self.x)
        print("y = ", self.y)
        print("indice = ", self.indice)
        print("spectre = ", self.spectre)

    def print_indice(self):
        print("indice = ", self.indice)