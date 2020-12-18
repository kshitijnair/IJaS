import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Window creater
class Window(QWidget):

    # init self window
    def __init__(self):
        super().__init__()
        self.init_ui()

    # design UI for the window
    def init_ui(self):
        self.le = QLineEdit()
        self.b1 = QPushButton('Clear')
        self.b2 = QPushButton('Print')


        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)

        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(1)
        self.s2.setMaximum(99)
        self.s2.setValue(25)
        self.s2.setTickInterval(10)
        self.s2.setTickPosition(QSlider.TicksBelow)

        self.s3 = QSlider(Qt.Horizontal)
        self.s3.setMinimum(1)
        self.s3.setMaximum(99)
        self.s3.setValue(25)
        self.s3.setTickInterval(10)
        self.s3.setTickPosition(QSlider.TicksBelow)

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)
        v_box.addWidget(self.s2)
        v_box.addWidget(self.s3)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Slider')

        self.b1.clicked.connect(lambda: self.btn_clk(self.b1, 'Hello from Clear'))
        self.b2.clicked.connect(lambda: self.btn_clk(self.b2, 'Hello from Print'))
        self.s1.valueChanged.connect(self.v_change)

        self.show()

    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v_change(self):
        my_value = str(self.s1.value())
        self.le.setText(my_value)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())