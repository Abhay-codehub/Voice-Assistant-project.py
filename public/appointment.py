import requests
import json
import pyttsx3
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def Wolframalpha(query):
    apikey = "L3JW2H-KVRAW3976V"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The Value is nOT ANSERWABLE")
#L3JW2H-KVRAW3976V#
def appoint(query):
    Term1 = str(query)
    Term1 = Term1.replace("Jarvis", "")
    Term1 = Term1.replace("Appointment", "")
    Term1 = Term1.replace("Make an", "")
    Term1 = Term1.replace("Doctor", "")

    Final = str(Term1)
    try:
     results = Wolframalpha(Final)
     print(f"{results}")
     speak(results)
    except:
        speak("The Value is not answerable")


