from playsound import playsound
from gtts import gTTS
import  speech_recognition as sr
import  os


def speak(string):
    tts = gTTS(text=string , lang="tr" , slow = False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("...                        Sayın Ahmet ESMER hayranları iyi geceleriniz olsun")