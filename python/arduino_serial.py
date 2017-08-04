import serial

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()
while True:
    if (serialFromArduino.inWaiting() > 0):
        input = serialFromArduino.read(1)
        print(str(ord(input)) + " = the ASCII character " + str(input) + ".")
