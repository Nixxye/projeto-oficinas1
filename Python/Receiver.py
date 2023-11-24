import serial,time
from queue import Queue
import asyncio

DELAY = 0.1

class Receiver:
    def __init__(self):
        self.pipe = Queue()
        self.ser = serial.Serial('/dev/rfcomm0', 9600, timeout=0.1)
        self.ser.flushInput()
        self.ser.flushOutput()

    def getPipe(self):
        return self.pipe
    
    def __del__(self):
        self.ser.flushInput()
        self.ser.flushOutput() 

    async def run(self):
        while True:
            try:
                bytesToRead = self.ser.inWaiting()
                
                if bytesToRead > 0:
                    data = self.ser.read(bytesToRead)
                
                    print(data.decode("utf-8").strip())
            except KeyboardInterrupt:
                break

            await asyncio.sleep(DELAY)