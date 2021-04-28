import speech_recognition as sr #For user speech to text
import pyttsx3 #For text to speech
import datetime #for telling the date and time
import wikipedia # for acessing info from wikipedia
import webbrowser #for accessing web
import time #for time display
import playsound
import os #some os(Operating System) functions
import subprocess #spawn new processes, connect to their input/output/error pipe
import json #work with JSON(JavaScript Object Notation) data
import requests #proccessing requests
import smtplib #Sending emails

print('Loading your AI personal assistant - BusiBot....')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello , Good Morning , I am BusiBot !  how may I help you ?")
        print("Hello , Good Morning , I am BusiBot !  how may I help you ?")
    elif hour>=12 and hour<18:
        speak("Hello , Good Afternoon , I am BusiBot !  how may I help you ?")
        print("Hello , Good Afternoon , I am BusiBot !  how may I help you ?")
    else:
        speak("Hello , Good Evening , I am BusiBot !  how may I help you ?")
        print("Hello , Good Evening , I am BusiBot !  how may I help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
            speak("Pardon me, I didn't get that , please say that again")
            return "None"
        return query
            
speak("Loading your AI  assistant BusiBot")
wishMe()


if __name__=='__main__':


    while True:
        query = takeCommand().lower()
        if query==0:
            continue

        if  "stop" in query:
            speak('BusiBot V1.0.0.1 closing....')
            print('BusiBot V1.0.0.1 closing....')
            break



        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome opened !")
            time.sleep(5)

        elif 'why are small and medium businesses so important' in query:
            speak("Micro, small and medium Enterprises (MSMEs) are the growth accelerators of the Indian economy, contributing about 30 percent of the country’s gross domestic product (GDP).")
            time.sleep(5)
            


        elif  'what can you do' in query:
            speak(" I am a AI bot in which I can give solutions  , suggestions and ideas depending upon the feeded  MSME's Sector ")

        elif "open MSME Government Portal" in query:
            webbrowser.open_new_tab("msme.gov.in")
            speak("Here is the official portal of MSME's by the Indian Government!")
            
        elif "open market news Portal" in query:
            webbrowser.open_new_tab("https://in.finance.yahoo.com/")
            
time.sleep(3)