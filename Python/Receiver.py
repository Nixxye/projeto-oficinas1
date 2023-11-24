import serial,time
from queue import Queue
import asyncio

DELAY = 0.1

class Receiver:
    def __init__(self):
        self.pipe = Queue()

    def getPipe(self):
        return self.pipe
    
    async def run(self):
        #get data
        await asyncio.sleep(DELAY)