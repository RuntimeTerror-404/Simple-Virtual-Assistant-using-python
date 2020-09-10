#text-to-speech module in python---
import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import smtplib

#import sapi5 voice assistant for windows---
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice" , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else :
        speak("good evening")

    speak("hello sir i'm Jarvis , how may i help you")

def takeCommand():
    #takes microphone input from user and gives output in string format
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try :
        print("recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("sorry, say that again...")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com')  
    server.ehlo()
    server.starttls()
    server.login("jindal8077@gmail.com" , "harshit@1234")
    server.sendmail("jindal8077@gmail.com" , to , content)

if __name__ == "__main__":
    wishMe()
    if 1 :
        
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia" , " ")
            results = wikipedia.summary(query , sentences=2)
            print(results)
            speak("According to wikipedia....")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "play music" in query:
            music_dir = "M:\\videos\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[4]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime} anything else sir...")

        elif "open code" in query:
            code_path = 'C:\\Users\\mohit\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)

        elif "email to mohit" in query:
            try :
                speak("what should i do...")
                content = takeCommand()
                to = "mohit1672002@gmail.com"
                sendEmail(to , content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry, we couldn't send email")


        

        



    
