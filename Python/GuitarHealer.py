import Game
import asyncio

class GuitarHealer:
    def __init__(self):
        self.game = Game.Game()
        asyncio.run(self.game.calibrate())
        #self.game.run()

if __name__ == "__main__":
    gH = GuitarHealer()