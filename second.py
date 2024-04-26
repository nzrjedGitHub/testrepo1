from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("logikaYear")
main_win.resize(400, 200)

question = QLabel('в якому році була замнована Логіка')
winner = QLabel('?')
btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')
layout_main = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

# line.addWidget(winner, alignment = Qt.AlignCenter)

main_win.setLayout(layout_main)


main_win.show()
app.exec_()
