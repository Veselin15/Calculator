import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(500, 500, 500, 500)
        self.initUI()

    def initUI(self):
        self.btn_7 = QtWidgets.QPushButton(self)
        self.btn_7.setText("7")
        self.btn_7.move(30, 70)
        self.btn_7.resize(70, 50)
        self.btn_7.clicked.connect(lambda: self.number_pressed(7))

        self.btn_8 = QtWidgets.QPushButton(self)
        self.btn_8.setText("8")
        self.btn_8.move(110, 70)
        self.btn_8.resize(70, 50)
        self.btn_8.clicked.connect(lambda: self.number_pressed(8))

        self.btn_9 = QtWidgets.QPushButton(self)
        self.btn_9.setText("9")
        self.btn_9.move(190, 70)
        self.btn_9.resize(70, 50)
        self.btn_9.clicked.connect(lambda: self.number_pressed(9))

        self.btn_4 = QtWidgets.QPushButton(self)
        self.btn_4.setText("4")
        self.btn_4.move(30, 130)
        self.btn_4.resize(70, 50)
        self.btn_4.clicked.connect(lambda: self.number_pressed(4))

        self.btn_5 = QtWidgets.QPushButton(self)
        self.btn_5.setText("5")
        self.btn_5.move(110, 130)
        self.btn_5.resize(70, 50)
        self.btn_5.clicked.connect(lambda: self.number_pressed(5))

        self.btn_6 = QtWidgets.QPushButton(self)
        self.btn_6.setText("6")
        self.btn_6.move(190, 130)
        self.btn_6.resize(70, 50)
        self.btn_6.clicked.connect(lambda: self.number_pressed(6))

        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setText("1")
        self.btn_1.move(30, 190)
        self.btn_1.resize(70, 50)
        self.btn_1.clicked.connect(lambda: self.number_pressed(1))

        self.btn_2 = QtWidgets.QPushButton(self)
        self.btn_2.setText("2")
        self.btn_2.move(110, 190)
        self.btn_2.resize(70, 50)
        self.btn_2.clicked.connect(lambda: self.number_pressed(2))

        self.btn_3 = QtWidgets.QPushButton(self)
        self.btn_3.setText("3")
        self.btn_3.move(190, 190)
        self.btn_3.resize(70, 50)
        self.btn_3.clicked.connect(lambda: self.number_pressed(3))

        self.btn_0 = QtWidgets.QPushButton(self)
        self.btn_0.setText("0")
        self.btn_0.move(30, 250)
        self.btn_0.resize(70, 50)
        self.btn_0.clicked.connect(lambda: self.number_pressed(0))

        self.btn_addition = QtWidgets.QPushButton(self)
        self.btn_addition.setText("+")
        self.btn_addition.move(270, 250)
        self.btn_addition.resize(70, 50)
        self.btn_addition.clicked.connect(self.calculate)

        self.btn_subtraction = QtWidgets.QPushButton(self)
        self.btn_subtraction.setText("-")
        self.btn_subtraction.move(270, 190)
        self.btn_subtraction.resize(70, 50)
        self.btn_subtraction.clicked.connect(self.calculate)

        self.btn_multiplication = QtWidgets.QPushButton(self)
        self.btn_multiplication.setText("*")
        self.btn_multiplication.move(270, 130)
        self.btn_multiplication.resize(70, 50)
        self.btn_multiplication.clicked.connect(self.calculate)

        self.btn_division = QtWidgets.QPushButton(self)
        self.btn_division.setText("/")
        self.btn_division.move(270, 70)
        self.btn_division.resize(70, 50)
        self.btn_division.clicked.connect(self.calculate)

        self.btn_decimal = QtWidgets.QPushButton(self)
        self.btn_decimal.setText(".")
        self.btn_decimal.move(110, 250)
        self.btn_decimal.resize(70, 50)
        self.btn_decimal.clicked.connect(lambda: self.number_pressed("."))

        self.btn_result = QtWidgets.QPushButton(self)
        self.btn_result.setText("=")
        self.btn_result.move(190, 250)
        self.btn_result.resize(70, 50)
        self.btn_result.clicked.connect(self.calculate)

        self.txt_box = QtWidgets.QLabel(self)
        self.txt_box.setText("0")
        self.txt_box.move(10, 30)
        self.txt_box.resize(330, 50)
        self.txt_box.setAlignment(QtCore.Qt.AlignRight)

    def division_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText("Cannot divide by zero.")
        msg.setWindowTitle("Error")
        msg.exec_()
    def invalid_numbers_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText("Please enter valid numbers.")
        msg.setWindowTitle("Error")
        msg.exec_()

    def number_pressed(self, number):
        current_text = self.txt_box.text()
        if current_text == "0":
            self.txt_box.setText(str(number))
        else:
            self.txt_box.setText(current_text + str(number))

    def calculate(self):
        sender = self.sender()
        result = 0
        print(sender.text())

        if sender.text() == "+":
            try:
                number1 = float(self.txt_box.text())
            except ValueError:
                self.invalid_numbers_error()
                return
            number1 = float(self.txt_box.text())
            self.txt_box.setText("")
        if self.txt_box.text() == "=":
            try:
                number2 = float(self.txt_box.text())
            except ValueError:
                self.invalid_numbers_error()
                return
            number2 = float(self.txt_box.text())
            print(number2)
            result = number1 + number2
            print(result)
            self.txt_box.setText(str(result))



def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

app()