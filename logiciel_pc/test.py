# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 946)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setFrameShape(QtWidgets.QFrame.Box)
        self.description.setObjectName("description")
        self.horizontalLayout.addWidget(self.description)
        self.imageplastique = QtWidgets.QLabel(self.centralwidget)
        self.imageplastique.setMaximumSize(QtCore.QSize(350, 200))
        self.imageplastique.setAutoFillBackground(False)
        self.imageplastique.setFrameShape(QtWidgets.QFrame.Box)
        self.imageplastique.setScaledContents(False)
        self.imageplastique.setObjectName("imageplastique")
        self.horizontalLayout.addWidget(self.imageplastique)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plage2 = QtWidgets.QLabel(self.centralwidget)
        self.plage2.setFrameShape(QtWidgets.QFrame.Box)
        self.plage2.setObjectName("plage2")
        self.gridLayout.addWidget(self.plage2, 1, 2, 1, 1)
        self.plage = QtWidgets.QLabel(self.centralwidget)
        self.plage.setFrameShape(QtWidgets.QFrame.Box)
        self.plage.setObjectName("plage")
        self.gridLayout.addWidget(self.plage, 0, 2, 1, 1)
        self.plage1 = QtWidgets.QLabel(self.centralwidget)
        self.plage1.setFrameShape(QtWidgets.QFrame.Box)
        self.plage1.setObjectName("plage1")
        self.gridLayout.addWidget(self.plage1, 1, 3, 1, 1)
        self.plage3 = QtWidgets.QLabel(self.centralwidget)
        self.plage3.setFrameShape(QtWidgets.QFrame.Box)
        self.plage3.setObjectName("plage3")
        self.gridLayout.addWidget(self.plage3, 0, 3, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.spectre = QtWidgets.QLabel(self.centralwidget)
        self.spectre.setEnabled(True)
        self.spectre.setMaximumSize(QtCore.QSize(1000, 1000))
        self.spectre.setText("")
        self.spectre.setPixmap(QtGui.QPixmap(":/img/img/plage.JPG"))
        self.spectre.setScaledContents(False)
        self.spectre.setAlignment(QtCore.Qt.AlignCenter)
        self.spectre.setObjectName("spectre")
        self.horizontalLayout_3.addWidget(self.spectre)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nomPlage = QtWidgets.QLabel(self.centralwidget)
        self.nomPlage.setEnabled(True)
        self.nomPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.nomPlage.setObjectName("nomPlage")
        self.horizontalLayout_2.addWidget(self.nomPlage)
        self.pollutionPlage = QtWidgets.QLabel(self.centralwidget)
        self.pollutionPlage.setAutoFillBackground(False)
        self.pollutionPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.pollutionPlage.setIndent(-1)
        self.pollutionPlage.setObjectName("pollutionPlage")
        self.horizontalLayout_2.addWidget(self.pollutionPlage)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
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
        self.gridLayout_2.addWidget(self.Titre, 0, 0, 1, 2)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.description.setText(_translate("MainWindow", "TextLabel"))
        self.imageplastique.setText(_translate("MainWindow", "image"))
        self.plage2.setText(_translate("MainWindow", "TextLabel"))
        self.plage.setText(_translate("MainWindow", "TextLabel"))
        self.plage1.setText(_translate("MainWindow", "TextLabel"))
        self.plage3.setText(_translate("MainWindow", "TextLabel"))
        self.nomPlage.setText(_translate("MainWindow", "Nom de plage:"))
        self.pollutionPlage.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Pollution totale de la plage:</span></p><p align=\"center\"><br/><span style=\" font-size:12pt;\">Détails des plastiques détectés: </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Polypropylène (PP): </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Polyéthylène basse densité (PE-LD): </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Polyéthylène téréphtalate (PET): </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Polyester: </span></p><p align=\"center\"><span style=\" font-size:11pt;\">PVC: </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Polystyrene: </span></p></body></html>"))
        self.Titre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#00007f;\">Analyse des plages</span></p></body></html>"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
