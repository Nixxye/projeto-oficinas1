import time
import board
import neopixel
import asyncio

import T_class

PATH = "1985.txt"
TIME_ENDLED = 0.1

class Led(T_class.T_class):
    def __init__(self):
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        self.pixel_pin = board.D12 
        self.num_pixels = 13
        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        self.ORDER = neopixel.GRB
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER
        )
        self.pixels.fill((255, 255, 255))
        self.pixels.show()
        time.sleep(1)
        self.position = self.num_pixels - 1

    
    async def run(self):
        while not T_class.T_class.end:
            #await self.rainbow_cycle(0.001)
            await self.music(PATH)
            await asyncio.sleep(0.01)
    async def show(self):
        while 1:
            self.pixels.show()
            await asyncio.sleep(0.01)
    async def music(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                led = 3
                # Itera sobre cada linha do arquivo
                for line in lines:
                    # Remove os caracteres de quebra de linha
                    line = line.strip()

                    # Obtém grupos de 4 dígitos de cada linha
                    for i in range(0, len(line), 4):
                        numbers = line[i:i+4]

                        # Converte o grupo de dígitos para números inteiros
                        #numbers = [int(digit) for digit in group_of_digits]

                        # Faz algo com os 4 números
                        #for j in range(self.num_pixels)
                            #self.pixels[j] = ((255, 255, 255, 0))
                        print(numbers)
                        if numbers[0] == '1':
                            self.pixels[led] = (255, 0, 0)
                        elif numbers[1] == '1':
                            self.pixels[led] = (0, 255, 0)
                        elif numbers[2] == '1':
                            self.pixels[led] = (0, 255, 0)
                        elif numbers[3] == '1':
                            self.pixels[led] = (255, 0, 255)
                        else:
                            self.pixels[led] = (255, 255, 255)

                        #self.pixels.show()

                        led = led + 1
                        if led >= self.num_pixels:
                            led = 0

                        # Aguarda um pouco antes de processar o próximo grupo
                        await asyncio.sleep(1)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo {filename}: {e}")
    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    async def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            await asyncio.sleep(wait)
    
    async def changeLed(self, vet):

        if vet[0] == '1':
            self.pixels[self.position] = (255, 0, 0)
        elif vet[1] == '1':
            self.pixels[self.position] = (0, 255, 0)
        elif vet[2] == '1':
            self.pixels[self.position] = (0, 255, 0)
        elif vet[3] == '1':
            self.pixels[self.position] = (255, 0, 255)
        else:
            self.pixels[self.position] = (255, 255, 255)

        self.position = self.position - 1
        if self.position < 0:
            self.position = self.num_pixels - 1      
