# Blue-To be reviewed in physical electronics....
# Red-Key Features

# This is F.R.E.D, an AI assistant inspired by J.A.R.V.I..S and made by Krishank Shah....
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pywhatkit
import pyjokes

print('Loading your AI personal assistant - FRED')

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning Sir")
        print("Hello,Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon Sir")
        print("Hello,Good Afternoon Sir")
    else:
        speak("Hello,Good Evening Sir")
        print("Hello,Good Evening Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your A I personal assistant FRED, At your service Sir")
wishMe()

if __name__ == '__main__':

    while True:
        speak("How can I help you sir ?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('I will shut down until you further wish to hear me.')
            print('I will shut down until you further wish to hear me.')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "ab41fb79ca0c82f16440ed4b66b0db3a"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                #                c=float(input("temp"))
                #                k=c+273.15
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n degree celcius is " +
                      #                      str(c) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n Degree Celcius is " +
                      #                      str(c) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak(
                'I am FRED version 2 point 3 your personal assistant. '
                'I am programmed to be with you whenever you need help')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Krishank Shah")
            print("I was built by Krishank Shah")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'question' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "8VW3GK-6TKHG3KJJW"
            client = wolframalpha.Client('8VW3GK-6TKHG3KJJW')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "play" in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            print("playing " + song)

        elif "are you single" in statement:
            speak("I am in a secret relationship sir, i am sorry i cannot answer this as of now.")
            print("I am in a secret relationship sir, i am sorry i cannot answer this as of now.")

        elif "code" in statement:
            speak(" That command requires password, tell me the password ")
            print("That command requires password, tell me the password")
            password = takeCommand().lower()
            if "red" in password:
                speak("This code is a combination of all the AI assistants in the world and the source code "
                      "is currently longer than 200 lines written by Krishank Sir. "
                      "There are a few vulnerabilities in this program that cannot be disclosed.")
                print("This code is a combination of all the AI assistants in the world and the source code"
                      " is currently longer than 200 lines written by Krishank Sir. "
                      "There are a few vulnerabilities in this program that cannot be disclosed.")
            else:
                speak("password does not match")
                print("password does not match")

        elif "calculate " in statement:
            speak("starting calculator assistant")
            os.system('python calculator.py')

        elif "joke" in statement:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif "fred" in statement:
            speak("at your service sir")
            print("at your service sir")
        elif "help" in statement or "save our soul" in statement:
            speak("Are you sure you want to call for help ?")
            print("Are you sure you want to call for help ?")
            confirmation = takeCommand().lower()
            if "yes" in confirmation:
                speak("I will send an email to the police station ")
                print("I will send an email to the police station")
            else:
                speak("There was no confirmation hence sos is not sent.")
                print("There was no confirmation hence sos is not sent.")
        elif "record" in statement or "recording" in statement :
            speak("starting voice recorder")
            os.system('python recorder.py')
        elif "go to sleep" in statement:
            speak("Ok sir, I will head to sleep")
            break
time.sleep(3)
