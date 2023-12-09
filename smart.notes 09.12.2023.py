from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem,
QLineEdit, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QTextEdit)

app=QApplication([])


window = QWidget()
window.setWindowTitle("Розумні замітки")
window.resize(900,600)
window.move(600,300)

text = QTextEdit()
text.setText("Це найкращий додаток")
notes1 = QLabel("Cписок заміток")
notes2 = QLabel("Список тегів")

but1 = QPushButton("Створити замітку")
but1.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")





but2 = QPushButton("Видалити замітку")
but3 = QPushButton("Зберегти замітки")
but4 = QPushButton("Додати до замітки")
but5 = QPushButton("Відкріпити від замітки")
but6 = QPushButton("Шукати зімітки по тегу")


items1 = QListWidget()
items2  =QListWidget()
line = QLineEdit()
line.setPlaceholderText("Введіть тег...")



line_mainH = QHBoxLayout()
line_V1 = QVBoxLayout()
line_V2 = QVBoxLayout()
line_H1 = QHBoxLayout()
line_H2 = QHBoxLayout()


line_V1.addWidget(text)
line_H1.addWidget(but1)
line_H1.addWidget(but2)
line_H2.addWidget(but4)
line_H2.addWidget(but5)

line_V2.addWidget(notes1)
line_V2.addWidget(items1)
line_V2.addLayout(line_H1)
line_V2.addWidget(but3)
line_V2.addWidget(notes2)
line_V2.addWidget(items2)
line_V2.addWidget(line)
line_V2.addLayout(line_H2)
line_V2.addWidget(but6)

line_mainH.addLayout(line_V1, stretch=2)
line_mainH.addLayout(line_V2, stretch=1)
window.setLayout(line_mainH)






window.show()
app.exec_()