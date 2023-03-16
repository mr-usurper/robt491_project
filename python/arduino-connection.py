import serial
#import keyboard

item = int(0);
value1 = 0;
value2 = 0;
thresh1 = 50;
thresh2 = 50;



def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)

    while True:
        data = ser.readline().decode().strip()
        if data:
            try:
                dataint = int(data)
                if dataint == 13:
                    print("No parcel on conveyor")
                    break
                elif dataint == 69:
                    print("The process is running")
                    break
                elif dataint == 77:
                    print("Parcel is stored")
                    break

            except ValueError:
                print("Data is not a valid integer")

if __name__ == '__main__':
    readserial('/dev/ttyACM0', 9600)


'''
if item == 0:
    if value1 > thresh1:
        print("no item")
    elif value1 < thresh1:
        print("SAW ITEM")
elif item == 1:
    if value2 > thresh2:
        print("RUN")
    elif value2 < thresh2:
        print("DONE DEAL")
elif item == 2:
    print("no item")
    
'''
