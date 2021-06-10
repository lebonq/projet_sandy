# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyseDesPlages.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from Analyse import *
from Plage import *
from Spectre import *
import numpy as np
import os
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

# Creation de la classe permettant d'afficher les spectres avec matplotlib dans Qt
# Source: https://www.mfitzp.com/plotting-matplotlib/
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 946)
        MainWindow.showFullScreen()

        # icon de la fenetre
        pm_icon = QtGui.QPixmap()
        pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sandy.ico")
        MainWindow.setWindowIcon(QtGui.QIcon(pm_icon))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # layout principal
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # layout fiche ID et image
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # layout fiche ID
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setSpacing(0)
        self.Id_usage = QtWidgets.QLabel(self.centralwidget)
        self.Id_usage.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Id_usage.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_usage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_usage.setObjectName("Id_usage")
        self.gridLayout_4.addWidget(self.Id_usage, 3, 0, 1, 1)
        self.Id_papl = QtWidgets.QLabel(self.centralwidget)
        self.Id_papl.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Id_papl.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_papl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_papl.setObjectName("Id_papl")
        self.gridLayout_4.addWidget(self.Id_papl, 5, 0, 1, 1)
        self.Id_abreviation = QtWidgets.QLabel(self.centralwidget)
        self.Id_abreviation.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Id_abreviation.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_abreviation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_abreviation.setObjectName("Id_abreviation")
        self.gridLayout_4.addWidget(self.Id_abreviation, 2, 0, 1, 1)
        self.Id_nvDangerosite = QtWidgets.QLabel(self.centralwidget)
        self.Id_nvDangerosite.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Id_nvDangerosite.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_nvDangerosite.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_nvDangerosite.setObjectName("Id_nvDangerosite")
        self.gridLayout_4.addWidget(self.Id_nvDangerosite, 4, 0, 1, 1)
        self.Id_nomChamp = QtWidgets.QLabel(self.centralwidget)
        self.Id_nomChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_nomChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_nomChamp.setObjectName("Id_nomChamp")
        self.gridLayout_4.addWidget(self.Id_nomChamp, 1, 1, 1, 1)
        self.Id_nom = QtWidgets.QLabel(self.centralwidget)
        self.Id_nom.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Id_nom.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_nom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_nom.setObjectName("Id_nom")
        self.gridLayout_4.addWidget(self.Id_nom, 1, 0, 1, 1)
        self.Id_variable = QtWidgets.QLabel(self.centralwidget)
        self.Id_variable.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_variable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_variable.setObjectName("Id_variable")
        self.gridLayout_4.addWidget(self.Id_variable, 6, 0, 1, 2)
        self.Id_titre = QtWidgets.QLabel(self.centralwidget)
        self.Id_titre.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_titre.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_titre.setObjectName("Id_titre")
        self.gridLayout_4.addWidget(self.Id_titre, 0, 0, 1, 2)
        self.Id_abreviationChamp = QtWidgets.QLabel(self.centralwidget)
        self.Id_abreviationChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_abreviationChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_abreviationChamp.setObjectName("Id_abreviationChamp")
        self.gridLayout_4.addWidget(self.Id_abreviationChamp, 2, 1, 1, 1)
        self.Id_usageChamp = QtWidgets.QLabel(self.centralwidget)
        self.Id_usageChamp.setMinimumSize(QtCore.QSize(0, 130))
        self.Id_usageChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_usageChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_usageChamp.setObjectName("Id_usageChamp")
        self.gridLayout_4.addWidget(self.Id_usageChamp, 3, 1, 1, 1)
        self.Id_nvDangerositeChamp = QtWidgets.QLabel(self.centralwidget)
        self.Id_nvDangerositeChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_nvDangerositeChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_nvDangerositeChamp.setObjectName("Id_nvDangerositeChamp")
        self.gridLayout_4.addWidget(self.Id_nvDangerositeChamp, 4, 1, 1, 1)
        self.Id_paplChamp = QtWidgets.QLabel(self.centralwidget)
        self.Id_paplChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.Id_paplChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Id_paplChamp.setObjectName("Id_paplChamp")
        self.gridLayout_4.addWidget(self.Id_paplChamp, 5, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)

        # label contenant l'image du niveau du plastique (à droite de la fiche ID)
        self.imgPlastique = QtWidgets.QLabel(self.centralwidget)
        self.imgPlastique.setMaximumSize(QtCore.QSize(226, 16777215))
        self.imgPlastique.setMinimumSize(QtCore.QSize(0, 350))
        self.imgPlastique.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
        self.imgPlastique.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imgPlastique.setObjectName("imgPlastique")
        self.horizontalLayout.addWidget(self.imgPlastique)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 2)

        # layout plage et spectre
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3.addLayout(self.gridLayout)

        # creation d'un graphique pour visualiser le spectre
        self.spectre =  MplCanvas(self, width=5, height=4, dpi=100)
        self.spectre.setEnabled(True)
        self.spectre.setObjectName("spectre")
        self.horizontalLayout_3.addWidget(self.spectre)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)

        # layout caracterisation et pollution de la plage
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.caractPlage = QtWidgets.QLabel(self.centralwidget)
        self.caractPlage.setEnabled(True)
        self.caractPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.caractPlage.setObjectName("caractPlage")
        self.horizontalLayout_2.addWidget(self.caractPlage)
        self.pollutionPlage = QtWidgets.QLabel(self.centralwidget)
        self.pollutionPlage.setAutoFillBackground(False)
        self.pollutionPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.pollutionPlage.setIndent(-1)
        self.pollutionPlage.setObjectName("pollutionPlage")
        self.horizontalLayout_2.addWidget(self.pollutionPlage)

        # layout titre
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        # boutton quitter
        self.quitter = QtWidgets.QPushButton(self.centralwidget)
        self.quitter.setMaximumSize(QtCore.QSize(100, 16777215))
        self.quitter.setObjectName("quitter")
        self.gridLayout_2.addWidget(self.quitter, 7, 1, 1, 1)

        # titre
        self.Titre = QtWidgets.QLabel(self.centralwidget)
        self.Titre.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titre.sizePolicy().hasHeightForWidth())
        self.Titre.setSizePolicy(sizePolicy)
        self.Titre.setMinimumSize(QtCore.QSize(0, 100)) # taille minimum du QLabel du titre largeur*hauteur
        self.Titre.setMinimumSize(QtCore.QSize(16777215, 100))
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
        self.gridLayout_2.addWidget(self.Titre, 0, 0, 1, 2)

        # initialisation de la page
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # affichage du spectre plastique
    def spectrePlastique(self, x, y, nomElement):
        _translate = QtCore.QCoreApplication.translate
        #self.descriptionPlastique.setText(_translate("MainWindow","C'est du plastique :)"))

        # affichage du spectre
        self.spectre.axes.clear() # effacage du dernier spectre affiche
        self.spectre.axes.plot(plage.get_specific_Case(x,y).spectre.plage_longueur_d_onde, plage.get_specific_Case(x,y).spectre.reflectance)
        self.spectre.show()
        self.spectre.draw()

        # identique pour toutes les fiches id
        self.gridLayout_4.setSpacing(6)
        self.horizontalLayout.setSpacing(6)
        self.Id_usage.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_papl.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_abreviation.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_nvDangerosite.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_nomChamp.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_nom.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_variable.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_titre.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_abreviationChamp.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_abreviationChamp.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_usageChamp.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_nvDangerositeChamp.setFrameShape(QtWidgets.QFrame.Box)
        self.Id_paplChamp.setFrameShape(QtWidgets.QFrame.Box)
        self.imgPlastique.setFrameShape(QtWidgets.QFrame.Box)

        self.Id_titre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Identité du plastique détecté</span></p></body></html>"))
        self.Id_variable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Le niveau de dangerosité indiqué peut varier suivant les études. </span></p></body></html>"))

        if (nomElement == "white_peld"):
            # affichage de l'image
            pm_icon = QtGui.QPixmap() 
            pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sigle4.jpg") 
            self.imgPlastique.setPixmap(pm_icon)

            # affichage de la fiche id
            self.Id_usage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usages</span></p></body></html>"))
            self.Id_usageChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- Sac de congélation, sac poubelle</span></p><p><span style=\" font-size:10pt;\">- Films alimentaires et barquettes</span></p><p><span style=\" font-size:10pt;\">- Flacons cosmétiques</span></p></body></html>"))
            self.Id_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
            self.Id_abreviation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abréviation</span></p></body></html>"))
            self.Id_abreviationChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PEBD</span></p></body></html>"))
            self.Id_papl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pour aller plus loin</span></p></body></html>"))
            self.Id_nvDangerosite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Niveau de dangerosité</span></p></body></html>"))
            self.Id_nomChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polyéthylène basse densité</span></p></body></html>"))
            self.Id_paplChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- https://www.natura-sciences.com/sante/plastiques-toxicite-sante787.html</span></p><p><span style=\" font-size:10pt;\">- https://www.perturbateur-endocrinien.com/identification-plastique/</span></p></body></html>"))
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Dangerosité faible </span></p><p align=\"justify\"><span style=\" font-size:10pt;\">D\'après le RSE, Raiseau Santé Environnement (France)</span></p></body></html>"))

        elif (nomElement == "blue_pp" or nomElement == "orange_pp"):
            # affichage de l'image
            pm_icon = QtGui.QPixmap() 
            pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sigle5.jpg") 
            self.imgPlastique.setPixmap(pm_icon)

            # affichage de la fiche id
            self.Id_usageChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- Boîtes de conservation (type tupperwar)</span></p><p><span style=\" font-size:10pt;\">- Pots de yaourts, margarines</span></p><p><span style=\" font-size:10pt;\">- Planches à découper en plastique</span></p><p><span style=\" font-size:10pt;\">- Pare-chocs, tableaux de bord de voitures</span></p></body></html>"))
            self.Id_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
            self.Id_abreviationChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PP</span></p></body></html>"))
            self.Id_abreviation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abréviation</span></p></body></html>"))
            self.Id_papl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pour aller plus loin</span></p></body></html>"))
            self.Id_nvDangerosite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Niveau de dangerosité</span></p></body></html>"))
            self.Id_nomChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polypropylène</span></p></body></html>"))
            self.Id_paplChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- https://www.natura-sciences.com/sante/plastiques-toxicite-sante787.html</span></p><p><span style=\" font-size:10pt;\">- https://www.perturbateur-endocrinien.com/identification-plastique/</span></p></body></html>"))
            self.Id_usage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usages</span></p></body></html>"))
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Dangerosité faible </span></p><p align=\"justify\"><span style=\" font-size:10pt;\">D\'après le RSE, Raiseau Santé Environnement (France)</span></p></body></html>"))

        elif (nomElement == "bottle"):
            # affichage de l'image
            pm_icon = QtGui.QPixmap() 
            pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sigle1.jpg")
            self.imgPlastique.setPixmap(pm_icon)

            # affichage de la fiche id
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Dangerosité avérée </span><span style=\" font-size:10pt;\">- d\'après le RSE, Raiseau Santé Environnement (France)</span></p><p><span style=\" font-size:10pt;\">Sous l\'effet du temps et de la chaleur, ce type de plastique est ammené à générer de l\'antimoine, un métal cancérigène qui passe de l\'emballage au contenu.</span></p></body></html>"))
            self.Id_usageChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- Bouteilles d\'eau</span></p><p><span style=\" font-size:10pt;\">- Emballages jetables de tous types et barquettes alimentaires</span></p><p><span style=\" font-size:10pt;\">- Fibres textiles, rembourrage</span></p><p><span style=\" font-size:10pt;\">- Carte de crédit</span></p></body></html>"))
            self.Id_abreviationChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PET</span></p></body></html>"))
            self.Id_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
            self.Id_nvDangerosite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Niveau de dangerosité</span></p></body></html>"))
            self.Id_abreviation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abréviation</span></p></body></html>"))
            self.Id_papl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pour aller plus loin</span></p></body></html>"))
            self.Id_usage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usages</span></p></body></html>"))
            self.Id_paplChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- https://www.natura-sciences.com/sante/plastiques-toxicite-sante787.html</span></p><p><span style=\" font-size:10pt;\">- https://www.perturbateur-endocrinien.com/identification-plastique/</span></p></body></html>"))
            self.Id_nomChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polyéthylène téréphtalate</span></p></body></html>"))

        elif (nomElement == "white_polyester"):
            # affichage de l'image
            pm_icon = QtGui.QPixmap() 
            pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sigle1.jpg") 
            self.imgPlastique.setPixmap(pm_icon)

            # affichage de la fiche id
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Dangerosité avérée </span><span style=\" font-size:10pt;\">- d\'après le RSE, Raiseau Santé Environnement (France)</span></p><p><span style=\" font-size:10pt;\">Sous l\'effet du temps et de la chaleur, ce type de plastique est ammené à générer de l\'antimoine, un métal cancérigène qui passe de l\'emballage au contenu.</span></p></body></html>"))
            self.Id_usageChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- Bouteilles d\'eau</span></p><p><span style=\" font-size:10pt;\">- Emballages jetables de tous types et barquettes alimentaires</span></p><p><span style=\" font-size:10pt;\">- Fibres textiles, rembourrage</span></p><p><span style=\" font-size:10pt;\">- Carte de crédit</span></p></body></html>"))
            self.Id_abreviationChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PET</span></p></body></html>"))
            self.Id_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
            self.Id_nvDangerosite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Niveau de dangerosité</span></p></body></html>"))
            self.Id_abreviation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abréviation</span></p></body></html>"))
            self.Id_papl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pour aller plus loin</span></p></body></html>"))
            self.Id_usage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usages</span></p></body></html>"))
            self.Id_paplChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- https://www.natura-sciences.com/sante/plastiques-toxicite-sante787.html</span></p><p><span style=\" font-size:10pt;\">- https://www.perturbateur-endocrinien.com/identification-plastique/</span></p></body></html>"))
            self.Id_nomChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polyéthylène téréphtalate</span></p></body></html>"))

        elif (nomElement == "pvc"):
            # affichage de l'image
            pm_icon = QtGui.QPixmap() 
            pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sigle3.jpg") 
            self.imgPlastique.setPixmap(pm_icon)

            # affichage de la fiche id
            self.Id_usageChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- Jouets pour enfants</span></p><p><span style=\" font-size:10pt;\">- Tuyeaux de canalisation</span></p><p><span style=\" font-size:10pt;\">- Sols plastiques, revêtements mureaux</span></p></body></html>"))
            self.Id_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
            self.Id_abreviationChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PVC</span></p></body></html>"))
            self.Id_abreviation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abréviation</span></p></body></html>"))
            self.Id_papl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pour aller plus loin</span></p></body></html>"))
            self.Id_nvDangerosite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Niveau de dangerosité</span></p></body></html>"))
            self.Id_nomChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polychlorure de vinyle</span></p></body></html>"))
            self.Id_paplChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- https://www.natura-sciences.com/sante/plastiques-toxicite-sante787.html</span></p><p><span style=\" font-size:10pt;\">- https://www.perturbateur-endocrinien.com/identification-plastique/</span></p></body></html>"))
            self.Id_usage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usages</span></p></body></html>"))
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Dangerosité avérée </span><span style=\" font-size:10pt;\">- d\'après le RSE, Raiseau Santé Environnement (France)</span></p><p><span style=\" font-size:10pt;\">Chauffé, le plastique PVC génère des phtalates pouvent migrer vers d\'autres surfaces. Le PVC est également supecté de contribuer aux pluies acides et de rejeter des dioxines (molécules persistantes et toxiques).</span></p></body></html>"))

        elif (nomElement == "polystyrene"):
            # affichage de l'image
            pm_icon = QtGui.QPixmap()  
            pm_icon.load(os.path.dirname(os.path.abspath(__file__)) + "/img/sigle6.jpg") 
            self.imgPlastique.setPixmap(pm_icon)

            # affichage de la fiche id
            self.Id_usageChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- Barquettes de viandes, de poissons</span></p><p><span style=\" font-size:10pt;\">- Couverts en plastiques </span></p><p><span style=\" font-size:10pt;\">- Isolants thermiques (cloisons, planchers)</span></p><p><span style=\" font-size:10pt;\">- Flotteurs et planches à voiles</span></p></body></html>"))
            self.Id_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
            self.Id_abreviationChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PS</span></p></body></html>"))
            self.Id_abreviation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abréviation</span></p></body></html>"))
            self.Id_papl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Pour aller plus loin</span></p></body></html>"))
            self.Id_nvDangerosite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Niveau de dangerosité</span></p></body></html>"))
            self.Id_nomChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polystyrène</span></p></body></html>"))
            self.Id_paplChamp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- https://www.natura-sciences.com/sante/plastiques-toxicite-sante787.html</span></p><p><span style=\" font-size:10pt;\">- https://www.perturbateur-endocrinien.com/identification-plastique/</span></p></body></html>"))
            self.Id_usage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usages</span></p></body></html>"))
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Dangerosité avéréé </span><span style=\" font-size:10pt;\">- d\'après le RSE, Raiseau Santé Environnement (France)</span></p><p align=\"justify\"><span style=\" font-size:10pt;\">Exposé à la chaleur le polystyrène risque de dégager du styrène qui pourrait être cancérigène selon le CIRC (Centre International de la Recherche sur le Cancer).</span></p></body></html>"))
        

    # affichage du spectre d'element inconnu du logiciel
    def spectreNonPlastique(self, x, y, nomElement):
            _translate = QtCore.QCoreApplication.translate

            # affichage du spectre
            self.spectre.axes.clear() # effacage du dernier spectre affiche
            self.spectre.axes.plot(plage.get_specific_Case(x,y).spectre.plage_longueur_d_onde, plage.get_specific_Case(x,y).spectre.reflectance)
            self.spectre.show()
            self.spectre.draw()

            # affichage de la fiche id en blanc
            self.horizontalLayout.setSpacing(0)
            self.gridLayout_4.setSpacing(0)
            self.Id_usage.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_usage.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_papl.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_papl.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_abreviation.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_abreviation.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_nvDangerosite.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_nvDangerosite.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_nomChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_nomChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_nom.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_nom.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_variable.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_variable.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_titre.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_titre.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_abreviation.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_abreviation.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_abreviationChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_abreviationChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_usageChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_usageChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_nvDangerositeChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_nvDangerositeChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.Id_paplChamp.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_paplChamp.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
            self.imgPlastique.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Id_usage.setText(_translate("MainWindow", ""))
            self.Id_usageChamp.setText(_translate("MainWindow", ""))
            self.Id_abreviation.setText(_translate("MainWindow", ""))
            self.Id_abreviationChamp.setText(_translate("MainWindow", ""))
            self.Id_nvDangerosite.setText(_translate("MainWindow", ""))
            self.Id_nvDangerositeChamp.setText(_translate("MainWindow", ""))
            self.Id_nom.setText(_translate("MainWindow", ""))
            self.Id_nomChamp.setText(_translate("MainWindow", ""))
            self.Id_papl.setText(_translate("MainWindow", ""))
            self.Id_paplChamp.setText(_translate("MainWindow", ""))
            self.Id_titre.setText(_translate("MainWindow", ""))
            self.Id_variable.setText(_translate("MainWindow", ""))
            self.imgPlastique.clear() # effacage de l'image

    # creation de la plage
    def setBeach(self):
        _translate = QtCore.QCoreApplication.translate
        for y in range(plage.ord):  # nombre ligne
            for x in range(plage.abs):  # chaque case de la ligne
                label = "label" + str(y) + str(x)
                self.label = ClickableLabel(self.centralwidget)
                self.label.setObjectName(label)
                self.gridLayout.addWidget(self.label, y, x, 1, 1)
                nomElement = plage.get_specific_Case(x,y).typePlastique
                self.label.setText(_translate("MainWindow", nomElement))
                if (nomElement == "sable"): # si c'est du sable sur la case
                    self.label.clicked.connect(lambda  x=x, y=y, nom = nomElement: self.spectreNonPlastique(x,y,nom))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(253, 221, 92).name()))
                elif (nomElement == "inconnu"): # si l'élement n'est pas reconnu
                    self.label.clicked.connect(lambda  x=x, y=y,nom = nomElement: self.spectreNonPlastique(x,y,nom))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255).name()))
                else: # si c'est du plastique
                    self.label.clicked.connect(lambda x=x, y=y, nom = nomElement: self.spectrePlastique(x,y,nom))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 156, 159).name()))

                    

                    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Projet Sandy")) # nom de la fenêtre
        # initialisation de la fiche id vide
        self.Id_usage.setText(_translate("MainWindow", ""))
        self.Id_papl.setText(_translate("MainWindow", ""))
        self.Id_abreviation.setText(_translate("MainWindow", ""))
        self.Id_nvDangerosite.setText(_translate("MainWindow", ""))
        self.Id_nomChamp.setText(_translate("MainWindow", ""))
        self.Id_nom.setText(_translate("MainWindow", ""))
        self.Id_variable.setText(_translate("MainWindow", ""))
        self.Id_titre.setText(_translate("MainWindow", ""))
        self.Id_abreviationChamp.setText(_translate("MainWindow", ""))
        self.Id_usageChamp.setText(_translate("MainWindow", ""))
        self.Id_nvDangerositeChamp.setText(_translate("MainWindow", ""))
        self.Id_paplChamp.setText(_translate("MainWindow", ""))
        self.imgPlastique.setText(_translate("MainWindow", ""))

        # initialisation de la caractérisation de la plage 
        self.caractPlage.setText(_translate("MainWindow", "Caractérisation de la plage:"))

        # affichage du détail de la pollution de la plage
        self.pollutionPlage.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Pollution totale de la plage: "+str('{0:.0%}'.format(plage.pourcentage))+"</span></p>"+
                                                            "<p align=\"center\"><br/><span style=\" font-size:12pt;\">Détails des plastiques détectés: </span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polypropylène (PP): "+str('{0:.0%}'.format(plage.PP))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polyéthylène basse densité (PE-LD): "+str('{0:.0%}'.format(plage.PELD))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polyéthylène téréphtalate (PET): "+str('{0:.0%}'.format(plage.PET))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polyester: "+str('{0:.0%}'.format(plage.Polyester))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">PVC: "+str('{0:.0%}'.format(plage.PVC))+"</span></p>"+
                                                            "<p align=\"center\"><span style=\" font-size:11pt;\">Polystyrene: "+str('{0:.0%}'.format(plage.polystyrene))+"</span></p></body></html>"))
        self.Titre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#00007f;\">Analyse des plages</span></p></body></html>"))
        self.setBeach() # creation des QLabel pour dessiner la plage

        self.quitter.setText(_translate("MainWindow", "Quitter")) # texte sur le bouton
        self.quitter.clicked.connect(app.quit)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
