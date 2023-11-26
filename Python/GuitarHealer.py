import Game
import asyncio

class GuitarHealer:
    def __init__(self):
        self.game = Game.Game()
        '''
        print("Calibrando")
        asyncio.run(self.game.calibrate())
        print("Jooj")
        asyncio.run(self.game.run())
        '''
        asyncio.run(self.run())

    async def run(self):
        print("Calibrando")
        await self.game.calibrate()
        print("Jooj")
        await self.game.run()

if __name__ == "__main__":
    gH = GuitarHealer()