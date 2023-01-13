import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def latestnews():
    apidict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=30a7b6563e7841e391efe8283b96c5c4",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=30a7b6563e7841e391efe8283b96c5c4",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=30a7b6563e7841e391efe8283b96c5c4",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=30a7b6563e7841e391efe8283b96c5c4",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=30a7b6563e7841e391efe8283b96c5c4",
                "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=30a7b6563e7841e391efe8283b96c5c4"}

    content =None
    url = None
    speak("Which Field News Do u Want, [business] [health] [technology] [sports] [entertainment] [science]")
    field = input("Type field news that u wish to hear")
    for key,value in apidict.items():
        if key.lower()in field.lower():
            url = value
            print(url)
            print("url was found")
            break

        else:
            url = True
    if url is True:
        print("URL NOT FOUND")


    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")
    arts = news["articles"]
    for articles in arts:
        article = articles['title']
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit:{news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
         break

    speak("Thats all")





