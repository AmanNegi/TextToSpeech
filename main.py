from gtts import gTTS
from playsound import playsound
import os

# Simply take input
text = input();

# Using Google Text To Speech to save the mp3 file
tts = gTTS(text, lang='en')
tts.save("hello.mp3")

# Using playsound library to play the mp3 file
playsound('./hello.mp3')

# Simply delete the mp3 file after it has been played
os.remove("./hello.mp3")
