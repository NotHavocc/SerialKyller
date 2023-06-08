import serial
import io
import keyboard
import sys
from time import sleep

print("SerialKyller CLI | Release V1.0")

while True:
    term = input(">>> ")
    if term == "info":
        print("SerialKyller by NotHavoc")
    if term == "serSetup":
        port = input("Insert serial port (number): ")
        baud = input("Insert baud rate:")
        ser = serial.Serial("COM"+str(port), int(baud))
        print("Succesfully connected to port COM", str(port), "with baud rate of" ,int(baud))
    if term == "serPorts":
        try:
            ser
        except NameError:
            print("No ports open.")
        else:
            print(ser.baudrate)
            print(ser.port)
    if term == "serWrite":
        write = (int(input("What do you want to write? (int): ")))
        ser.write(int.to_bytes(write))
    if term == "serWriteByte":
        writestr = (str(input("What do you want to write? (byte): ")))
        writebyte = bytes(writestr, 'utf-8')
        ser.writelines(writebyte)
    if term == "serMonitor":
        conf = input("Are you sure? (Y/N) (Exit by pressing Q): ").capitalize()
        if conf == "Y":
            loop = 1
            while loop == 1:
                if ser.in_waiting > 0:
                        print(ser.readline())
                        if loop == 1 & keyboard.is_pressed("q"):
                            loop = 0
    if term == "serOff":
        print("Succesfully closed port COM", str(port))
        ser.close()
    if term == "exit":
        sys.exit()
    if term == "serHelp":
        print("type serSetup to begin the setup process.")
        print("***COMMANDS***")
        print("info = Shows info of application")
        print("serPorts = Shows which port is FREESHELL4SERIAL connected to and the baud rate")
        print("serWrite = Sends an integer to the connected port")
        print("serMonitor = Displays what the serial device is sending in string format")
        print("serOff = Disconnects the serial port")
        print("quit = Quits application")
        print("*** MADE WITH LOVE BY NOTHAVOC!!! ***")
        # serial.serialutil.SerialException
            








