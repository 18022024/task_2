import io
import sys
import random

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>410</y>
     <width>151</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>generate</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        xy1 = random.randint(0, 100)
        xy2 = random.randint(0, 100)
        xy3 = random.randint(0, 100)
        qp.drawEllipse(QPointF(100, 100), xy1, xy1)
        qp.drawEllipse(QPointF(200, 200), xy2, xy2)
        qp.drawEllipse(QPointF(300, 300), xy3, xy3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
