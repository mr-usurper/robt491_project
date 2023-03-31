from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time, threading

global ser
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0.1
                    #parity=serial.PARITY_NONE,
                    #stopbits=serial.STOPBITS_ONE,
                    #bytesize=serial.EIGHTBITS
                    )

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 211, 41))
        
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.labelDistance = QtWidgets.QLabel(self.centralwidget)
        self.labelDistance.setGeometry(QtCore.QRect(60, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.labelDistance.setFont(font)
        self.labelDistance.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDistance.setObjectName("labelDistance")
        #self.labelcm = QtWidgets.QLabel(self.centralwidget)
        #self.labelcm.setGeometry(QtCore.QRect(120, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        #self.labelcm.setFont(font)
        #self.labelcm.setAlignment(QtCore.Qt.AlignCenter)
        #self.labelcm.setObjectName("labelcm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label2 = QtWidgets.QLineEdit(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(400, 50, 211, 41))
        self.label2.setFont(font)
        #self.label2.setObjectName("label2")
        self.label2.setText("waiting")
        self.label2.textChanged(self.onChange)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onChange(self):
        print("changed")
        #self.label2.setText(text)
        self.label2.adjustSize()


    def retranslateUi(self, MainWindow):
        print("retranslate")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logistic Box"))
        self.label.setText(_translate("MainWindow", "Arduino Data"))
        self.labelDistance.setText(_translate("MainWindow", "0"))
        #self.labelcm.setText(_translate("MainWindow", "cm"))
        # User Code
        self.timeout = 0
        self.check_serial_event()

    '''
    def check_serial_event(self):
        print("serial")
        self.timeout += 1
        print (self.timeout)
        serial_thread = threading.Timer(1, self.check_serial_event)
        if ser.is_open == True:
            serial_thread.start()
            if ser.in_waiting:

                data = ser.readline().decode().strip()
                    
                distance = data
                self.labelDistance.setText(distance)
                # print (distance)
                self.timeout = 0

        if self.timeout >= 3:
            ser.close()
    '''

    
    def check_serial_event(self):
        self.timeout += 1
        #print (self.timeout)
        serial_thread = threading.Timer(1, self.check_serial_event)
        if ser.is_open == True:
            serial_thread.start()
            if ser.in_waiting:
                eol = b'\n'
                leneol = len(eol)
                line = bytearray()
                while True:
                    c = ser.read(1)
                    #print(c)
                    if c:
                        line += c
                        if line[-leneol:] == eol:
                            break
                    else:
                        break
                    # print (line)
                    # print (type(line))
                line = line.rstrip()
                distance = line.decode("utf-8")
                self.labelDistance.setText(distance)
                # print (distance)
                self.timeout = 0

        if self.timeout >= 3:
            ser.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
