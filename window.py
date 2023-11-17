import random,time
from PyQt6 import *
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QLineEdit, QWidget, QVBoxLayout

class MillionDiceRoll(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MillionDiceRoll')
        self.setGeometry(100, 100, 230, 280)

        self.init_ui()
        self.button_event()

    def init_ui(self):
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Введите количество кубиков...')

        self.button = QPushButton("Сделать 1кк бросков",self)
        self.button.setStyleSheet("background-color: rgb(0, 128, 0); color: white;")

        self.field_to_see_answer = QTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        layout.addWidget(self.field_to_see_answer)
    
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        central_widget.setStyleSheet("background-color: rgb(192, 192, 192);")

    def check_field(self) -> bool:
        txt = self.input_field.text().strip()

        if txt == '':
            self.errors('Поле должно содержать число')
            return False    
        
        elif len(txt.split()) > 1:
            self.errors('В поле не должно быть больше одного числа')
            return False

        elif not txt.isdigit():
            self.errors('В поле должны быть только числа')
            return False
        
        return True

    def errors(self,error_msg:str ):
        self.field_to_see_answer.setStyleSheet('color: red;')
        self.field_to_see_answer.setText(error_msg)


    def button_event(self):
        self.button.clicked.connect(self.simulation)

    def simulation(self):

        if not self.check_field():
            return 0

        numberOfDice = int(self.input_field.text())
        # Set up a dictionary to store the results of each dice roll:
        results = {}
        for i in range(numberOfDice, (numberOfDice * 6) + 1):
            results[i] = 0

        # Simulate dice rolls:
        lastPrintTime = time.time()
        for i in range(1000000):
            if time.time() > lastPrintTime + 1:
                lastPrintTime = time.time()

            total = 0
            for j in range(numberOfDice):
                total = total + random.randint(1, 6)
            results[total] = results[total] + 1

        # Display results:
        tr = ''
        for i in range(numberOfDice, (numberOfDice * 6) + 1):
            roll = results[i]
            percentage = round(results[i] / 10000, 1)
            tr += f'<tr><td style="border: 1px solid; padding: 3px;">{i}</td><td style="border: 1px solid; padding: 3px;">{roll}</td><td style="border: 1px solid; padding: 3px;">{percentage}%</td></tr>'

        answer = f"""
                <html>
                    <table>
                        <tr>
                            <th style="border: 1px solid; padding: 3px;">TOTAL</th>
                            <th style="border: 1px solid; padding: 3px;">ROLLS</th>
                            <th style="border: 1px solid; padding: 3px;">PERCENTAGE</th>
                        </tr>
                       {tr}
                    </table>
                </html>
                """

        self.field_to_see_answer.setHtml(answer)
    

        
