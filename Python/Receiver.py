import serial
import asyncio
from multiprocessing import Value
#sudo rfcomm bind 0 98:D3:51:FD:8B:69 1
DELAY = 0.1

class Receiver:
    def __init__(self, pipe, go):
        self.pipe_sender = pipe
        self.go = go

        self.ser = serial.Serial('/dev/rfcomm0', 9600, timeout=0.1)
        self.ser.flushInput()
        self.ser.flushOutput()

    def __del__(self):
        self.ser.flushInput()
        self.ser.flushOutput() 

    async def run(self):
        #print("No Rcv")
        while self.go.value:
            #print("rcv")
            vet = [0,0,0,0]
            try:
                n_bytes = self.ser.inWaiting()
                if n_bytes > 0:
                    val = self.ser.read(n_bytes)
                    b_array = bytearray(val)
                    data = int(chr(b_array[0]))
                    #print(val)
                    #print(data)
                    if data >= 8:
                        vet[3] = 1
                        data = data - 8
                    if data >= 4:
                        vet[2] = 1
                        data = data - 4
                    if data >= 2:
                        vet[1] = 1
                        data = data - 2
                    if data >= 1:
                        vet[0] = 1
                    #print(vet)
                    self.pipe_sender.send(vet)
                    #print(vet)
                    #print(data.decode("utf-8").strip())
            except Exception as e:
                print(f"Error: {e}")

            await asyncio.sleep(DELAY)
        print("Saindo receiver")