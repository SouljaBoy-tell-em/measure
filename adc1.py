import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troykaModule = 17
bits = len(dac)
levels = 2**bits
maxVoult = 3.3

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal
def adc(value):
    signal = num2dac(value)
    voult = value/levels*maxVoult
    compValue = GPIO.input(comp)
    return(compValue)

try:
    while True:
        for value in range(256):
            compValue = adc(value)
            signal = num2dac(value)
            voult = value/levels*maxVoult
            #GPIO.output(dac, value)
            time.sleep(0.0007)
            if compValue == 0:
                print("ADC value = {:^3} -> {}, input voultage = {:.2f}".format(value, signal, voult))
                break
    
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
