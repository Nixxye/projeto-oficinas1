import atexit
import asyncio
from multiprocessing import Pipe, Value
import time

import Motor
import T_class
import Led
import Receiver
import Player
import Lcd

F_LEDS = 0.31
TIME_MOTOR = 2
TIME_PLAYER = 3
FILE = "girls.txt"
#colocar arquivo de música aqui também

class Game:
    def __init__(self):
        self.player = Player.Player()
        self.led = Led.Led()

        self.loop = asyncio.get_event_loop()
        self.threads = []
        self.pipe_receiver, self.pipe_sender = Pipe(duplex=False)
        
        self.go = Value('b', False)
        self.lcd = Lcd.Lcd(self.go)
        self.receiver = Receiver.Receiver(self.pipe_sender, self.go)
        self.motor = Motor.Motor(self.pipe_receiver, self.go)

        atexit.register(self.close)

    def clear_pipe(self):
        while self.pipe_receiver.poll():
            _ = self.pipe_receiver.recv()

    async def calibrate(self):
        self.go.value = True
        await asyncio.gather(
            self.receiver.run(),
            self.motor.calibrate(),
            self.lcd.show("Calibrando", "Indicador: Girar    Médio: OK")
            )
        
        self.clear_pipe()

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
    async def run(self):
        try:
            with open(FILE, 'r') as file:
                #await self.loop.run_in_executor(None, self.player.play)
                self.go.value = True
                task = asyncio.create_task(self.led.show())
                await asyncio.sleep(1)
                self.player.play()
                #await asyncio.sleep(TIME_PLAYER)
                await asyncio.gather(
                    self.controlLeds(file),
                    self.led.show(),
                    self.motor.run(),
                    task,
                    self.lcd.show("Guitar Healer", "Something in The Way - Nirvana - ")
                )
                #await asyncio.sleep(TIME_MOTOR)
                #self.motor.run()
#                self.threads.append(self.loop.create_task(self.controlLeds(file)))
        except FileNotFoundError:
            print(f"Arquivo {FILE} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo {FILE}: {e}")
        #self.threads.append(self.loop.create_task(self.led.run()))

        #self.threads.append(self.loop.create_task(self.motor.run()))

        #self.threads.append(self.loop.create_task(self.led.rainbow_cycle(0.01)))
        #self.loop.run_until_complete(self.led.rainbow_cycle(0.01))
        #self.loop.run_until_complete(self.motor.run())

    async def controlLeds(self, file):
        lines = file.readlines()
        while 1:
            # Itera sobre cada linha do arquivo
            j = 0
            for line in lines:
                # Remove os caracteres de quebra de linha
                line = line.strip()

                # Obtém grupos de 4 dígitos de cada linha
                for i in range(0, len(line), 4):
                    numbers = line[i:i+4]
                    #self.led.timingTest()
                    #await asyncio.sleep(F_LEDS)
                    await self.led.changeLed(numbers)
                    if j > 4:
                        await asyncio.sleep(F_LEDS)
                    j = j + 1