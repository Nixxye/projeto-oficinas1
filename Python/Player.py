'''from pydub import AudioSegment
from pydub.playback import play

PATH = "girls.mp3"

class Player:
    def __init__(self):
        self.sound = AudioSegment.from_file(PATH)

    def play(self):
        print("Music")
        play(self.sound)
   
        '''
'''
import pygame

PATH = "girls.mp3"

class Player:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(PATH)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()
'''
import simpleaudio as sa

PATH = "girls.wav"

class Player:
    def __init__(self):
        self.file_path = PATH
        self.wave_obj = sa.WaveObject.from_wave_file(self.file_path)

    def play(self):
        play_obj = self.wave_obj.play()
        play_obj.wait_done()