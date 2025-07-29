import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyjokes
import subprocess
import time
import pyautogui
import sys
import socket


import random
def rock():
    you = int(input("please enter your choice:-\n 1-Rock \n 2-Paper \n 3-Scissor \n"))
    shapes = {1:'rock',2:'paper',3:'scissor'}
    if you not in shapes:
        print("please enter a valid choice")
        exit()
    comp=random.randint(1,3)
    print("you choose",you)
    print("computer choose",comp)
    if (you==1) and (comp==3) or (you==2) and (comp==1) or (you==3) and (comp==2):
        speak("Congratulations! You Won!")
    elif (you==comp):
        speak("Match tied")
    else:
        speak("Sorry! You loose!")

#import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source,timeout=8,phrase_time_limit=10)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            speak("Unable to recognize your voice...")
            return "None"
        return query
def username():
    speak("What should I call you sir ?")
    uname=takeCommand()
    speak("Welcome "+uname)
    speak("how can i help you sir ?")
def wishme():
    speak("Good Afternoon  ")
    speak("I am your virtual assistant . ")
if __name__=='__main__':
    wishme()
    username()
    while True:
        order=takeCommand().lower()

        if 'how are you' in order:
            speak("I am fine Thank you")
            speak("How are you sir?")

        elif 'fine' in order or 'good' in order:
            speak("its good to know that you are fine")

        elif 'who i am' in order:
            speak("if you can talk then surely you are a human ")

        elif 'who are you' in order:
            speak("i am your virtual assistant")

        elif 'what is your name' in order:
            speak("my friendd called me Emma")

        elif 'open notepad' in order:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif 'open chrome' in order:
            npath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)

        elif 'wikipedia' in order or 'tell me about' in order:
            speak("searching wikipedia...")
            order=order.replace('wikipedia','')
            result=wikipedia.summary(order,sentences=2)
            speak("According to Wikipedia")
            speak(result)

        elif 'open google' in order:
            speak("here you go to google .")
            webbrowser.open("google.com")

        elif 'open myntra' in order:
            speak("here you go to myntra sir , happy shopping")
            webbrowser.open("myntra.com")

        elif 'open youtube' in order:
            speak("here you go to youtube")
            webbrowser.open("youtube.com")

        elif 'open amazon' in order:
            speak("here you go to amazon , happy shopping")
            webbrowser.open("amazon.com")

        elif 'open jdiet website' in order:
            speak("here you go to jdiet website")
            webbrowser.open("https://www.jdiet.ac.in")

        elif 'open geekforgeek' in order:
            speak("here you go to greekforgeek")
            webbrowser.open("geeksforgeeks.com")

        elif 'where is' in order:
            order=order.replace('where is','')
            location=order
            speak("locating.....")
            speak("location")
            webbrowser.open("https://google.co.in/maps/place/"+location+"")

        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en" , category="neutral"))

        elif 'the time' in order:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well,The time is {strTime}")

        elif 'shutdown' in order or 'turn off' in order:
            speak("Hold on a second ! your system is on its way to shutdown")
            speak("make sure that all of your application is close")
            time.sleep(5)
            subprocess.call(['shutdown','/s'])

        elif 'restart' in order:
            subprocess.call(['shutdown','/r'])

        elif 'hibernate' in order:
            speak("Hibernating")
            subprocess.call(['shutdown','/h'])

        elif 'log off' in order or 'sign out' in order:
            speak("make sure all of your application is close before sign out")
            time.sleep(5)
            subprocess.call(['shutdown','/i'])

        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        #elif 'take a screenshot' in order or 'screen shot this ' in order:
            #speak('please tell me the name for this file')
            #name=takeCommand().lower()
            #speak('please hold the screen')
           # time.sleep(3)
            #img=pyautogui.screenshot()
            #img.save(f"{name}.png")
            #speak('screenshot captured')
            #speak('screenshot saved')

        elif 'exit' in order or 'quit' in order or 'stop' in order:
            speak("Thank you for using me. Have a good day")
            sys.exit()

      

        elif 'bmi' in order:
            speak("please tell your height in centimeters")
            height=takeCommand()
            speak("please tell your weight in kilograms ")
            weight=takeCommand()
            height =float(height)/100
            BMI = float(weight)/(height*height)
            speak("your Body Mass Index is "+str(BMI))
            if (BMI>0):
                if(BMI<=16):
                    speak("you are severly underweight")
                elif(BMI <=18.5):
                    speak("you are underweight")
                elif(BMI <=25):
                    speak("you are healthy")
                elif(BMI <=30):
                    speak("you are overweight")
                else:
                    speak("you are severly overweight")
            else:
                speak("Give valid details")
        elif 'date' in order or 'what is today date' in order or 'what is today date' in order:
            today_date = datetime.date.today().strftime("%A, %B %d, %Y")
            speak(f"Today's date is {today_date}")



        elif 'rock' in order:
            rock()
