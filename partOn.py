import time
import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0,0,1,0,0,0,0,0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
for i in range(8):
    GPIO.output(dac[i], number[i])
time.sleep(12)
GPIO.output(dac, 0)
GPIO.cleanup()
