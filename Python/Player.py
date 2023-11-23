import asyncio
from pydub import AudioSegment
from pydub.playback import play
import time

class Player:
    def __init__(self, music="girls.mp3"):
        self.audio = AudioSegment.from_file(music, format="mp3")

    async def run(self, loop):
        await loop.run_in_executor(None, play, self.audio)