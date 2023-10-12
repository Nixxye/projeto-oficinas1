from time import sleep
import RPi.GPIO as GPIO

#define GPIO pins
DIR = 22
STEP = 23
CW = 1
CCW = 0
SPR = 160

class Motor:
    step_count = SPR
    delay = 0.01
    
    def __init __ (self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
        GPIO.output(DIR, CW)
        
    def exec (self):
        while (1):
            for i in range(100):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                
if __name__ == '__main__':
    motor = Motor()
    motor.run()
