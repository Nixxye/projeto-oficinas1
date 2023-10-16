# import required modules
from pydub import AudioSegment
from pydub.playback import play

# for playing wav file
song = AudioSegment.from_wav("1985.wav")
print('playing sound using pydub')
play(song)

