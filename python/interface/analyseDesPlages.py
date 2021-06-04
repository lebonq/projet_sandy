# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
 
# /!\ A CHANGER /!\ ==> importer les plages
import numpy as np
plage = np.array([['S', 'S', 'S', 'P', 'P', 'S', 'S', 'P', 'S', 'S', 'S'],
                  ['S', 'P', 'S', 'P', 'P', 'S', 'S', 'P', 'S', 'S', 'S'],
                  ['S', 'S', 'P', 'P', 'P', 'S', 'S', 'P', 'S', 'S', 'S'],
                  ['S', 'S', 'S', 'P', 'P', 'S', 'S', 'P', 'S', 'S', 'S'],
                  ['S', 'S', 'S', 'S', 'P', 'S', 'S', 'S', 'S', 'P', 'S'],
                  ['P', 'S', 'S', 'P', 'S', 'S', 'S', 'P', 'P', 'S', 'S'],
                  ['S', 'P', 'S', 'S', 'S', 'S', 'P', 'S', 'S', 'S', 'S'],
                  ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                  ['S', 'S', 'S', 'S', 'S', 'P', 'S', 'P', 'S', 'S', 'S'],
                  ['S', 'S', 'S', 'P', 'S', 'S', 'S', 'P', 'S', 'S', 'S']])


#labelPlage = np.chararray((plage.shape[0], plage.shape[1]))

# Override de la classe QLabel
# Source: https://python-forum.io/thread-17718.html
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent):
        super().__init__()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:  # clic boutton gauche de la souris
            self.clicked.emit()


# class Ui_MainWindow(object): --> nom de classe de base

class Ui_MainWindow(QMainWindow):
    # creation et placement des QWidget
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 946)
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Titre.sizePolicy().hasHeightForWidth())
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
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
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
        

        # Creation de n label representant n elements sur la plage (sable ou plastique)
        """ for y in range(plage.shape[1]): # nombre ligne
                    for x in range(plage.shape[0]): # chaque case de la ligne
                        label = "label" + str(y) + str(x)
                        self.label = QtWidgets.QLabel(self.centralwidget)
                        #self.label = ClickableLabel(self.centralwidget)
                        self.label.setObjectName(label)                        
                        self.gridLayout_3.addWidget(self.label, y, x, 1, 1) """
        """ self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label) """

#############
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.spectre = QtWidgets.QLabel(self.centralwidget)
        self.spectre.setEnabled(True)
        self.spectre.setText("")  # label vide
        #self.spectre.setPixmap(QtGui.QPixmap(":/resource/img/spectre.png"))  # affichage de l'image
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
        self.spectre.setPixmap(QtGui.QPixmap(":/resource/img/spectre.png")) # affichage de l'image
        self.spectre.show()


    # affichage du spectre sable
    # ne marche pas /!\
    def spectreSable(self, event):
        self.spectre.setPixmap(QtGui.QPixmap(":/resource/img/plage.JPG")) # affichage de l'image
        self.spectre.show()

    # fonction permettant de definir QPainter et de dessiner
    """ def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawLine(event, self.qp)
        self.qp.end() """

    # fonction permettant de dessiner des rectangles
    # def drawRectangle():
    def setLabels(self):
        pixmap = QPixmap(self.label.size())
        print(self.label.size())
        pixmap.fill(QColor(255, 215, 0))  # dernier 0 = opacité de la couleur
        self.label.setScaledContents(True)
        self.label.setText("oui")
        self.label.setPixmap(pixmap)
        print(self.label.size())

    def setBeach(self):
        _translate = QtCore.QCoreApplication.translate
        for y in range(plage.shape[1]):  # nombre ligne
            for x in range(plage.shape[0]):  # chaque case de la ligne
                label = "label" + str(y) + str(x)
                #self.label = QtWidgets.QLabel(self.centralwidget)
                self.label = ClickableLabel(self.centralwidget)
                self.label.setObjectName(label)
                #self.label.clicked.connect(self.close)
                self.label.mousePressEvent = self.close
                self.gridLayout_3.addWidget(self.label, y, x, 1, 1)
                if (plage[x][y] == 'S'):
                    # self.label.clicked.connect(self.spectrePlastique)
                    self.label.mousePressEvent = self.spectrePlastique
                    self.label.setText(_translate("MainWindow", 'S'))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 215, 0).name()))
                elif (plage[x][y] == 'P'):
                    # self.label.clicked.connect(self.spectreSable)
                    self.label.mousePressEvent = self.spectreSable
                    self.label.setText(_translate("MainWindow", 'P'))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(30, 144, 255).name()))
                else:
                    self.label.setText(_translate("MainWindow", 'N/A'))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 255, 255, 0).name()))
                
                # QtWidgets.QApplication.processEvents()

    # initialisation des QWidget

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Projet Sandy"))
        self.descriptionPlastique.setText(_translate("MainWindow","Description du plastique"))
        self.Titre.setText(_translate("MainWindow","<html><head/><body><p><span style=\" color:#00007f;\">Analyse des plages</span></p></body></html>"))
        self.nomPlage.setText(_translate("MainWindow","Nom de la plage:"))
        self.pollutionPlage.setText(_translate("MainWindow","Pollution de la plage:"))
        self.setBeach()
        #self.label.setText(_translate("MainWindow", 'S'))
        #self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 215, 0).name()))
        #self.ui.label.clicked.connect(self.close)

        # Creation de n label representant n elements sur la plage (sable ou plastique)
        """ for y in range(plage.shape[1]): # nombre ligne
            for x in range(plage.shape[0]): # chaque case de la ligne
                label = "label" + str(y) + str(x)
                #self.label = QtWidgets.QLabel(self.centralwidget)
                #self.label = ClickableLabel(self.centralwidget)
                #self.label.setObjectName(label)                        
                if (plage[x][y] == 'S'):
                    #self.label.clicked.connect(self.spectrePlastique)
                    print(label)
                    self.label.setText(_translate("MainWindow", 'S'))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(255, 215, 0).name()))
                else:
                    #self.label.clicked.connect(self.spectreSable)
                    self.label.setText(_translate("MainWindow", 'P'))
                    self.label.setStyleSheet("background-color: {};".format(QtGui.QColor(30, 144, 255).name()))

                #self.gridLayout_3.addWidget(self.label, y, x, 1, 1)
                #QtWidgets.QApplication.processEvents() """


# main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
