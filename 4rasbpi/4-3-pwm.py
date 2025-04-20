import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
pwm=gpio.PWM(24, 1000)
pwm.start(0)

try:
    while True:
        try:
                DutyCycle=input()
                pwm.ChangeDutyCycle(int(DutyCycle))
                print("{:.2f}".format(int(DutyCycle)*3.3/100))
                
        except ValueError:
            print('введите число')
finally:
    pwm.stop()
    gpio.cleanup()   