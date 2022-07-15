from urllib.parse import quote_from_bytes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from datetime import date
import smtplib
import requests
import googletrans
from googletrans import Translator
import pywikihow
from pywikihow import search_wikihow, WikiHow

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    #datetime code
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening!")
    #weather code
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=311f0cb181a61b9c71cbbfa6b73cc53e&q=Unnao'
    json_data = requests.get(api_address).json()
    formatted_data = json_data['weather'][0]['description']
    print(formatted_data)
    speak(f"I am Friday. Todays weather is{formatted_data}.")
    speak("What can i do for you")
def takeCommand():
    #it take microphone input from user and give string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)
        check=1
    except Exception as e:
        check=0
        print("Say that again please...")
        return "None"
    return query

def takeCommandhindi():
    #it take microphone input from user and give string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='hi')
        print("User said: ",query)
        check=1
    except Exception as e:
        check=0
        print("Say that again please...")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fridayassist9@gmail.com','C:\\Users\\ASUS\\Desktop\\passkey.txt')
    server.sendemail('fridayassist9@gmail.com',to,content)
    server.close()

def search_wikihow(query, max_results=10, lang='e'):
    return list(WikiHow.search(query, max_results,lang))

if __name__ == "__main__":
    wishMe()
    stop = 0
    while (stop==0):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open my class' in query:
            webbrowser.open("https://myclass.lpu.in/")
        
        elif 'open college portal' in query:
            webbrowser.open("https://ums.lpu.in/")
        
        elif 'play music' in query:
            music_dir ='D:\\My Music'
            songs = os.listdir(music_dir)
            print(songs)
            randomNo = random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir, songs[randomNo]))
        
        elif 'what is time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'what is date today' in query:
            strDate= date.today().strftime("%B %d, %Y")
            print(f"sir, the date is {strDate}")
            speak(f"sir, the date is {strDate}")
        
        elif 'open camera' in query:
            campath = ""

        elif 'open code' in query:
            codepath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("I am opening Visual Code for you, Sir")
            os.startfile(codepath)
        
        elif 'i want to make presentation' in query:
            pptpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            speak("I am opening powerpoint for you, Sir")
            os.startfile(pptpath)

        elif 'send email to aryan' in query:
            #speak("to whom, sir")
            #check=0
            #while(check==0):
             #   getemail=takeCommand().lower()
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'aryantiwari522@gmail.com'
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Sir. I am not able to send this email")
        
        elif 'translate this for me in english' in query:
            speak("tell me the sentence")
            sentence = takeCommandhindi()
            print(sentence)
            translater= Translator()
            res = translater.translate(sentence)
            text=res.text
            print(text)
            speak(text)

        elif 'translate this for me in hindi' in query:
            speak("tell me the sentence")
            sentence = takeCommand()
            print(sentence)
            translater= Translator()
            res = translater.translate(sentence, dest='hi')
            text=res.text
            print(text)
            speak(text)

        elif 'activate learning mod' in query:
            speak("Learning mode activated. Ask me anything")
            while True:
                how= takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("How to do mode is closed")
                        break
                    else:
                        max_results= 1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir. i am not able to find this")

        elif 'thank you friday you can rest now' in query:
            speak("Take care of you, Sir")
            stop=1