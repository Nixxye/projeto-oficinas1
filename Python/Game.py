import atexit
import asyncio
from queue import Queue
import time

import Motor
import T_class
import Led
import Receiver

'''
import Player
import Lcd
'''
TIME_MOTOR = 2
FILE = "girls.mp3"

class Game:
    def __init__(self):
        self.motor = Motor.Motor()
        #self.player = Player.Player()
        #self.lcd = Lcd.Lcd()
        self.led = Led.Led()
        self.receiver = Receiver.Receiver()

        self.loop = asyncio.get_event_loop()
        self.threads = []
        self.pipe = self.receiver.getPipe()

        self.loop.run_until_complete(self.receiver.run())
        atexit.register(self.close)

    def calibrate(self):
        self.motor.calibrate(self.pipe)

    def close(self):
        T_class.T_class.close()
        '''
        for thread in self.threads:
            thread.cancel()
        '''
        self.loop.stop()
        self.loop.close()

        if hasattr(self, 'motor'):
            self.motor.__del__()
        '''
        if hasattr(self, 'led'):
            self.led.__del__()

        if hasattr(self, 'lcd'):
            self.lcd.__del__()

        if hasattr(self, 'receiver'):
            self.receiver.__del__()
        '''
    def run(self):
        '''
        try:
            with open(FILE, 'r') as file:
                self.threads.append(self.loop.create_task(self.controlLeds(file)))
        except FileNotFoundError:
            print(f"Arquivo {FILE} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo {FILE}: {e}")
        '''
        #self.threads.append(self.loop.create_task(self.motor.run()))
        #self.threads.append(self.loop.create_task(self.led.run()))
        #time.sleep(TIME_MOTOR)
        #self.threads.append(self.loop.create_task(self.led.rainbow_cycle(0.01)))
        self.loop.run_until_complete(self.led.rainbow_cycle(0.01))
        self.loop.run_until_complete(self.motor.run())

    async def controlLeds(self, file):
            lines = file.readlines()
            while 1:
                # Itera sobre cada linha do arquivo
                for line in lines:
                    # Remove os caracteres de quebra de linha
                    line = line.strip()

                    # Obtém grupos de 4 dígitos de cada linha
                    for i in range(0, len(line), 4):
                        numbers = line[i:i+4]
                        await asyncio.sleep(1)