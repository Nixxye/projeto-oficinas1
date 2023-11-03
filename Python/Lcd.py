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
  while no T_class.T_class.end:
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
