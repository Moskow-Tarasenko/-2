import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt, QRectF
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Загрузка интерфейса из файла UI.ui
        loadUi('UI.ui', self)

        # Настройка компонентов PyQT
        self.pushButton.clicked.connect(self.drawRandomCircle)

        # Настройка элементов для рисования
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def drawRandomCircle(self):
        # Генерация случайных параметров для окружности
        diameter = random.randint(10, 100)
        color = QColor(Qt.yellow)

        # Рисование окружности на сцене
        self.scene.addEllipse(self.getRandomPosition(diameter), QRectF(0, 0, diameter, diameter),
                               pen=QtGui.QPen(color), brush=QtGui.QBrush(color))

    def getRandomPosition(self, diameter):
        # Генерация случайной позиции для размещения окружности
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)
        return QRectF(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
