from time import sleep
import pigpio
import T_class
import asyncio
from queue import Queue

#define GPIO pins
DIR = 21
STEP = 20


class Motor(T_class.T_class):  
	def __init__(self, pipe):
		super().__init__()
		self.pi = pigpio.pi()
		self.delay = 0.01
		self.pipe_receiver = pipe
		self.pi.set_mode(DIR, pigpio.OUTPUT)
		self.pi.set_mode(STEP, pigpio.OUTPUT)
		self.MODE = (14, 15, 18)
		self.RESOLUTION = {'Full': (0, 0, 0),
							 'Half': (1, 0, 0),
							 '1/4': (0, 1, 0),
							 '1/8': (1, 1, 0),
							 '1/16': (0, 0, 1),
							 '1/32': (1, 0, 1)}
							 
		for i in range(3):
			self.pi.write(self.MODE[i], self.RESOLUTION['Full'][i])

		# Set duty cycle and frequency
		self.pi.set_PWM_dutycycle(STEP, 0)  # PWM 1/2 On 1/2 Off
		self.pi.set_PWM_frequency(STEP, 150)  # 500 pulses per second	
		
	def __del__(self):
		self.pi.set_PWM_dutycycle(STEP, 0)
		self.pi.stop()	
		
	async def run(self):
		try:
			while not T_class.T_class.end:
				self.pi.write(DIR, 0)
				await asyncio.sleep(self.delay)
		except KeyboardInterrupt:
			self.close()
	
	async def calibrate(self):
		self.pi.set_PWM_frequency(STEP, 100)
		self.pi.set_PWM_dutycycle(STEP, 0)

		go = True
		print("no loop")
		while go:
			print("motr")
			if self.pipe_receiver.poll():
				input = self.pipe_receiver.recv()
				print(input)
				if input[3] == 1:
					self.pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
					self.pi.write(DIR, 1)
					print("Esquerda")
				elif input[0] == 1:
					self.pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
					self.pi.write(DIR, 0)
					print("Direita")
					'''
				elif input[2] == 1:
					self.pi.set_PWM_dutycycle(STEP, 0)
					go = False
					'''
				else:
					self.pi.set_PWM_dutycycle(STEP, 0)
			await asyncio.sleep(0.1)