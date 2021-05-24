# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyseDesPlages.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titre = QtWidgets.QLabel(self.centralwidget)
        self.Titre.setEnabled(True)
        self.Titre.setGeometry(QtCore.QRect(0, 0, 1121, 121))
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
        self.nomPlage = QtWidgets.QLabel(self.centralwidget)
        self.nomPlage.setGeometry(QtCore.QRect(0, 130, 131, 31))
        self.nomPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.nomPlage.setObjectName("nomPlage")
        self.pollutionPlage = QtWidgets.QLabel(self.centralwidget)
        self.pollutionPlage.setGeometry(QtCore.QRect(0, 160, 131, 31))
        self.pollutionPlage.setFrameShape(QtWidgets.QFrame.Box)
        self.pollutionPlage.setObjectName("pollutionPlage")
        self.plage = QtWidgets.QLabel(self.centralwidget)
        self.plage.setGeometry(QtCore.QRect(30, 220, 601, 351))
        self.plage.setText("")
        self.plage.setPixmap(QtGui.QPixmap(":/resource/img/plage.JPG"))
        self.plage.setObjectName("plage")
        self.spectre = QtWidgets.QLabel(self.centralwidget)
        self.spectre.setGeometry(QtCore.QRect(650, 300, 421, 201))
        self.spectre.setText("")
        self.spectre.setPixmap(QtGui.QPixmap(":/resource/img/spectre.png"))
        self.spectre.setObjectName("spectre")
        self.descriptionPlastique = QtWidgets.QLabel(self.centralwidget)
        self.descriptionPlastique.setGeometry(QtCore.QRect(30, 600, 1061, 241))
        self.descriptionPlastique.setFrameShape(QtWidgets.QFrame.Box)
        self.descriptionPlastique.setObjectName("descriptionPlastique")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 21))
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
        self.Titre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Analyse des plages</span></p></body></html>"))
        self.nomPlage.setText(_translate("MainWindow", "Nom de la plage:"))
        self.pollutionPlage.setText(_translate("MainWindow", "Pollution de la plage:"))
        self.descriptionPlastique.setText(_translate("MainWindow", "Description du plastique"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

