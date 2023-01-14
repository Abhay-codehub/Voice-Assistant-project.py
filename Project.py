import ctypes
import datetime
import shutil
import ecapture as ec
import winshell as winshell
import wolframalpha
import pyjokes as pyjokes
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import os
import smtplib
import subprocess
from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import pyautogui
from playsound import playsound
import keyboard
from pynput.keyboard import Key,Controller
from time import sleep
import random
import pywhatkit
keyboard = Controller()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def greetMe():
     hour = int(datetime.datetime.now().hour)
     if hour >= 0 and hour <= 12:
         speak("Good Morning,sir")
     elif hour > 12 and hour <= 18:
         speak("Good Afternoon ,sir")

     else:
         speak("Good Evening,sir")

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword", "excel":"excel","chrome":"chrome","vscode":"code", "powerpoint":"powerpnt","notepad":"notepad.exe","calculator":"calc.exe"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")




""""
def username():
 speak("What should I call you sir")
 uname = takeCommand()
 speak("Welcome Mister")
 speak(uname)
 columns = shutil.get_terminal_size().columns
 print("####################".center(columns))
 print("Welcome Mr.",uname.center(columns))
 speak("How can I hElp You, Sir")"""


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


def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)





if __name__ == '__main__':

    greetMe()
    speak(" Hello Sir I am jarvis. How can i Help you?")
   # username()
while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open" in query:
         openappweb(query)

        elif "close" in query:
            closeappweb(query)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak(" I Am Fine,Thank you")
            speak("How are You,Sir")

        elif 'fine' in query or'good' in query:
            speak("I am Happy to know that ")

        elif 'who made you' in query:
            speak(" I have been created by Yash Tandon")

        elif 'who are your friends' in query:
            speak("My Friends are Alexa and Siri")

        elif 'exit' in query or 'stop' in query:
            speak("Thanks for giving me your time,Sir")
            exit()
        elif 'what is your name' in query:
            speak("my Name is Jarvis")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'lock window' in query:
            speak('locking the device')
            ctypes.windll.user32.LockWorkStation()

        elif "change my name to" in query:
            speak("What would you like to call me,Sir")
            query = query.replace("change my name to","")
            assname = query
            speak("That is a good one,Sir!")

        elif 'change name' in query:
            speak("What would you like to call me,Sir")
            assname = takeCommand()
            speak("My Friends Call me that")

        elif 'thank you' in query:
            speak("Always Available Sir,anytime")

        elif 'welcome' in query:
            speak("I think i should say that")

        elif 'who am i' in query:
            speak("If you can talk then definetly you are human")

        elif 'why you came to the world' in query:
            speak("Thanks to Yash. further It's a Secret")

        elif 'camera' in query or'take a photo' in query:
            ec.capture(0,"Jarvis Camera","img.jpg")


        elif "restart" in query:
            speak("Your Computer Will be Restarted Shortly,Sir")
            subprocess.call(["shutdown", "/r"])

        elif 'shutdown system' in query or 'jarvis close the system' in query:
            speak("Hold on a Second! Your System is on its way to shut down")
            subprocess.call(["shutdown","/h"])

        elif 'my contacts' in query or 'tell me the contact details of my account' in query:
            speak("Opening Contacts in chrome, please wait it will be opened shortly")
            webbrowser.open("contacts.google.com")

        elif "temperature" in query:
            search = "temperature in varanasi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
            search = "temperature in varanasi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")

# Set An Alarm
        elif "alarm" in query:
            speak("Enter the Time!")
            time = input(":Enter the time")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Alarm Is Ringing")
                    playsound("music.mp3")
                    speak("Alarm Closed")

                elif now>time:
                    break


        elif "sleep" in query:
            speak("Going to sleep,sir")
            exit()

        elif "pause" in query:
            pyautogui.press("k")
            speak("Video Paused")

        elif "play" in query:
            pyautogui.press("k")
            speak("Video Playing")

        elif "mute" in query:
            pyautogui.press("m")
            speak("Video Muted")

        elif "unmute" in query:
            pyautogui.press("m")
            speak("Video Unmuted")

        elif "back" in query:
            pyautogui.press("J")
            speak("Video has been Rewinded by 10 seconds")

        elif "forward" in query:
            pyautogui.press("L")
            speak("Video has been forwarded by 10 seconds")

        elif "open the miniplayer" in query:
            pyautogui.press("I")
            speak("Video is Opening in the miniplayer")

        elif "close the miniplayer" in query:
            pyautogui.press("I")
            speak("Video is not in miniplayer mode")

        elif "Full Screen" in query:
            pyautogui.press("F")
            speak("Video is now in Full Screen")

        elif " Full Screen Exit" in query:
            pyautogui.press("F")
            speak("Video is not in Full Screen")

        elif "Activate Subtitles" in query:
            pyautogui.press("C")
            speak("Subtitles Activated")

        elif "Deactivate Subtitles" in query:
            pyautogui.press("C")
            speak("Subtitles Deactivated")

        elif "play the video from the start" in query:
            pyautogui.press("0")
            speak("Video is being played from the beginning")

        elif "theatre mode" in query:
            pyautogui.press("t")
            speak("Video is being played in the theatre mode")

        elif "volume up " in query:

            speak("Turning Volume up,Sir")
            volumeup()

        elif "volume down " in query:
            speak("Turning Volume down,Sir")
            volumedown()

        elif "tired" in query:
            speak("Playing your favourite Songs,sir")
            a = (1,2,3,4,5)
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=syFZfO_wfMQ")
            elif b==2:
                webbrowser.open("https://www.youtube.com/watch?v=_fqpk3cXG-U")

            elif b==3:
                webbrowser.open("https://www.youtube.com/watch?v=qPPdjjEAbMM")

            elif b==4:
                webbrowser.open("https://www.youtube.com/watch?v=WAEUgfHUHBQ")

            elif b==5:
                webbrowser.open("https://www.youtube.com/watch?v=SmaY7RfBgas")


        elif "news" in query:
           from NewsRead import latestnews
           latestnews()

        elif "calculate" in query:
            from Calculatenumbers import Wolframalpha
            from Calculatenumbers import calc
            query = query.replace("Calculate","")
            query = query.replace("jarvis","")
            calc(query)

        elif "whatsapp" in query:
            from Whatsapp import sendwhatmsg_instantly
            sendwhatmsg_instantly()

        elif "send message in group" in query:
            from Whatsapp import sendwhatmsg_to_group_instantly
            sendwhatmsg_to_group_instantly()


        elif "the video on youtube" in query:
            speak("Playing the video")
            from Whatsapp import playonyoutube
            playonyoutube()

        elif"start server" in query:
         speak("Strting the server")
         pywhatkit.start_server()








