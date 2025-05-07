import RPi.GPIO as gpio
import time
from matplotlib import pyplot
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds=[21, 20, 16, 12, 7, 8, 25, 24]
comp=4
troyka=17
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)


def perevod(a, n=8):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]
def adc():
    j=128
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=64
    else:
        j+=64
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=32
    else:
        j+=32
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=16
    else:
        j+=16
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=8
    else:
        j+=8
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=4
    else:
        j+=4
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=2
    else:
        j+=2
    gpio.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    time.sleep(0.001)
    if gpio.input(comp)==0:
        j-=1
    else:
        j+=1
    if gpio.input(comp)==0:
        j-=1
    return j

try:
    Uolt=0
    results=[]
    time_start=time.time()
    count=0
    print("zaryad")
    while Uolt<256*0.9:
        Uolt=adc()
        results.append(Uolt)
        time.sleep(0)
        count+=1
        gpio.output(leds, perevod(Uolt))
    gpio.setup(troyka,gpio.OUT, initial=gpio.LOW)

    print("razryad")
    while Uolt>256*0.1:
        Uolt=adc()
        results.append(Uolt)
        time.sleep(0)
        count+=1
        gpio.output(leds, perevod(Uolt))
    time_experiment=time.time()-time_start
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации проведённых измерений {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/(time_experiment/count), 0.013))
    
    with open('data.txt', 'w') as f:
        for i in results:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01299')
    
    
    y=[i/256*3.3 for i in results]
    x=[i*time_experiment/count for i in range(len(results))]
    pyplot.plot(x, y)
    pyplot.xlabel('время, с')
    pyplot.ylabel('Напряжение, В')
    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
