
import sys
from PyQt5 import QtCore, QtWidgets
 
 
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()
 
    def __init__(self, parent):
        super().__init__()
 
    def mouseReleaseEvent(self, event):
        if event.button () == QtCore.Qt.LeftButton:
            self.clicked.emit()
 
 
class Main(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = QtWidgets.QWidget(self)
        self.setCentralWidget(self.ui)
        self.ui.label = ClickableLabel(self)
        self.ui.label.clicked.connect(self.close)
        self.ui.label.setText("Close")
        self.ui.layout = QtWidgets.QVBoxLayout()
        self.ui.layout.addWidget(self.ui.label)
        self.ui.setLayout(self.ui.layout)
        self.show()
 
if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Main(app)
    sys.exit(app.exec_())