import RPi.GPIO as gpio
from time import sleep
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def perevod(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    while (True):
        a=input()
        if a=='q':
            exit()
        elif not a.isdigit():
            print('введите число')
        t=int(a)/256/2
        for i in range(256):
            gpio.output(dac, perevod(i, 8))
            sleep(t)
        for i in range(254, 0, -1):
            gpio.output(dac, perevod(i, 8))
            sleep(t)
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()