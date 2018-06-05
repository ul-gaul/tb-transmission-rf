#!/usr/bin/env python3


import sys
import serial


if __name__ == '__main__':
    baud = 9600
    port = sys.argv[1]
    ser = serial.Serial(port, baud)
    while True:
        s = input("gimme da string\n")
        ser.write(s.encode())


