import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

# def perevod(a, n=8):
#     return [int (elem) for elem in bin(a)[2:].zfill(n)]

def adc():
    # j=0
    # for i in range(7, -1, -1):
    #     j+=2**i
    #     gpio.output(dac, perevod(j))
    #     sleep(0.01)
    #     if gpio.input(comp)==1:
    #         j-=2**i
    j=128
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=128
    j+=64
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=64
    j+=32
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=32
    j+=16
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=16
    j+=8
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=8
    j+=4
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=4
    j+=2
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=2
    j+=1
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if gpio.input(14)==1:
        j-=1

    return j
try:
    while True:
        i=adc()
        if i==None:
            i=255
        else:
            print(i, '{:.2f}v'.format(3.3*i/256))
             
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()    