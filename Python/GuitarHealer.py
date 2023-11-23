import atexit
import asyncio
from queue import Queue

import Motor
import T_class
import Player
#import Lcd
#import Led

class GuitarHealer:
    def __init__(self, loop):
        #self.motor = Motor.Motor()
        self.player = Player.Player()
        #self.lcd = Lcd.Lcd()
        #self.led = Led.Led()
        self.loop = loop
        self.threads = []
        self.queue = Queue()
        #self.threads.append(loop.create_task(self.motor.run()))
        #self.threads.append(loop.create_task(self.lcd.run()))
        #self.threads.append(loop.create_task(self.led.run()))
        #self.threads.append(loop.create_task(self.led.show()))
        atexit.register(self.close)
        #INICIAR A COMUNICAÇÃO
        loop.run_until_complete(self.start())

    def close(self):
        T_class.T_class.close()
        for thread in self.threads:
            thread.cancel()
        self.loop.stop()
        self.loop.close()
        if hasattr(self, 'motor'):
            self.motor.__del__()
    async def start(self):
        await self.player.run(self.loop)
    def __del__(self):
        self.close()

    def calibrate(self):
        self.threds.append(self.loop.create_task(self.motor.calibrate(queue)))


loop = asyncio.get_event_loop()
game = GuitarHealer(loop)
loop.run_forever()
