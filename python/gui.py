import connection_v2
import serial
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt, QSize, QProcess

class CustomDialog(QDialog):
    def __init__(self):
        
        super().__init__()

        #self.p = None  # Default empty value.

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

    '''
    def b1_clicked(self):
        if self.editor.text() == 'asdf':
            #print("wow")
            self.label.setText("Scanned, opening the door, weighting the parcel")
        else:
            self.label.setText("No such parcel in DB")
        self.update()

    def b2_clicked(self):
        if self.editor2.text() == '1kg':
            self.label.setText("The weight is 1kg")
        else:
            self.label.setText("The parcel is overweight")
            CustomDialog().exec()
        self.update()
    '''

    def message(self, s):
        self.text.appendPlainText(s)

    def b3_clicked(self):
        self.message("Executing process.")
        self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.start("python3", ['/home/lenovo/Downloads/ROBT/491/program/python/gui/connection_v2.py'])
 
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)
        

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)
        self.label.setText(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def initUI(self):
        self.setGeometry(500, 500, 1000, 1000)
        self.setWindowTitle("Logistic Box")
        self.setFixedSize(QSize(1000, 500))

        self.text = QPlainTextEdit(self)
        self.text.setReadOnly(True)
        self.text.move(500, 150)
        self.text.adjustSize()

        self.editor = QtWidgets.QLineEdit(self)
        self.editor.move(50, 50)
        self.editor.adjustSize()

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("State of the process:")
        self.label2.move(50,150)
        self.label2.adjustSize()
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Waiting for scan")
        self.label.move(50,200)
        self.label.adjustSize()

        '''
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(50, 125)
        self.b1.setText("Scanner")
        self.b1.clicked.connect(self.b1_clicked)
        self.b1.adjustSize()
        
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(400, 125)
        self.b2.setText("Weight")
        self.b2.clicked.connect(self.b2_clicked)
        self.b2.adjustSize()
        '''

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(590, 50)
        self.b3.setText("ARDUINO")
        self.b3.clicked.connect(self.b3_clicked)
        self.b3.adjustSize()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
    connection_v2.readserial(comopert, daue)
    
    
