from time import sleep
import RPi.GPIO as GPIO

#define GPIO pins
DIR = 22
STEP = 23
CW = 1
CCW = 0
SPR = 160


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.01 

#while True:
    #GPIO.output(STEP, GPIO.HIGH)
    #sleep(delay)
    #GPIO.output(STEP, GPIO.LOW)
    #sleep(delay)
while True:
    for i in range(100):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)


GPIO.cleanup()
