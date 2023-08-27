import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrecyConv(QtWidgets.QMainWindow):

    def __init__(self):
        super(CurrecyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def  init_UI(self):
        self.setWindowTitle('Converter')
        self.setWindowIcon((QIcon('open.png')))

        self.ui.input_cur.setPlaceholderText('From what currency?')
        self.ui.input_count.setPlaceholderText('Count')
        self.ui.output_cur.setPlaceholderText('In what currency?')
        self.ui.output_count.setPlaceholderText('Count')
        self.ui.convert.clicked.connect(self.converter)


    def converter(self):
        c = CurrencyConverter()
        input_cur = self.ui.input_cur.text()
        input_count = int(self.ui.input_count.text())
        output_cur = self.ui.output_cur.text()
        output_count = c.convert(input_count, input_cur, output_cur)

        self.ui.output_count.setText(str(output_count))




app = QtWidgets.QApplication([])
application = CurrecyConv()
application.show()

sys.exit(app.exec())




