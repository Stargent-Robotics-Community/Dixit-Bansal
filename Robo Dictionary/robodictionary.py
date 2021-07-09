import pyttsx3
import speech_recognition as sr
from PyDictionary import PyDictionary



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
        return "please say again"
    return query


engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Hello sir,i am your robodictionary please tell me the word you want to search.")
while True:
    query=takecommand().lower()
    d=PyDictionary(query)
    print(f"you said {query}")
    if query in d:
        print("searching..")
        print(d.getMeanings())
        speak(d.getMeanings())
    else:
        speak("meaning not found")
    speak("sir,if you want to search another word?")
    ans=takecommand().lower()
    print(f"you said {ans}")
    speak("ok")
    if "no" in ans:
        quit()