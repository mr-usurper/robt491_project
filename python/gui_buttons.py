import sys
import logging
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import *
import connection_v2

logging.basicConfig(filename="logfile.txt",
                    format='%(levelname)-8s %(asctime)s %(message)s ',
                    filemode='w', datefmt="%d/%m/%Y %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Overweight")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Your parcel is overweight, pay up")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def b1_clicked(self):
        self.message("Scanning a parcel.")
        logger.info("Scanning a parcel.")

        if self.editor.text() == 'asdf':
            self.label2.setText("Opening door, weighting parcel")

            self.message("The parcel is in DB.")
            logger.info("The parcel is in DB.") 

        else:
            self.label2.setText("No such parcel in DB")

            self.message("No such parcel in DB.")
            logger.info("No such parcel in DB.")
        self.update()

    
    def b2_clicked(self):
        self.message("Weighting parcels.")
        logger.info("Weighting parcels.") 

        if self.editor2.text() == '1kg':
            self.label2.setText("The weight is 1kg")

            self.message("The weight is correct.")
            logger.info("The weight is correct.") 
        else:
            self.label2.setText("The parcel is overweight")

            self.message("The parcel is overweight.")
            logger.warning("The parcel is overweight.") 

            CustomDialog().exec()
        self.update()
    
    def b3_clicked(self):
        data = connection_v2.readserial()
        self.label.setText(str(data))
        
        while data == 13:
            data = connection_v2.readserial()
            self.label.setText(str(data))
            self.message("Waiting for parcel.")
            logger.info("Waiting for parcel.") 
            print("13")
            self.label2.setText("Waiting for parcel.")
        
        
        while data == 69:
            data = connection_v2.readserial()
            self.label.setText(str(data))
            self.message("Starting process.")
            logger.info("Starting process.") 
            print("69")
            self.label2.setText("Starting process")

    def message(self, s):
        self.text.appendPlainText(s)

    def initUI(self):
        self.setGeometry(500, 400, 1000, 1000)
        self.setWindowTitle("Logistic Box")
        self.setFixedSize(QSize(800, 500))

        self.text = QPlainTextEdit(self) #logging
        self.text.setReadOnly(True)
        self.text.move(525, 50)
        self.text.adjustSize()
        self.text.resize(225, 330)

        self.editor = QtWidgets.QLineEdit(self)
        self.editor.move(50, 50)
        self.editor.setFont(QFont('Arial', 18))
        self.editor.resize(225, 40)

        self.editor2 = QtWidgets.QLineEdit(self)
        self.editor2.move(50, 150)
        self.editor2.setFont(QFont('Arial', 18))
        self.editor2.resize(225, 40)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(325, 50)
        self.b1.setFont(QFont('Arial', 18))
        self.b1.setText("Scanner")
        self.b1.clicked.connect(self.b1_clicked)
        self.b1.resize(150, 40)
        self.b1.setStyleSheet("QLabel::hover"
                            "{"
                            "background-color : lightgreen;"
                            "}")
        
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(325, 150)
        self.b2.setFont(QFont('Arial', 18))
        self.b2.setText("Weight")
        self.b2.clicked.connect(self.b2_clicked)
        self.b2.resize(150, 40)
    

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(325, 250)
        self.b3.setFont(QFont('Arial', 18))
        self.b3.setText("Start")
        self.b3.clicked.connect(self.b3_clicked)
        self.b3.resize(150, 40)
        self.b3.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )

        self.label = QtWidgets.QLabel(self)
        self.label.setText("State of the process:")
        self.label.setFont(QFont('Arial', 18))
        self.label.move(50, 255)
        self.label.adjustSize()
        #self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Waiting for scan")
        self.label2.setFont(QFont('Arial', 20))
        self.label2.move(50, 340)
        self.label2.adjustSize()
        self.label2.resize(425, 40)
        self.label2.setStyleSheet("border: 1px solid black;")

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("1")
        self.label3.move(750,450)
        self.label3.adjustSize()
        

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
