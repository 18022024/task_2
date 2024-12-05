import random
import sys

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Git и случайные окружности')
        self.but = QPushButton(self)
        self.but.move(325, 600)
        self.but.resize(200, 50)
        self.but.setText('generate')


class Circles(Interface):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.but.clicked.connect(self.push)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def push(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        c1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        c2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        c3 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        c4 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        xy1 = random.randint(0, 100)
        xy2 = random.randint(0, 100)
        xy3 = random.randint(0, 100)
        xy4 = random.randint(0, 100)
        qp.setBrush(QColor(c1[0], c1[1], c1[2]))
        qp.drawEllipse(QPointF(100, 300), xy1, xy1)
        qp.setBrush(QColor(c2[0], c2[1], c2[2]))
        qp.drawEllipse(QPointF(300, 300), xy2, xy2)
        qp.setBrush(QColor(c3[0], c3[1], c3[2]))
        qp.drawEllipse(QPointF(500, 300), xy3, xy3)
        qp.setBrush(QColor(c4[0], c4[1], c4[2]))
        qp.drawEllipse(QPointF(700, 300), xy4, xy4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
