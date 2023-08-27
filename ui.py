# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 357)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 34, 46);\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 391))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 721, 111))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(730, 20, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/open_in_full_FILL0_wght600_GRAD200_opsz48.png"))
        self.label_2.setObjectName("label_2")
        self.input_cur = QtWidgets.QLineEdit(self.frame)
        self.input_cur.setGeometry(QtCore.QRect(390, 100, 380, 30))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.input_cur.setFont(font)
        self.input_cur.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 2px solid #0055ff;\n"
"border-radius: 10px;\n"
"color: white;")
        self.input_cur.setText("")
        self.input_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.input_cur.setObjectName("input_cur")
        self.input_count = QtWidgets.QLineEdit(self.frame)
        self.input_count.setGeometry(QtCore.QRect(390, 152, 380, 30))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.input_count.setFont(font)
        self.input_count.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 2px solid #0055ff;\n"
"border-radius: 10px;\n"
"color: white;")
        self.input_count.setText("")
        self.input_count.setAlignment(QtCore.Qt.AlignCenter)
        self.input_count.setObjectName("input_count")
        self.output_cur = QtWidgets.QLineEdit(self.frame)
        self.output_cur.setGeometry(QtCore.QRect(390, 207, 380, 30))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.output_cur.setFont(font)
        self.output_cur.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 2px solid #0055ff;\n"
"border-radius: 10px;\n"
"color: white;")
        self.output_cur.setText("")
        self.output_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.output_cur.setObjectName("output_cur")
        self.output_count = QtWidgets.QLineEdit(self.frame)
        self.output_count.setGeometry(QtCore.QRect(390, 260, 380, 30))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.output_count.setFont(font)
        self.output_count.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 2px solid #0055ff;\n"
"border-radius: 10px;\n"
"color: white;")
        self.output_count.setText("")
        self.output_count.setAlignment(QtCore.Qt.AlignCenter)
        self.output_count.setObjectName("output_count")
        self.convert = QtWidgets.QPushButton(self.frame)
        self.convert.setGeometry(QtCore.QRect(392, 310, 380, 30))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.convert.setFont(font)
        self.convert.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 112);\n"
"border-radius: 10;\n"
"\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"\n"
"    background-color: rgb(0, 0, 128);\n"
"\n"
"}")
        self.convert.setObjectName("convert")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Currency converter (at the rate of the Central Bank of Turkmenistan)"))
        self.convert.setText(_translate("MainWindow", "Convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
