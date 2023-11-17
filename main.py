import sys

from window import *

from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MillionDiceRoll()
    window.show()
    
    sys.exit(app.exec())
