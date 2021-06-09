# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyseDesPlages.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from Analyse import *
from Plage import *
from Spectre import *
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PySide2.QtCore import SIGNAL, QObject


plage = Plage(10,10,0.5)
my_analyse = Analyse().affichage_scan(plage,liste_matrix_ref)


# Override de la classe QLabel
# Source: https://python-forum.io/thread-17718.html
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal() 

    def __init__(self, parent):
        super().__init__()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:  # clic boutton gauche de la souris
            self.clicked.emit()

# Creation de la classe permettant d'afficher les spectres dans Qt
# Source: https://www.mfitzp.com/plotting-matplotlib/
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(object):
    
    # creation et placement des QWidget
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 946)

        MainWindow.setWindowIcon(QtGui.QIcon(":/img/sandy.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.descriptionPlastique = QtWidgets.QLabel(self.centralwidget)
        self.descriptionPlastique.setFrameShape(QtWidgets.QFrame.Box)
        self.descriptionPlastique.setObjectName("descriptionPlastique")
        self.gridLayout_2.addWidget(self.descriptionPlastique, 8, 0, 2, 3)
        self.Titre = QtWidgets.QLabel(self.centralwidget)
        self.Titre.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titre.sizePolicy().hasHeightForWidth())
        self.Titre.setSizePolicy(sizePolicy)
        self.Titre.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Titre.setFont(font)
        self.Titre.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Titre.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Titre.setFrameShape(QtWidgets.QFrame.Box)
        self.Titre.setScaledContents(False)
        self.Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.Titre.setObjectName("Titre")
        self.gridLayout_2.addWidget(self.Titre, 0, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nomPlage = QtWidgets.QLabel(self.centralwidget)
        self.nomPlage.setEnabled(True)
        self.nomPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.nomPlage.setObjectName("nomPlage")
        self.horizontalLayout_2.addWidget(self.nomPlage)
        self.pollutionPlage = QtWidgets.QLabel(self.centralwidget)
        self.pollutionPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.pollutionPlage.setObjectName("pollutionPlage")
        self.horizontalLayout_2.addWidget(self.pollutionPlage)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.x = 0
        self.y = 0

#############
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        # self.spectre = QtWidgets.QLabel(self.centralwidget)
        self.spectre =  MplCanvas(self, width=5, height=4, dpi=100)
        self.spectre.setEnabled(True)
        # self.spectre.setText("")  # label vide
        #self.spectre.setPixmap(QtGui.QPixmap(":/resource/img/spectre.png"))  # affichage de l'image à l'ouverture de l'interface
        #self.spectre.setScaledContents(True) # met la taille de l'image a la taille max du QLabel
        #self.spectre.setMaximumSize(QtCore.QSize(350, 350)) # maximise la taille de l'image en 350x350
        #self.spectre.setAlignment(QtCore.Qt.AlignCenter)
        self.spectre.setObjectName("spectre")
        self.horizontalLayout_3.addWidget(self.spectre)
#############

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # affichage du spectre plastique
    def spectrePlastique(self, x,y):
        print("x = " + str(x) + "  y = " + str(y))
        _translate = QtCore.QCoreApplication.translate
        self.descriptionPlastique.setText(_translate("MainWindow","C'est du plastique :)"))
        self.spectre.axes.clear()
        self.spectre.axes.plot(plage.get_specific_Case(x,y).spectre.plage_longueur_d_onde, plage.get_specific_Case(x,y).spectre.reflectance)
        self.spectre.show()
        self.spectre.draw()

    # affichage du spectre sable
    def spectreSable(self, x,y):
        print("x = " + str(x) + "  y = " + str(y))
        _translate = QtCore.QCoreApplication.translate
        self.descriptionPlastique.setText(_translate("MainWindow","C'est du sable :)"))
        self.spectre.axes.clear()
        self.spectre.axes.plot(plage.get_specific_Case(x,y).spectre.plage_longueur_d_onde, plage.get_specific_Case(x,y).spectre.reflectance)
        self.spectre.show()
        self.spectre.draw()

    def spectreInconnu(self, x,y):
            print("x = " + str(x) + "  y = " + str(y))
            _translate = QtCore.QCoreApplication.translate
            self.descriptionPlastique.setText(_translate("MainWindow","C'est inconnu :,("))
            self.spectre.axes.clear()
            self.spectre.axes.plot(plage.get_specific_Case(x,y).spectre.plage_longueur_d_onde, plage.get_specific_Case(x,y).spectre.reflectance)
            self.spectre.show()
            self.spectre.draw()

    # creation de la plage
    def setBeach(self):
        _translate = QtCore.QCoreApplication.translate
        for y in range(plage.ord):  # nombre ligne
            for x in range(plage.abs):  # chaque case de la ligne
                label = "label" + str(y) + str(x)
                self.label = ClickableLabel(self.centralwidget)
                self.label.setObjectName(label)
                self.gridLayout_3.addWidget(self.label, y, x, 1, 1)
                nomElement = plage.get_specific_Case(x,y).typePlastique
                if (nomElement == "sable"): # si c'est du sable sur la case
                    #self.label.mousePressEvent = self.spectreSable
                    self.label.clicked.connect(lambda  x=x, y=y: self.spectreSable(x,y))
                    self.label.setText(_translate("MainWindow", nomElement))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(253, 221, 92).name()))
                elif (nomElement == "inconnu"): # si l'élement n'est pas reconnu
                    self.label.clicked.connect(lambda  x=x, y=y: self.spectreInconnu(x,y))
                    self.label.setText(_translate("MainWindow", nomElement))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
                else: # si c'est du plastique
                    #self.label.mousePressEvent = self.spectrePlastique
                    self.label.clicked.connect(lambda x=x, y=y: self.spectrePlastique(x,y))
                    self.label.setText(_translate("MainWindow", nomElement))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 156, 159).name()))
                
    # initialisation des QWidget
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Projet Sandy"))
        self.descriptionPlastique.setText(_translate("MainWindow","Description"))
        self.Titre.setText(_translate("MainWindow","<html><head/><body><p><span style=\" color:#00007f;\">Analyse des plages</span></p></body></html>"))
        self.nomPlage.setText(_translate("MainWindow","Caractéristique de la plage: "))
        self.pollutionPlage.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Pollution totale de la plage: "+str('{0:.0%}'.format(plage.pourcentage))+"</span></p>"+
                                                            "<p align=\"center\"><br/><span style=\" font-size:12pt;\">Détails des plastiques détectés: </span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polypropylène (PP): "+str('{0:.0%}'.format(plage.PP))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polyéthylène basse densité (PE-LD): "+str('{0:.0%}'.format(plage.PELD))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polyéthylène téréphtalate (PET): "+str('{0:.0%}'.format(plage.PET))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polyester: "+str('{0:.0%}'.format(plage.Polyester))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">PVC: "+str('{0:.0%}'.format(plage.PVC))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polystyrene: "+str('{0:.0%}'.format(plage.polystyrene))+"</span></p></body></html>"))                    
        self.setBeach()



# main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
