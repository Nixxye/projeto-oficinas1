# import required modules
from pydub import AudioSegment
from pydub.playback import play

# for playing wav file
song = AudioSegment.from_wav("girls.mp3")
print('playing sound using pydub')
play(song)

