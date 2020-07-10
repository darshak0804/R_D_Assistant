import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("I am Jarvis sir.please tell me how may I help you ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:

        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ddrak123456789@gmail.com','DARSHAK@123')
    server.sendmail('ddrak123456789@gmail.com',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()




    # logic exectue tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif'open p u b g' in query:
            webbrowser.open("pubg.com")
        elif 'play music' in query:
            music_dir = 'G:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))
    
        elif 'what time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the is time is{strTime}")

        elif 'open telegram' in query:
            path = "C:\\Users\\Darshak Rakholiya\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(path)
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "darshakrakholiya@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend darshak.i am not able to send this email")

        elif 'quit' in query:
            speak("quit ")
            exit()



