import connection_v2
import serial
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt, QSize, QProcess
import keyboard
import door2
import time

def barCode():
    input_str = ""
    while True:
        event = keyboard.read_event()
        if event.name == 'enter':
            break
        elif event.event_type == 'down':
            input_str += event.name.replace("down", "")
    return input_str

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

    def message(self, s):
        self.text.appendPlainText(s)

    def b3_clicked(self):
        self.message("Executing process.")
        self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.start("python3", ['/home/lenovo/Downloads/ROBT/491/program/python/gui/connection_v2.py'])
        self.update()
        
 
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)
        

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)
        self.label.setText(stdout)
        self.update()

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")
        

    def b4_clicked(self):
        data=connection_v2.readserial()
        self.label.setText(str(data))
        if data == 69:
            door2.opening(2)

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
        self.editor.setText(input)
        

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("State of the process:")
        self.label2.move(50,150)
        self.label2.adjustSize()
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Waiting for scan")
        self.label.move(50,200)
        self.label.adjustSize()
        

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(590, 50)
        self.b3.setText("ARDUINO")
        self.b3.clicked.connect(self.b3_clicked)
        self.b3.adjustSize()

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.move(300, 50)
        self.b4.setText("button")
        self.b4.clicked.connect(self.b4_clicked)
        self.b4.adjustSize()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    input = ""
    while(input != "4870001157913"):
        input = barCode()
        print(input)
        if input == "4870001157913":
            print("nia accepted")
        else:
            print("wrong nia")
            input = ""
    door2.opening(1)
    time.sleep(1)
    door2.opening(2)

    window()
    
