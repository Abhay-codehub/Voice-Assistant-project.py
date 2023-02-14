import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning,sir")
    elif 12 < hour <= 18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")


        speak("Please Tell Me How Can I help u")
