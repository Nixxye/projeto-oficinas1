import atexit
import asyncio
from multiprocessing import Pipe, Value

import Motor
import T_class
import Led
import Receiver
import Player
import Lcd
import Matrix

F_LEDS = 0.2
TIME_MOTOR = 2
TIME_PLAYER = 3
FILE = "girls.txt"
#colocar arquivo de música aqui também

class Game:
    def __init__(self):
        self.player = Player.Player()

        self.loop = asyncio.get_event_loop()
        self.threads = []
        self.pipe_receiver, self.pipe_sender = Pipe(duplex=False)
        
        self.index = Value('i', 0)
        self.led = Led.Led(self.index)

        self.go = Value('b', False)
        self.lcd = Lcd.Lcd(self.go)
        self.receiver = Receiver.Receiver(self.pipe_sender, self.go)
        self.motor = Motor.Motor(self.pipe_receiver, self.go)
        self.matrix = Matrix.Matrix()

        self.lines = []
        try:
            with open(FILE, 'r') as file:
                self.lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Arquivo {FILE} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo {FILE}: {e}")

        atexit.register(self.close)

    def clear_pipe(self):
        while self.pipe_receiver.poll():
            _ = self.pipe_receiver.recv()

    async def calibrate(self):
        self.go.value = True
        await asyncio.gather(
            self.receiver.run(),
            self.motor.calibrate(),
            self.lcd.show("Calibrando", "Indicador: Girar    Medio: OK")
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
        self.go.value = True
        task = asyncio.create_task(self.led.show())
        await asyncio.sleep(2)
        self.player.play()
        #await asyncio.sleep(TIME_PLAYER)
        await asyncio.gather(
            self.controlLeds(),
            self.led.show(),
            self.motor.run(),
            task,
            self.lcd.show("Guitar Healer", "Something in The Way - Nirvana - "),
            self.receiver.run(),
            self.combo()
        )


    async def controlLeds(self):
        while 1:
            # Itera sobre cada linha do arquivo
            j = 0
            for line in self.lines:
                # Remove os caracteres de quebra de linha
                line = line.strip()

                # Obtém grupos de 4 dígitos de cada linha
                for i in range(0, len(line), 4):
                    numbers = line[i:i+4]
                    '''
                    self.led.timingTest()
                    await asyncio.sleep(F_LEDS)
                    '''
                    await self.led.changeLed(numbers)
                    if j > 4:
                        await asyncio.sleep(F_LEDS)
                    j = j + 1
        
    async def combo(self):
        self.clear_pipe()
        while self.go.value:
            if self.pipe_receiver.poll():
                input = self.pipe_receiver.recv()
                n = self.index.value
                if (
                    input[0] != int(self.lines[n][0]) or 
                    input[1] != int(self.lines[n][1]) or 
                    input[2] != int(self.lines[n][2]) or 
                    input[3] != int(self.lines[n][3])
                    ):
                    self.matrix.miss()
                else:
                    self.matrix.hit()
                print(input)
                print(self.lines[n])
                print()   
            await asyncio.sleep(0.05)