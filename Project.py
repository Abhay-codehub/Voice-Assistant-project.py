import ctypes
import datetime
import shutil
from threading import Thread
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
from pynput.keyboard import Key, Controller
from time import sleep
import random
import pywhatkit
from flask import Flask, request
from tkinter import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from plyer import notification
from pygame import mixer
import speedtest

keyboard = Controller()  # It is used to Initialize the engine present in OS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 180)


def speak(audio):  # Defining the Speak Function
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True
        audio = r.listen(source, 0, 4)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said  {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please")
            return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome",
           "vscode": "code", "powerpoint": "powerpnt", "notepad": "notepad.exe", "calculator": "calc.exe"}


def openappweb(query):  # It is used to open the Web Application
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):  # It is used to close the web application
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


def volumeup(): #It is used to increase the volume up function
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown(): # It is used to decrease the volume down function
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def start_server(port=8000, print_msg=True): #It is used to start the server
    if print_msg:
        print("Server started at local_ip_of_this_pc:%s" % port)
        print("Print Ctrl+C to exit")
    app = Flask("app")
    app.run(host="0.0.0.0", port=port)


if __name__ == '__main__':
    while True:
        # if 1:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Sir,You can call me anytime")
                    break
                elif 'how are you' in query:
                    speak(" I Am Fine,Thank you")
                    speak("How are You,Sir")

                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("Jarvis", "")
                    query = query.replace("Please", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)

                    pyautogui.press("enter")

                elif "close" in query:
                    query = query.replace("open", "")
                    query = query.replace("Jarvis", "")
                    query = query.replace("Please", "")

                    pyautogui.typewrite(query)

                    pyautogui.hotkey('ctrl', 'w')



                elif 'fine' in query or 'good' in query:
                    speak("I am Happy to know that ")

                elif 'who made you' in query:
                    speak(" I have been created by Yash Tandon")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif "open" in query:
                    openappweb(query)

                elif "close" in query:
                    closeappweb(query)

                elif 'who are your friends' in query:
                    speak("My Friends are Alexa and Siri")

                elif 'what is your name' in query:
                    speak("my Name is Jarvis")

                elif 'exit' in query or 'stop' in query:
                    speak("Thanks for giving me your time,Sir")
                    speak("I am Signing off", exit())



                elif 'joke' in query:
                    speak(pyjokes.get_joke())

                elif 'lock window' in query:
                    speak('locking the device')
                    ctypes.windll.user32.LockWorkStation()


                elif 'thank you' in query:
                    speak("Always Available Sir,anytime")

                elif 'welcome' in query:
                    speak("I think i should say that")

                elif 'who am i' in query:
                    speak("If you can talk then definetly you are human")
                elif "google" in query:
                    from SearchNow import searchGoogle

                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube

                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia

                    searchWikipedia(query)


                elif 'why you came to the world' in query:
                    speak("Thanks to Yash. further It's a Secret")

                elif 'camera' in query or 'take a photo' in query:
                    ec.capture(0, "Jarvis Camera", "img.jpg")


                elif "restart" in query:
                    speak("Your Computer Will be Restarted Shortly,Sir")
                    subprocess.call(["shutdown", "/r"])

                elif 'shutdown system' in query or 'jarvis close the system' in query:
                    speak("Hold on a Second! Your System is on its way to shut down")
                    subprocess.call(["shutdown", "/h"])

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

                        elif now > time:
                            break


#Youtube Automation
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
                    a = (1, 2, 3, 4, 5)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=syFZfO_wfMQ")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=_fqpk3cXG-U")

                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=qPPdjjEAbMM")

                    elif b == 4:
                        webbrowser.open("https://www.youtube.com/watch?v=WAEUgfHUHBQ")

                    elif b == 5:
                        webbrowser.open("https://www.youtube.com/watch?v=SmaY7RfBgas")


                elif "news" in query:
                    from NewsRead import latestnews

                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import Wolframalpha
                    from Calculatenumbers import calc

                    query = query.replace("Calculate", "")
                    query = query.replace("jarvis", "")
                    calc(query)




                elif "the video on youtube" in query:
                    speak("Playing the video")
                    from Whatsapp import playonyoutube

                    playonyoutube()

                elif "start server" in query:
                    speak("Strting the server")
                    pywhatkit.start_server()

                elif "image to art" in query:
                    pywhatkit.image_to_ascii_art("sharukh.jpg", "sharukh.txt")
                    speak("Image Converted to ASCII ART")

                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("music.mp3")
                    mixer.music.play()
                    notification.notify(title="My schedule :-", message=content, timeout=15)

                elif "whatsapp" in query:
                    from Whatsapp import sendwhatmsg_instantly

                    sendwhatmsg_instantly()

                elif "send message in group" in query:
                    from Whatsapp import sendwhatmsg_to_group_instantly

                    sendwhatmsg_to_group_instantly()

                elif "how is chrome" in query:
                    speak("Very Good Platform to use")

                elif "internet speed" in query:
                    webbrowser.open("fast.com")
                    speak("You can see on the screen")

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
