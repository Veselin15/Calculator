import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(500, 500, 500, 500)
        self.initUI()
        self.current_operator = None
        self.first_number = None
        self.is_waiting_for_second_number = False

    def initUI(self):
        # Numbers
        self.btn_7 = self.create_button("7", 30, 70, self.number_pressed)
        self.btn_8 = self.create_button("8", 110, 70, self.number_pressed)
        self.btn_9 = self.create_button("9", 190, 70, self.number_pressed)
        self.btn_4 = self.create_button("4", 30, 130, self.number_pressed)
        self.btn_5 = self.create_button("5", 110, 130, self.number_pressed)
        self.btn_6 = self.create_button("6", 190, 130, self.number_pressed)
        self.btn_1 = self.create_button("1", 30, 190, self.number_pressed)
        self.btn_2 = self.create_button("2", 110, 190, self.number_pressed)
        self.btn_3 = self.create_button("3", 190, 190, self.number_pressed)
        self.btn_0 = self.create_button("0", 30, 250, self.number_pressed)
        self.btn_decimal = self.create_button(".", 110, 250, self.number_pressed)

        # Operations
        self.btn_addition = self.create_button("+", 270, 250, self.operation_pressed)
        self.btn_subtraction = self.create_button("-", 270, 190, self.operation_pressed)
        self.btn_multiplication = self.create_button("*", 270, 130, self.operation_pressed)
        self.btn_division = self.create_button("/", 270, 70, self.operation_pressed)
        self.btn_result = self.create_button("=", 190, 250, self.calculate)

        # Display
        self.txt_box = QtWidgets.QLabel(self)
        self.txt_box.setText("0")
        self.txt_box.move(10, 30)
        self.txt_box.resize(330, 50)
        self.txt_box.setAlignment(QtCore.Qt.AlignRight)

    def create_button(self, text, x, y, handler):
        btn = QtWidgets.QPushButton(self)
        btn.setText(text)
        btn.move(x, y)
        btn.resize(70, 50)
        btn.clicked.connect(handler)
        return btn

    def division_error(self):
        self.show_error_message("Cannot divide by zero.")

    def invalid_numbers_error(self):
        self.show_error_message("Please enter valid numbers.")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def number_pressed(self):
        sender = self.sender()
        number = sender.text()

        if self.is_waiting_for_second_number:
            self.txt_box.setText(number)
            self.is_waiting_for_second_number = False
        else:
            current_text = self.txt_box.text()
            if current_text == "0":
                self.txt_box.setText(number)
            else:
                self.txt_box.setText(current_text + number)


    def operation_pressed(self):
        sender = self.sender()
        self.first_number = float(self.txt_box.text())
        self.current_operator = sender.text()
        self.is_waiting_for_second_number = True

    def calculate(self):
        if not self.first_number or not self.current_operator:
            return

        second_number = float(self.txt_box.text())

        try:
            if self.current_operator == "+":
                result = self.first_number + second_number
            elif self.current_operator == "-":
                result = self.first_number - second_number
            elif self.current_operator == "*":
                result = self.first_number * second_number
            elif self.current_operator == "/":
                if second_number == 0:
                    self.division_error()
                    return
                result = self.first_number / second_number
            else:
                self.invalid_numbers_error()
                return

            self.txt_box.setText(str(result))
            self.first_number = result
            self.current_operator = None
            self.is_waiting_for_second_number = True

        except Exception as e:
            self.invalid_numbers_error()

def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

app()
