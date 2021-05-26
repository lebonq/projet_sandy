1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
 
 
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))
 
        painter.drawRect(100, 15, 400,200)
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())