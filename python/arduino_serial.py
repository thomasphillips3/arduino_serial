import serial, sys

if (len(sys.argv) != 2):
    print ("Usage: python arduino_serial.py port")
    sys.exit()

port = sys.argv[1]
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()
while True:
    input = serialFromArduino.readline()
    inputAsInteger = int(input)
    print(inputAsInteger * 1)
