import ZEN as z


if __name__ == "__main__":
    z.wishme()
    while True:
        query = z.takeCommand().lower()

        if 'time' in query:
            z.time()

        elif 'date' in query:
            z.date()