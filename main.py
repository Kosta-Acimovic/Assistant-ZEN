import wikipedia

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



        elif 'offline' in query:
            s.speak("Goodbye")
            quit()