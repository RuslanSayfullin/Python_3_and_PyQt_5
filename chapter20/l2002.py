# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()            # Родительский компонент — окно
window.setWindowTitle("QHBoxLayout")
window.resize(300, 60)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
hbox = QtWidgets.QHBoxLayout()          # Создаем контейнер
# Добавляем компоненты
hbox.addWidget(button1)
hbox.addWidget(button2)
# Передаем ссылку родителю
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())
