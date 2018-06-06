import serial
import sys

if __name__ == "__main__":
    ser=serial.Serial(sys.argv[1],9600, bytesize = 8, parity = "N", stopbits = 1, xonxoff = 0, rtscts =0)
    while True:
        c=ser.read()
        print(c)
        print(c.decode())

