import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def takeCommand():
    #It takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening.....")
       r.pause_threshold = 0.5
       r.energy_threshold = 300
       r.dynamic_energy_threshold = True
       audio = r.listen(source, 0, 4)

       try:
         print("Recognizing....")
         query = r.recognize_google(audio,language = 'en-in')
         print(f"User said  {query}\n")
       except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendwhatmsg_instantly():
    speak("Who Do u want TO Message")
    a = int(input('''Yash Tandon - 1  
    Sambit - 2 '''))
    if a==1:
        speak("Whats the Message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg_instantly("+91-9580692521",message,wait_time= 15)


    elif a==2:
        speak("Whats the Message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg_instantly("+91-8763532489", message,wait_time= 15)

def sendwhatmsg_to_group_instantly():
    speak("Who Do U  want to message")
    a = int(input('''Projects-1 
    Enterprenuers - 2 '''))
    if a==1:
        speak("What is The Message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg_to_group_instantly("HwYCxSYMaDZDAj2PB4kcLs",message,wait_time=15)


    elif a==2:
        speak("What is the message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg_to_group_instantly("BkaKn69NwxmDkG0Fxmzor3",message,wait_time=15)

