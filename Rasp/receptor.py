import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

pipe = [0xE8, 0xE8, 0xF0, 0xE1]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17) #Mudar pinos

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()

while True:
    while not radio.avaliable(0):
        time.sleep(1/100)
    
    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSioze())
    priunt("Received: {}".format(receivedMessage))

    