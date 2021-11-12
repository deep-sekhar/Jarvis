# PACKAGES NEEDED 
import os
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from Commands.wiki import wikisearch
from Commands.all_paths import all_paths
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
        speak("Good Morning Sir")
    elif(h<19):
        speak("Good Evening Sir")

def takecommand():
    """ microphone command from user"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.energy_threshold = 400
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

    while True:
        cmmd = takecommand().lower()

        # if "jarvis" in cmmd:
        #     cmmd = cmmd.replace("jarvis","")  
        # else: 
        #     continue
    
        if "wikipedia" in cmmd:
            wikisearch(cmmd)

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
            os.startfile(all_paths.vspath)

        elif cmmd == "update all working folders":
            gfiles = all_paths.gitpaths;
            for gpath in gfiles:
                os.startfile(gpath)
            speak("All git directories have been pushed to their respective repos")

        elif cmmd == "shutdown":
            speak("Have a nice day, Sir!")
            break
