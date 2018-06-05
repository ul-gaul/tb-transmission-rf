
import sys
import serial


if __name__ == '__main__':
    baud = 9600
    port = sys.argv[1]
    with serial.Serial(port, baud) as ser:
        while True:
            s = input("gimme da string")
            ser.write(s.encode())
