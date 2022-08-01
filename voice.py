import os
import speech_recognition as sr


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

        except :
            return "None"

        return statement


while True:
    wakeup = takeCommand().lower()
    if "wake up " in wakeup or "FRED" in wakeup:
        os.startfile('D:\\F.R.E.D\\Ready\\FRED.py')

    else:
        print("FRED is sleeping")
