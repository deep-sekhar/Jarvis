# PACKAGES NEEDED 
import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    h = int(datetime.datetime.now().hour)
    if(h>=0 and h<12):
        speak("Good Morninig Sir")
    elif(h<19):
        speak("Good Evening Sir")
    # else:
    #     speak("Good night Sir")

def takecommand():
    """ microphone command from user"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold =1 
        audio = r.listen(source)
    try:
        print("processing")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said --{query}\n")
    except Exception as e :
        # print(e)
        print("say again please")
        return "None"

    return query

if __name__ == "__main__":

    speak("All Systems online!")
    wishme()
    cmmd = takecommand().lower()
    
    if "wikipedia" in cmmd:
        speak("Searching wikipedia")
        query = cmmd.replace("search for","")
        query = query.replace("in wikipedia","")

        try:
            results = wikipedia.summary(query,2)
            speak("Here is what I found  "+ results)
        except Exception as e :
            speak("could not find anything relevant in wikipedia Sir")

    elif cmmd == "open youtube":
        webbrowser.open("youtube.com")

    elif "on youtube" in cmmd:
        query = cmmd.replace("search for","")
        query = cmmd.replace("on youtube","")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif cmmd == "what is time now":
        tm = datetime.datetime.now().strftime("%H:%M")
        speak(f"currently it is {tm}")

    elif cmmd == "open code":
        vspath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vspath)

