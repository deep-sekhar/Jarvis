# PACKAGES NEEDED 

# -------------------------------
import os
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from Commands.wiki import wikisearch
from Commands.all_paths import all_paths
import subprocess
# import pyaudio
# -------------------------------

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
        #     # cmmd = ' '.join(list(filter(jcmd,)))
        #     cmmd  = cmmd.split(' ')  
        #     cmmd = ' '.join([word for word in cmmd if word != "jarvis"])
        # else: 
        #     cmmd = ""
    
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

        elif cmmd == "update working folders":
            cpath = (str)(os.getcwd())
            # print(type(cpath))
            cauto = cpath+r'\automated.bat'
            # print(cauto)
            gfiles = all_paths.gitpaths
            for gpath in gfiles:
                os.chdir(gpath)
                os.startfile(cauto)
            os.chdir(cpath)
            speak("All git directories have been pushed to their respective repos")

        elif cmmd == "update your codebase":
            os.startfile('automated.bat')
            speak("My codebase has been updated")
            
        elif cmmd == "shutdown":
            speak("Have a nice day, Sir!")
            break

