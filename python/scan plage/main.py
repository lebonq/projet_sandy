# scan plage 
import numpy as np

def scan_plage (plage) : 
    print(plage)
    print('longueur de la plage : ', plage.shape[1])
    print('largeur de la plage : ', plage.shape[0])
    
    with open('fichierScan.txt', mode='w') as fichierScan :
        for i in range(0,plage.shape[1]):
            column = plage[:,i]
            for j in range(0,plage.shape[0]):
                contenu = column[j]
                fichierScan.write(contenu +"\n") 
        fichierScan.closed

#################################################################
#################################################################

plage = np.array([['S','S','S','P','P','S','S','P','S','S','S'],
                  ['S','P','S','P','P','S','S','P','S','S','S'],
                  ['S','S','P','P','P','S','S','P','S','S','S'],
                  ['S','S','S','P','P','S','S','P','S','S','S'],
                  ['S','S','S','S','P','S','S','S','S','P','S'],
                  ['P','S','S','P','S','S','S','P','P','S','S'],
                  ['S','P','S','S','S','S','P','S','S','S','S'],
                  ['S','S','S','S','S','S','S','S','S','S','S'],
                  ['S','S','S','S','S','P','S','P','S','S','S'],
                  ['S','S','S','P','S','S','S','P','S','S','S']])

scan = scan_plage(plage)