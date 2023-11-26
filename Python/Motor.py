import pigpio
import T_class
import asyncio
from multiprocessing import Value

#define GPIO pins
DIR = 21
STEP = 20

VEL = 200
TIME_MOTOR = 0.5
class Motor(T_class.T_class):  
	def __init__(self, pipe, go):
		super().__init__()
		self.pi = pigpio.pi()
		self.delay = 0.01
		self.pipe_receiver = pipe
		self.go = go
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
		await asyncio.sleep(TIME_MOTOR)
		self.pi.write(DIR, 1)
		self.pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
		self.pi.set_PWM_frequency(STEP, VEL)  # 500 pulses per second	
	
	async def calibrate(self):
		self.pi.set_PWM_frequency(STEP, 100)
		self.pi.set_PWM_dutycycle(STEP, 0)
		#print("no loop")
		while self.go.value:
			#print("motr")
			if self.pipe_receiver.poll():
				input = self.pipe_receiver.recv()
#				print(input)
				if input[3] == 1:
					self.pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
					self.pi.write(DIR, 1)
					#print("Esquerda")
				elif input[0] == 1:
					self.pi.set_PWM_dutycycle(STEP, 0)
					self.go.value = False
					print("Parando")
				else:
					self.pi.set_PWM_dutycycle(STEP, 0)
			await asyncio.sleep(0.1)
		print("Saindo motor")