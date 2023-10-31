import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb

Lady_english="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine = pyttsx3.init()

engine.setProperty('volume',1)
engine.setProperty('voice', Lady_english)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    else:
        month = "December"

    day = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back!")
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    elif 18 <= hour < 24:
        speak("Good evening!")
    else:
        speak("Good night!")

    speak("ZEN at your service. Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query


def wiki(x):
    speak("Searching....")
    x = x.replace("wikipedia", "")
    try:
        result = wikipedia.summary(x, sentences=2)
        print(result)
        speak(result)
    except Exception as e:
        print(e)
        speak("Please try again")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('OUR EMAIL','PASSWORD FOR THAT EMAIL')
    server.sendmail('zentestingai@gmail.com', to, content)
    server.close()

def searchchrome():
    speak("What should i search?")
    chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    search = takeCommand().lower()
    if search!="none":
        wb.get(chromepath).open_new_tab(search + '.com')
        return
    else:
        searchchrome()

