import serial,time

resposta=[0,0,0,0]

with serial.Serial("/dev/ttyACM0", 9600, timeout=0.1) as arduino:
	time.sleep(0.02)
	if arduino.isOpen():
		try:
			while True:
				answer=arduino.readline()
				#if answer>7:
					#resposta[3]=1
				#if answer-8>3:
					#resposta[2]=1
				#if answer-12>1:
					#resposta[1]=1
				#if answer-14>0:
					#resposta[0]=1
				print(answer)
				arduino.flushInput() #remove data after reading
		except KeyboardInterrupt:
			print("KeyboardInterrupt has been caught.")
