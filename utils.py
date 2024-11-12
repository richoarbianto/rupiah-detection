import os
from playsound import playsound
from datetime import datetime
from gtts import gTTS

def text_to_speech(text):
    tts = gTTS(text, lang = 'id')
    pathfile = "sounds/" + str(datetime.now().timestamp()) + ".mp3"
    tts.save(pathfile)
    playsound(pathfile)
    os.remove(pathfile)