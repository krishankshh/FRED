import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

        try:
            duration = r.recognize_google(audio, language='en-in')
            print(f"user said:{duration}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return duration


speak("For how long do you want to record in minutes.")

freq = 44100
duration = int(takeCommand().lower())
dur = duration*60
speak("Starting voice recording now....")
recording = sd.rec(int(dur * freq),
                   samplerate=freq, channels=2)
sd.wait()
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2)
print("Completed recording voice, returning to main program of FRED")
speak("Completed recording voice, returning to main program of FRED")
os.system('python FRED.py')