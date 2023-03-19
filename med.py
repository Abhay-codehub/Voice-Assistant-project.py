import http.client
import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def aim():


conn = http.client.HTTPSConnection("medicine-autocomplete-indian-brands.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "8581967a2bmshf446cabef9a8bbbp1fd815jsnbc0602408f3f",
    'X-RapidAPI-Host': "medicine-autocomplete-indian-brands.p.rapidapi.com"
}

conn.request("GET", "/api/medicine/search?searchterm=para", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
speak(data.decode("utf-8"))

