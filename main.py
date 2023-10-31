import ZEN as z
import pyttsx3 as s


if __name__ == "__main__":
    z.wishme()
    while True:
        query = z.takeCommand().lower()

        if 'time' in query:
            z.time()

        elif 'date' in query:
            z.date()

        elif 'wikipedia' in query:
            z.wiki(query)

        elif 'send email' in query:
            try:
                s.speak("What should I say?")
                content = z.takeCommand()
                to='EMAIL WHERE WE WANT TO SEND IT TO'
                z.sendemail(to,content)
                s.speak("Email has been sent")

            except Exception as e:
                print(e)
                s.speak("Unable to send the email")

        elif 'search in chrome' in query:
            z.searchchrome()


        elif 'offline' in query:
            s.speak("Goodbye")
            quit()