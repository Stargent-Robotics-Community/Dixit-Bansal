import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognising...")
        query=r.recognize_google(audio,language='en-in')
    except:
        return "cant hear,please say again!!!"
    return query


engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("hello i am jarvis how may i help you?")
speak("there's a lot i can help with" + "here are a few populer actions")
print('"open youtube"\n"open facebook"\n"open google"\n"current time"\n"current day"')
while True:
    query=takecommand().lower()
    print(f"{query}")
    if "how are you " in query:
        speak("i am fine how about you? ")
        reply=takecommand().lower()
        if "i am" in reply:
            speak("okay")
    elif "who create" in query:
        speak("i am programmed by Dixit Bansal")
    elif "youtube" in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")
    elif "google" in query:
        speak("opening google")
        webbrowser.open("www.google.com")
    elif "facebook" in query:
        speak("opening facebook")
        webbrowser.open("facebook.com")
    elif "date" in query:
        cd=str(datetime.datetime.now().strftime("%B %d %Y"))
        engine.setProperty("rate",130)
        speak(cd)
    elif "day" in query:
        cd=str(datetime.datetime.now().strftime("%A"))
        engine.setProperty("rate",130)
        speak(cd)
    elif "time" in query:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))
    else:
        speak("do you want to ask more?")
        ans=takecommand().lower()
        if "no" in ans:
            quit()
        

