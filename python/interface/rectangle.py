import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class BinColUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()
        self.createLabelTop()
        self.createLabelBot()

    def initUi(self):
        self.setWindowTitle('Bin Collection')
        self.setFixedSize(500, 500)
        # self.setStyleSheet('background-color: white')
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawLine(event, self.qp)
        self.qp.end()

    def drawLine(self, event, qp):
        pen = QPen(Qt.red, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(5, 5, 495, 5)
        qp.drawLine(495, 5, 495, 495)
        qp.drawLine(495, 495, 5, 495)
        qp.drawLine(5, 495, 5, 5)

    def createLabelTop(self):
        self.label_top = QLabel('PLEASE WAIT')
        self.label_top.setAlignment(Qt.AlignCenter)
        self.label_top.setFixedSize(450, 60)
        self.label_top.setStyleSheet("font: 14pt Bahnschrift; color: black; background-color: yellow")
        self.generalLayout.addWidget(self.label_top, alignment=Qt.AlignCenter)

    def createLabelBot(self):
        self.label_bot = QLabel('PLEASE WAIT')
        self.label_bot.setAlignment(Qt.AlignCenter)
        self.label_bot.setFixedSize(450, 60)
        self.label_bot.setStyleSheet("font: 14pt Bahnschrift; color: black; background-color: yellow")
        self.generalLayout.addWidget(self.label_bot, alignment=Qt.AlignCenter)

    def setLabels(self, texttop, textbot):
        pixmap = QPixmap(self.label_top.size())
        pixmap.fill(Qt.transparent)
        qp = QPainter(pixmap)
        pen = QPen(Qt.red, 3)
        qp.setPen(pen)
        qp.drawLine(10, 10, 50, 50)
        qp.end()
        self.label_top.setPixmap(pixmap)
        self.label_bot.setText(textbot)

    # draw rectangle + write text
    """ def setLabels(self, texttop, textbot):
    pixmap = QPixmap(self.label_top.size())
    pixmap.fill(Qt.transparent)
    qp = QPainter(pixmap)
    pen = QPen(Qt.red, 3)
    qp.setPen(pen)
    qp.drawLine(10, 10, 50, 50)

    qp.drawText(pixmap.rect(), Qt.AlignCenter, texttop)

    qp.end()
    self.label_top.setPixmap(pixmap)
    self.label_bot.setText(textbot) """

class BinColCtrl:

    def __init__(self, view: BinColUI):
        self._view = view
        self.calculateResult()

    def calculateResult(self):
        line_top = 'NEW LABEL TOP'
        line_bottom = 'NEW LABEL BOTTOM'
        self._view.setLabels(line_top, line_bottom)


def main():
    """Main function."""
    # Create an instance of `QApplication`
    bincol = QApplication(sys.argv)
    window = BinColUI()
    window.show()
    BinColCtrl(view=window)
    sys.exit(bincol.exec_())


if __name__ == '__main__':
    main()