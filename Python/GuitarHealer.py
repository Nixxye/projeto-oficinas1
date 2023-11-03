import Motor
import T_class
import asyncio
import Lcd
class GuitarHealer:
    def __init__(self, loop):
        self.motor = Motor.Motor()
        self.lcd = Lcd.Lcd()
        
        self.loop = loop
        self.threads = []
        self.threads.append(loop.create_task(self.motor.run()))
        self.threads.append(loop.create_task(self.lcd.run()))

    def close(self):
        T_class.close()
        for thread in self.threads:
            thread.cancel()
        self.loop.stop()
        self.loop.close()

loop = asyncio.get_event_loop()
game = GuitarHealer(loop)
loop.run_forever()
T_class.close()
loop.close()

