"""
My pysideApp
"""
import sys
from PySide2 import QtWidgets


class papodedev(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('meu_bee_app')
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = papodedev()
    sys.exit(app.exec_())
