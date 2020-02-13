import serial
import io
import panadas as pd
import numpy as np
import matplotlib.pyplot as plt



def convertDate(date):
    pass

def connectedGPS(line):
    pass

if __name__ == "main":
    
    ser = serial.Serial('/dev/ttyUSB0', 15200)
    while 1: 
        if(ser.in_waiting >0):
            line = ser.readline()
            print(line)
