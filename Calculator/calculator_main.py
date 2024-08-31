import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(300, 300, 300, 300)
        self.initUI()

    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number1")
        self.lbl_number1.move(10, 20)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(100, 20)
        self.txt_number1.resize(100, 32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText("Number2")
        self.lbl_number2.move(10, 60)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(100, 60)
        self.txt_number2.resize(100, 32)

        self.btn_addition = QtWidgets.QPushButton(self)
        self.btn_addition.setText("+")
        self.btn_addition.move(30, 100)
        self.btn_addition.clicked.connect(self.calculate)

        self.btn_subtraction = QtWidgets.QPushButton(self)
        self.btn_subtraction.setText("-")
        self.btn_subtraction.move(150, 100)
        self.btn_subtraction.clicked.connect(self.calculate)

        self.btn_multiplication = QtWidgets.QPushButton(self)
        self.btn_multiplication.setText("*")
        self.btn_multiplication.move(30, 150)
        self.btn_multiplication.clicked.connect(self.calculate)

        self.btn_division = QtWidgets.QPushButton(self)
        self.btn_division.setText("/")
        self.btn_division.move(150, 150)
        self.btn_division.clicked.connect(self.calculate)


        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(10, 200)
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

    def calculate(self):
        sender = self.sender()
        result = 0
        print(sender.text())
        try:
            number1 = float(self.txt_number1.text())
            number2 = float(self.txt_number2.text())
        except ValueError:
            self.invalid_numbers_error()
            return

        if sender.text() == "/" and float(self.txt_number2.text()) == 0:
            self.division_errorMessage()




        if sender.text() == "+":
            result = float(self.txt_number1.text()) + float(self.txt_number2.text())
        elif sender.text() == "-":
            result = float(self.txt_number1.text()) - float(self.txt_number2.text())
        elif sender.text() == "*":
            result = float(self.txt_number1.text()) * float(self.txt_number2.text())
        elif sender.text() == "/":
            result = float(self.txt_number1.text()) / float(self.txt_number2.text())




        self.lbl_result.setText(f"Result: {str(result)}")

def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

app()