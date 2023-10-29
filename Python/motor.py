from time import sleep
import RPi.GPIO as GPIO
import T_class
import asyncio

#define GPIO pins
DIR = 22
STEP = 23
CW = 1
CCW = 0
SPR = 160

class Motor(T_class.T_class):  
    def __init__(self):
        super().__init__()
        
        self.step_count = SPR
        self.delay = 0.01
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
        GPIO.output(DIR, CCW)
        
    async def run(self):
        while not T_class.T_class.end:
            GPIO.output(STEP, GPIO.HIGH)
            await asyncio.sleep(self.delay)
            #sleep(self.delay)
            GPIO.output(STEP, GPIO.LOW)
            await asyncio.sleep(self.delay)
            #sleep(self.delay)
                            
    def set_speed(self, s):
        self.delay = 10 / s


