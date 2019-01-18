#!/usr/bin/env python3

import time
import speech_recognition as sr
import speech_recognition as sr
from win32com.client import Dispatch
import datetime
import time

def SpeakSentence(sentence):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(sentence)

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        if (text.lower() == "hello"):
            print("Good morning")
            SpeakSentence("Good morning")
        elif(text.lower() == "good morning"):
            print("how are you doing today")
            SpeakSentence("how are you doing today")
        elif(text.lower() == "i am doing great"):
            print("good to know")
            SpeakSentence("Good to know")
        elif(text.lower() == "what time is it"):
            t = time.strftime("%I:%M:%S")
            print("The current time is ",t)
            SpeakSentence("The current time is " + str(t))
        elif(text.lower() == "who were you developed by"):
            print("I was developed by Kanishka Balaji, Pallavi Pandey, Isha Gandhi and Elsa Jerry")
            SpeakSentence("I was developed by Kanishka Balaji, Pallavi Pandey, Isha Gandhi and Elsa Jerry")
        elif(text.lower() == "what is your favourite colour"):
            print("My favourite color is blue")
            SpeakSentence("My favourite color is blue")
        elif(text.lower() == "are you a robot"):
            print("no i am not a robot. i am a virtual assistant")
            SpeakSentence("I am not a robot. I am a virtual assistant.")
        elif(text.lower() == "what is the date"):
            today = datetime.date.today()
            print("the date is: ",today)
            SpeakSentence(today)
        elif(text.lower() == "bye"):
            print("good bye")
            SpeakSentence("good bye")
    except:
        pass


def SpeakFunction():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, callback)
    while True: a = 0

if __name__ == "__main__":
    SpeakFunction()