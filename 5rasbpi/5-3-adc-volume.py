import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
leds=[2, 3, 4, 17, 27, 22, 10, 9]
comp=14
troyka=13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
gpio.setup(leds, gpio.OUT)

def adc():
    j=128
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=64
    else:
        j+=64
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=32
    else:
        j+=32
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=16
    else:
        j+=16
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=8
    else:
        j+=8
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=4
    else:
        j+=4
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=2
    else:
        j+=2
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=1
    else:
        j+=1
    if gpio.input(14)==1:
        j-=1

    return j

def volume(n):
    n=int(n/256*10)
    spisok=[0]*8
    for i in range(n-1):
        spisok[i]=1
    return spisok

try:
    while True:
        i=adc()
        if i!=0:
            gpio.output(leds, volume(i))
            print(int(i/256*10))
             
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()   