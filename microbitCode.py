#https://www.hackster.io/samelhusseini/micro-bit-spotify-mac-5ac6d7

#print() sends info over serial
#https://support.microbit.org/support/solutions/articles/19000022103-outputing-serial-data-from-the-micro-bit-to-a-computer


from microbit import *


while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    print("m"+str(x)+","+str(y))
    sleep(10)
    
    if button_a.is_pressed():
        print("c1")
        sleep(10)#dont know if dekay is needed, keeping just in case
    elif button_b.is_pressed():
        print("c2")
        sleep(10)
    
    sleep(1000)