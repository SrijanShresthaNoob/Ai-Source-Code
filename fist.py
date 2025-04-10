import pyttsx3 
import speech_recognition as sr 
import datetime 
import webbrowser
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning boss!")

    elif hour>=12 and hour<18:
        speak("welcome back boss!")   

    else:
        speak("Good Evening boss!")  



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("C:\\Users\\user\\Desktop\\development\\my projects\\online.mp3")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        playsound("C:\\Users\\user\\Desktop\\development\\my projects\\no.mp3")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'say' in query:
            query = query.replace("say","")
            print(query)
            speak(query)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            playsound("C:\\Users\\user\\Desktop\\development\\my projects\\offline.mp3")
            exit()

        elif 'open google' in query:
            print("opening google........")
            speak("opening google")
            webbrowser.open("www.google.com")

        elif 'open messenger' in query:
            print("opening messanger.....")
            speak("opening messanger")
            webbrowser.open("https://www.messenger.com/")

        elif 'open facebook' in query:
            print("opening facebook....")
            speak("opening facebook")
            webbrowser.open("www.facebook.com")

        elif 'open youtube' in query:
            print("opening youtube....")
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'play' in query:
            print("playing on youtube...")
            speak("playing on youtube")
            query = query.replace("play","")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        
        elif 'rick roll' in query:
            speak("haha..")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        elif 'i love you' in query:
            playsound("C:\\Users\\user\\Desktop\\development\\my projects\\care.mp3")

        elif 'can you sing' in query:
            yes = "No, I can compose music inseted, wait I'll show you."
            print(yes)
            speak(yes)
            playsound("C:\\Users\\user\\Desktop\\development\\my projects\\reco.mp3")

        elif 'you are rude' in query:
            playsound("C:\\Users\\user\\Desktop\\development\\my projects\\man-screaming-memes-sound-effect-2020-for-pro-content-creators_HU6teNC.mp3")
            print("you are not my friend now...")
            playsound("C:\\Users\\user\\Desktop\\development\\my projects\\i-dont-wanna-talk-about-it.mp3")
            exit()

        elif 'introduce yourself' in query:
            speak("Hi, i am Pushpa, Nice to meet you. i am created by Mr.Srijan Shrestha.")
            print("Hi, i am Pushpa, Nice to meet you. i am created by Mr.Srijan Shrestha.")

        elif 'tere ko' in query:
            print("Mula sag ")
            speak("mula sag")

        elif 'nice' in query:
            print("Thanks for the compliment.")
            speak("Thanks for the compliment.")