import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('Say Something...')
        audio = r.listen(source, timeout=2)
        try:
            text = r.recognize_google(audio)
            if str(text).lower() == "exit":
                break
            tb = TextBlob(text)
            print(text)
            print(tb.sentiment)
        except sr.UnknownValueError:
            print('Could not understand audio')
        except sr.RequestError as e:
            print(f'Error fetching results from Google Speech Recognition service; {e}')
        except Exception as e:
            print(f'Error: {e}')
            print('Try again')
