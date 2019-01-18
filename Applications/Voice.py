import speech_recognition as sr
from win32com.client import Dispatch
import datetime
import time

speak = Dispatch("SAPI.SpVoice")
#Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hello how can i help you?")
    speak.Speak("Hello how can i help you?")
    audio = r.listen(source)
    while(r.recognize_google(audio) != "bye"):
        if (r.recognize_google(audio) == "hello"):
            print("Good morning")
            speak.Speak("Good morning")
            audio = r.listen(source)
        if(r.recognize_google(audio) == "good morning"):
            print("how are you doing today")
            speak.Speak("how are you doing today")
            audio = r.listen(source)
        if(r.recognize_google(audio) == "i am doing great"):
            print("good to know")
            speak.Speak("Good to know")
            audio = r.listen(source)
        if(r.recognize_google(audio) == "what time is it"):
            t = time.strftime("%I:%M:%S")
            print("The current time is ",t)
            speak.Speak(t)
            audio= r.listen(source)
        if(r.recognize_google(audio) == "who were you developed by"):
            print("I was developed by Kanishka Balaji, Pallavi Pandey, Isha Gandhi and Elsa Jerry")
            speak.Speak("I was developed by Kanishka Balaji, Pallavi Pandey, Isha Gandhi and Elsa Jerry")
            audio = r.listen(source)
        if(r.recognize_google(audio) == "what is your favourite colour"):
            print("My favourite color is blue")
            speak.Speak("My favourite color is blue")
            audio = r.listen(source)
        if(r.recognize_google(audio) == "are you a robot"):
            print("no i am not a robot. i am a virtual assistant")
            speak.Speak("I am not a robot. I am a virtual assistant.")
        if(r.recognize_google(audio) == "what is the date"):
            today = datetime.date.today()
            print("the date is: ",today)
            speak.Speak(today)
            audio = r.listen(source)
        if(r.recognize_google(audio) == "bye"):
            print("good bye")
            speak.Speak("good bye")
            audio = r.listen(source)
            break
                    
    
#Speech recognition using Google Speech Recognition

try:
    while(audio != r.recognize_google(audio) ):
        speak.Speak("You said: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    speak.Speak("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
