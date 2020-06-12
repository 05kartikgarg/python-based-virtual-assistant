import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Hi there!,I am scooby. Please tell me how can I help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        #r.energy_threshold=200
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        
    
        try:
            print("Recognizing....")
            query=r.recognize_google(audio)
            print(f"user said: {query}\n")

        except Exception as e:
            print(e)
            print("Please say that again...")
            return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('opening youtube..')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google..')
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak('opening gmail..')
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir="E:\\music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is")
            speak(strtime)

        elif 'open chrome' in query:
            chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open code' in query:
            codepath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

      #  elif 'exit' or 'stop' in query:
      #      speak("bye, see you soon")
      #      exit()