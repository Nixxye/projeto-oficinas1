#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Example: Scrolling text on display if the string length is major than columns in display.
# Created by Dídac García.

# Import necessary libraries for communication and display use
import drivers
from time import sleep
import asyncio
from multiprocessing import Value
# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
class Lcd:
	def __init__(self, go):
		self.display = drivers.Lcd()
		self.num_cols = 16
		self.go = go

	async def show(self, text1, text2):
		while self.go.value:
			self.display.lcd_display_string(text1, 1)

			if len(text2) > self.num_cols:
				self.display.lcd_display_string(text2[:self.num_cols], 2)
				await asyncio.sleep(1)
				for i in range(len(text2) - self.num_cols + 1):
					text_to_print = text2[i:i+self.num_cols]
					self.display.lcd_display_string(text_to_print, 2)
					if not self.go.value:
						self.display.lcd_clear()
						return
					await asyncio.sleep(0.2)
				await asyncio.sleep(1)
			else:
				self.display.lcd_display_string(text2, 2)

			self.display.lcd_clear()	
'''
display = drivers.Lcd()

# Main body of code
try:
	print("Press CTRL + C to stop this script!")

	def long_string(display, text='', num_line=1, num_cols=16):
		""" 
		Parameters: (driver, string to print, number of line to print, number of columns of your display)
		Return: This function send to display your scrolling string.
		"""
		if len(text) > num_cols:
			display.lcd_display_string(text[:num_cols], num_line)
			sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print, num_line)
				sleep(0.2)
			sleep(1)
		else:
			display.lcd_display_string(text, num_line)


	# Example of short string
	long_string(display, "Hello World!", 1)
	sleep(1)

	# Example of long string
	long_string(display, "Hello again. This is a long text.", 2)
	display.lcd_clear()
	sleep(1)

	while True:
		# An example of infinite scrolling text
		long_string(display, "Hello friend! This is a long text!", 2)
except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	display.lcd_clear()
'''