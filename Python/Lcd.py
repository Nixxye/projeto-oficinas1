import drivers
import T_class
import asyncio

class Lcd(T_class.T_class):
	def __init__(self):
		super().__init__()
		self.display = drivers.Lcd()
		self.num_line = 1
		self.text = "Guitar Healer -> 1985 - Bowling for soup"
		self.num_cols = 2

async def run(self):
	while not T_class.T_class.end:
		if len(self.text) > self.num_cols:
			self.display.lcd_display_string(self.text[:num_cols], self.num_line)
			await asyncio.sleep(1)
			for i in range(len(self.text) - num_cols + 1):
				text_to_print = self.text[i:i+num_cols]
				self.display.lcd_display_string(text_to_print, self.num_line)
				await asyncio.sleep(0.2)
			await asyncio.sleep(1)
		else:
			self.display.lcd_display_string(self.text, self.num_line)
