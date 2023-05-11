import sys
import logging
import csv
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from PyQt5.QtGui import *
import door
 
logging.basicConfig(filename="logfile.txt",
                    format='%(levelname)-8s %(asctime)s %(message)s ',
                    filemode='w', datefmt="%d/%m/%Y %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
 
serial = QSerialPort()
serial.setBaudRate(9600)
serial.setPortName('COM10')
global process  
global weight
global Rdata
Rdata = [0,0]
process = 0
weight = 0
 
 
 
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
        global weightR
        weightR = 3
        self.initUI()
        self.buffer = ""
        serial.open(QIODevice.ReadWrite)
        serial.readyRead.connect(self.onRead)        
        # read CSV file and store the data in a dictionary
        self.data = {}
        with open('baza.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name = row[0]
                codes = row[1].split('|')
                weight = row[2]
                self.data[name] = {'codes': codes, 'weight': weight}
 
        print(self.data)  
 
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            # split the scanned data by '|' character
            name, code = self.buffer.split('|')
            self.findData(name, code)
            self.buffer = ""
        else:
            self.buffer += event.text()
 
    def findData(self, name, code):
 
 
 
        global Rdata
        global weightR
        sumWeight = 0
        # check if the name exists in the data dictionary
        if name in self.data:
            codes = self.data[name]['codes']
            weight = int(self.data[name]['weight'])
 
            if code in codes:
                codes.remove(code)
                print(f"Code {code} found for product {name} {len(codes)} left")
                self.label2.setText(f"{len(codes)} left")
                door.opening(1)
                scale = 0
                if int(Rdata[1]) > 300 and int(Rdata[1]) < 1000:
                        sumWeight = int(Rdata[1])+sumWeight
                        print(sumWeight)
                        scale == 1
                if len(codes) == 0:
                    print(f"All codes for product {name} have been scanned")
                    self.label2.setText("All codes are scanned")
                    weightR = 0
                    if weight < sumWeight:
                        print("pay nigga")
                    else:
                        print("nigga u aight")
 
            else:
                print(f"Code {code} not found for product {name}")
        else:
            print(f"Product {name} not found in the database")
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
        print("test")
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
 
 
        self.update()
 
 
    def b3_clicked(self):
        print("started")
        serial.open(QIODevice.ReadWrite)
        serial.readyRead.connect(self.onRead)
        print("set up")
 
 
    def onRead(self):
        global weightR
        global Rdata
        #print("onRead")
 
        if not serial.canReadLine(): return     # ������� ���� ������ ������
        rx = serial.readLine()
        rxs = str(rx, 'utf-8').strip()
        try:
            Rdata = rxs.split(',')  
        except:
            print("ket nahu")
        #print(rxs) 
        print(Rdata)
 
        #print(data[1])
 
        if weightR == 0:
            if int(Rdata[1]) < 300 and int(Rdata[1]) > 1000:
                self.label2.setText("weight the parcel.")
                self.message("weight the parcel.")
                logger.warning("weight the parcel.") 
                weightR = 0
 
            elif int(Rdata[1]) > 300 and int(Rdata[1]) < 600:
                self.label2.setText("the weight is correct.")
                self.message("the weight is correct.")
                logger.info("the weight is correct.")
                weightR = 1
 
            elif int(Rdata[1]) > 600 and int(Rdata[1]) < 1000:
                self.label2.setText("the parcel is overweight.")
                self.message("the parcel is overweight.")
                logger.warning("the parcel is overweight.") 
                weightR = 2
                customdialog().exec()
 
        elif weightR == 1:
            if Rdata[0] == '1313':
                self.label2.setText("no parcel.")
                self.message("no parcel.")
                logger.info("no parcel.")
        if Rdata[0] == '6969':
                door.opening(2)
                self.label2.setText("Process started.")
                self.message("Process started.")
                logger.info("Process started.")
 
        elif Rdata[0] == '7777':
                self.label2.setText("Package sorted.")
                self.message("Package sorted.")
                logger.info("Package sorted.")
 
 
    def message(self, s):
        self.text.appendPlainText(s)
 
    def initUI(self):
 
        self.setGeometry(300, 300, 1500, 1500)
        self.setWindowTitle("Logistic Box")
        self.setFixedSize(QSize(1200, 800))
 
        self.text = QPlainTextEdit(self) #logging
        self.text.setReadOnly(True)
        self.text.move(525, 50)
        self.text.adjustSize()
        self.text.resize(225, 330)
        '''
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
        '''
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
 
process = 0
weight = 0
door.opening(2)
window()
