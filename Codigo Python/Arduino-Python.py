import serial
import time

ser = serial.Serial('/dev/ttyUSB0')
a = input()
print(a)
if(a == "s"):
    ser.write(b's')
elif(a == "a"):
    ser.write(b'a')
elif(a == "d"):
    ser.write(b'd')
elif(a == "w"):
    ser.write(b'w')
    print(ser.readline())