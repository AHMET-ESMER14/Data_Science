import webbrowser

from playsound import playsound
from gtts import gTTS
import  speech_recognition as sr
import  os
import webbrowser


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio , language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan : Sistem çalışmıyor")
        return voice



def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba")
    if "ahmet" in voice:
        speak("sa")
    if "ara":
        speak("what")
        search = record()
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("opening")

def speak(string):
    tts = gTTS(text=string , lang="tr" , slow = False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    #os.remove(file)


speak("Open")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)

