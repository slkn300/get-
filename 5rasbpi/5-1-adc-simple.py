import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perevod(a, n=8):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

def adc():
    for i in range(256):
        dacvoltage=perevod(i)
        gpio.output(dac, dacvoltage)
        compv=gpio.input(comp)
        sleep(0.001)
        if compv==1:
            return i
try:
    while True:
        i=adc()
        if i!=0:
            if i==None:
                i=255
            else:
                print(i, '{:.2f}v'.format(3.3*i/256))
             
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()   
