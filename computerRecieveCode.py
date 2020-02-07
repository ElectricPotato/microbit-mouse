#https://nitratine.net/blog/post/simulate-mouse-events-in-python/

from pynput.mouse import Button, Controller
mouse = Controller()

import serial
ser = serial.Serial('/dev/ttyUSB0',115200)  # open serial port
print(ser.name)         # check which port was really used

#TODO: find port automatically https://pyserial.readthedocs.io/en/latest/tools.html

while True:
    line = ser.readline()
    if(line[0]=='m'): #e.g. "m10,10" command for moving mouse 10 pixels in both directions
        x,y=line[1:].split(',')
        mouse.move(int(x), int(y))
    if(line[0]=='c'): #c1 or c2 for L/R click
        if(line[1]=='1'):
            mouse.click(Button.right, 1)
        else:
            mouse.click(Button.left, 1)

ser.close()
