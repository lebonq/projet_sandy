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

        MainWindow.setWindowIcon(QtGui.QIcon(":/img/img/logoV2.png"))
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

#############
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.spectre = QtWidgets.QLabel(self.centralwidget)
        self.spectre.setEnabled(True)
        self.spectre.setText("")  # label vide
        #self.spectre.setPixmap(QtGui.QPixmap(":/resource/img/spectre.png"))  # affichage de l'image à l'ouverture de l'interface
        #self.spectre.setScaledContents(True) # met la taille de l'image a la taille max du QLabel
        #self.spectre.setMaximumSize(QtCore.QSize(350, 350)) # maximise la taille de l'image en 350x350
        self.spectre.setAlignment(QtCore.Qt.AlignCenter)
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
    def spectrePlastique(self, event):
        _translate = QtCore.QCoreApplication.translate
        self.descriptionPlastique.setText(_translate("MainWindow","C'est du plastique :)"))
        self.spectre.setPixmap(QtGui.QPixmap(":/img/img/spectre.png"))
        self.spectre.show()


    # affichage du spectre sable
    def spectreSable(self, event):
        _translate = QtCore.QCoreApplication.translate
        self.descriptionPlastique.setText(_translate("MainWindow","C'est du sable :)"))
        self.spectre.setPixmap(QtGui.QPixmap(":/img/img/plage.JPG"))
        self.spectre.show()


    # creation de la plage
    def setBeach(self):
        _translate = QtCore.QCoreApplication.translate
        for y in range(plage.ord):  # nombre ligne
            for x in range(plage.abs):  # chaque case de la ligne
                label = "label" + str(y) + str(x)
                self.label = ClickableLabel(self.centralwidget)
                self.label.setObjectName(label)
                self.gridLayout_3.addWidget(self.label, y, x, 1, 1)
                if (plage.get_specific_Case(x,y).get_spectre().type_plastique == "sable"): # type de plastique 
                    self.label.mousePressEvent = self.spectreSable
                    self.label.setText(_translate("MainWindow", 'N'))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 215, 0).name()))
                else: # si c'est du plastique
                    self.label.mousePressEvent = self.spectrePlastique
                    self.label.setText(_translate("MainWindow", plage.get_specific_Case(x,y).get_spectre().type_plastique))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(30, 144, 255).name()))
                


    # initialisation des QWidget
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Projet Sandy"))
        self.descriptionPlastique.setText(_translate("MainWindow","Description"))
        self.Titre.setText(_translate("MainWindow","<html><head/><body><p><span style=\" color:#00007f;\">Analyse des plages</span></p></body></html>"))
        self.nomPlage.setText(_translate("MainWindow","Nom de la plage:"))
        self.pollutionPlage.setText(_translate("MainWindow","Pollution de la plage:"))
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
