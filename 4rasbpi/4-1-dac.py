import RPi.GPIO as gpio
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def perevod(a, n):
    return [int(element) for element in bin(a)[2:].zfill(n)]
try:
    while (True):
        a=input('input 0-255')
        if a=='q':
            exit()
        try:
            if int(a)<0 or int(a)>255:
                print('input number 0-255') 
        except ValueError:
            try: 
                if float(a):
                    print('input number instead of float')  
            except ValueError:
                print('input int number instead of string')  
        
        else:
            gpio.output(dac, perevod(int(a), 8))
            print("{:.4f}".format(int(a)/256*3.3))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()