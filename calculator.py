import operator
import os
import time

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
r = sr.Recognizer()
my_mic_device = sr.Microphone()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

if __name__ == '__main__':
    while True:
        print("Say what you want to calculate")
        speak("Say what you want to calculate")
        statement: str = takeCommand().lower()
        if "1" in statement or "1" in statement or "2" in statement or "3" in statement or "4" in statement or"5" in statement or "6" in statement or "7" in statement or "8" in statement or "9" in statement or "0" in statement :
            with my_mic_device as source:
                speak('Please repeat')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try :
                statement = r.recognize_google(audio,language='en-in')
                speak('Sorry i could not get that')
            except :
                print(statement)
                speak(statement)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(statement.split())))
                speak(eval_binary_expr(*(statement.split())))

        elif " return " in statement or "stop" in statement or "that's it" in statement:
            speak("Going back to FRED")
            print("Going back to FRED")
#            if " yes " in statement :
            os.system('python FRED.py')
#           if " no " in statement :
#                continue
time.sleep(3)