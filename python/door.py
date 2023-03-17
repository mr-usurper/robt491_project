import os
from dynamixel_sdk import * 

flag = 0


def opening(flag):
    if os.name == 'nt':
        import msvcrt
        def getch():
            return msvcrt.getch().decode()
    else:
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        def getch():
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

                       # Uses Dynamixel SDK library

    # Control table address
    ADDR_PRO_TORQUE_ENABLE      = 512              # Control table address is different in Dynamixel model
    ADDR_PRO_GOAL_POSITION      = 564
    ADDR_PRO_PRESENT_POSITION   = 580
    ADDR_PRO_GOAL_VELOCITY      = 552
    ADDR_PRO_PRESENT_VELOCITY   = 576
    ADDR_PRO_OPERATING_MODE     = 11;
    # Protocol version
    PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel
    #value for 7.5 mm = 3700000
    #value for each iteration = 74000
    # Default setting
    DXL_ID_2                      = 2
    DXL_ID_1                      = 1               # Dynamixel ID : 1
    BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
    DEVICENAME                  = "/dev/ttyUSB0"    # Check which port is being used on your controller
                                                    # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

    TORQUE_ENABLE               = 1                 # Value for enabling the torque
    TORQUE_DISABLE              = 0                 # Value for disabling the torque



    # Initialize PortHandler instance
    # Set the port path
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    portHandler = PortHandler(DEVICENAME)

    # Initialize PacketHandler instance
    # Set the protocol version
    # Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
    packetHandler = PacketHandler(PROTOCOL_VERSION)

    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()


    # Set port baudrate
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()

    # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel has been successfully connected")


    # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel has been successfully connected")



    DXL_MINIMUM_POSITION_VALUE  =0     # Dynamixel will rotate between this value
    DXL_MAXIMUM_POSITION_VALUE_right  =-606908      # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
    DXL_MAXIMUM_POSITION_VALUE_left  =-606908
    DXL_MOVING_STATUS_THRESHOLD = 100
    DXL_MINIMUM_POSITION_VALUE_2  =0     # Dynamixel will rotate between this value
    DXL_MAXIMUM_POSITION_VALUE_2_right  =-74000
    DXL_MAXIMUM_POSITION_VALUE_2_left  =74000    # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
    DXL_MOVING_STATUS_THRESHOLD_2 = 100              # Dynamixel moving status threshold
    turns=1
    index = 0
    #dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]
    dxl_zero_position =0        # Goal position
    dxl_step=74000
    #0.1744
    #260


    # Change operating mod
    EXT_POSITION_CONTROL_MODE = packetHandler.read1ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_OPERATING_MODE)
    EXT_POSITION_CONTROL_MODE = packetHandler.read1ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_OPERATING_MODE)



    counter_while_one=0
    counter_while_two=1

    counter_while_one_2=0


    counter_back_one=0
    counter_back_two=0
    #for i in range(1,int(number    _of_directions+1)):

    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_PRESENT_POSITION)
    if flag == 1:
        print ("main while")
        while  (dxl_present_position!=151727 and dxl_present_position!=-151727):
            # Write goal position for motor 1
            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_GOAL_POSITION,151727)
            #print("wrote to motor station", DXL_MAXIMUM_POSITION_VALUE_2_right*counter_back_one, "rotations")
            #print("wrote to drive motor mandrine", counter_while_two_2, "rotations")
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            counter_while_one_2=counter_while_one_2+1

            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_GOAL_POSITION, -151727)
            #print("wrote to motor station", DXL_MAXIMUM_POSITION_VALUE_2_right*counter_back_one, "rotations")
            #print("wrote to drive motor mandrine", counter_while_two_2, "rotations")
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            while 1:
                # Read present position for motor 1
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_PRESENT_POSITION)
                if (dxl_present_position> 0):
                    dxl_present_position = dxl_present_position-2**32
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_PRESENT_POSITION)
                if (dxl_present_position> 0):
                    dxl_present_position = dxl_present_position-2**32
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

                
                if  (abs( 151727 + dxl_present_position) < DXL_MOVING_STATUS_THRESHOLD_2):

                    break
                dxl_present_position=151727

    elif flag == 2:
        while  (dxl_present_position!=0):
            # Write goal position for motor 1
            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_GOAL_POSITION, 0)

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            counter_while_one_2=counter_while_one_2+1

            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_GOAL_POSITION, 0)

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            while 1:
                # Read present position for motor 1
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_PRESENT_POSITION)
                if (dxl_present_position> 0):
                    dxl_present_position = dxl_present_position-2**32
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_PRESENT_POSITION)
                if (dxl_present_position> 0):
                    dxl_present_position = dxl_present_position-2**32
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

                if  (abs( 0 + dxl_present_position) < DXL_MOVING_STATUS_THRESHOLD_2):
                    break
        

    # Disable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_1, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_2, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


    dxl_comm_result, dxl_error = packetHandler.reboot(portHandler, DXL_ID_1)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    #print("[ID:%03d] reboot Succeeded\n" % DXL_ID_1)

    dxl_comm_result, dxl_error = packetHandler.reboot(portHandler, DXL_ID_2)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    # Close port
    portHandler.closePort()

if __name__ == '__main__':
    opening(2)
