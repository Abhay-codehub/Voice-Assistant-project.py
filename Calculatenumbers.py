import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


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


def calc(query):
    Term = str(query)
    Term = Term.replace("Jarvis", "")
    Term = Term.replace("Multiply", "")
    Term = Term.replace("Plus", "")
    Term = Term.replace("Minus", "")
    Term = Term.replace("Divide", "")
    Term = Term.replace("Remainder","")

    Final = str(Term)


    try:
     results = Wolframalpha(Final)
     print(f"{results}")
     speak(results)

    except:
     speak("The Value is not answerable")
