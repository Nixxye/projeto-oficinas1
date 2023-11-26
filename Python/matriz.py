#!/usr/bin/env python
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT


class Matrix:
    def __init__(self):
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=4, block_orientation=90, blocks_arranged_in_reverse_order=True)
        self.device.contrast(16)

        self.toggle = False

        self.number = 0

    def hit(self):
        self.number = self.number + 1
        self.change()

    def miss(self):
        self.number = self.number - 1
        self.change()

    def change(self):
        with canvas(self.device) as draw:
            text(draw, (17, 1), str(self.number), fill="white", font=proportional(CP437_FONT))        