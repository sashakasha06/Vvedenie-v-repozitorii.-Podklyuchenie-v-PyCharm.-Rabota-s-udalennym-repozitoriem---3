import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QBrush, QColor
import random


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.fl = False

    def button_clicked(self):
        self.fl = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        if self.fl:
            r = random.randint(10, 50)
            center = (random.randint(50, self.width() - 50), random.randint(50, self.height() - 50))
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setBrush(QBrush(color))
            qp.drawEllipse(center[0] - r, center[1] - r, 2 * r, 2 * r)
        qp.end()
        self.fl = False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 500, 500)
        self.setWindowTitle('Координаты')
        layout = QVBoxLayout(self)
        self.circle_widget = CircleWidget()
        layout.addWidget(self.circle_widget)
        self.pushButton = QPushButton("Добавить окружность")
        layout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.circle_widget.button_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())