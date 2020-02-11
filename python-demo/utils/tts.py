import pyglet
from gtts import gTTS
import os


def google(text):
    tts = gTTS(text=text, lang='ko')
    tts.save('temp.wav')
    os.system("open temp.wav")