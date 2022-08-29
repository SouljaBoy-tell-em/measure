import RPi.GPIO as GPIO
import time

dac    = [26, 19, 13,  6, 5, 11,  9, 10]
leds   = [21, 20, 16, 12, 7,  8, 25, 24]
comp   = 4
troyka = 17

MAX_VOLTAGE = 3.3
BITS        = 8
LEVELS      = 2 ** BITS

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

# def d2v(digit):
#     active_leds = []
#     n_active_leds = int(digit / LEVELS * BITS) 

#     for i in range(n_active_leds):
#         active_leds.append(1)

#     for i in range(BITS - n_active_leds):
#         active_leds.append(0)

#     return active_leds

        
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def transform(digit):
    return (1 << round(digit * BITS / LEVELS)) - 1

def adc_sar():
    value = 0

    for i in range(7, -1, -1):
        step   = 2 ** i
        value += step

        GPIO.output(dac, dec2bin(value))
        time.sleep(0.005)
        
        if GPIO.input(comp) == GPIO.LOW:
            value -= step

    return value

def adc():
    for i in range(LEVELS):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.005)
        
        if GPIO.input(comp) == GPIO.LOW:
            return i

    return LEVELS - 1


try:
    while True:
        value = adc_sar()
        GPIO.output(leds, dec2bin(transform(value)))
       
        print("Voult: {:.2f}V, num: ".format(value * MAX_VOLTAGE / LEVELS), value)
    

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
