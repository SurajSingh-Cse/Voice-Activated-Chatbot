# Enhanced Jarvis Voice Assistant

import pyttsx3
import speech_recognition as sr
import os
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import openai
import openai_request as ai
import user_config
import ctypes
import subprocess

engine = pyttsx3.init(driverName='sapi5')  # For Windows systems
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)

def speak(audio):
    print("Jarvis: " + audio)
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content.strip() == "":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            content = r.recognize_google(audio, language='en-in')
            content = content.lower()
            print("You Said....." + content)
        except Exception as e:
            print("Please try again.....")
            speak("Sorry, please say that again.")
            content = " "
    return content

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, your voice assistant. How may I help you?")

def main_process():
    wishMe()
    while True:
        request = command().lower()

        if "jarvis" in request:
            speak("Yes, I am listening")

        elif "play music" in request:
            speak("Playing music")
            music_path = os.path.join(os.environ["USERPROFILE"], "Music")
            try:
                songs = os.listdir(music_path)
                if songs:
                    os.startfile(os.path.join(music_path, songs[0]))
                else:
                    speak("No music files found in Music folder.")
            except:
                speak("Error opening music folder.")

        elif "say time" in request or "what is the time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {now_time}")

        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task:
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "show task" in request:
            speak("Here are your tasks")
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read()
                    print("Tasks:\n", tasks)
                notification.notify(title="Your Tasks", message=tasks)
            except:
                speak("No tasks found.")

        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "open google" in request:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "open" in request:
            app = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(app)
            pyautogui.sleep(1)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            speak("Searching Wikipedia...")
            query = request.replace("search wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("Could not find results on Wikipedia")

        elif "search google" in request:
            query = request.replace("search google", "").strip()
            webbrowser.open("https://www.google.com/search?q=" + query)
            speak("Searching Google for " + query)

        elif "screenshot" in request:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved.")

        elif "ask ai" in request:
            question = request.replace("ask ai", "").strip()
            print("Request to AI:", question)
            response = ai.send_request(question)
            print("AI Response:", response)
            speak(response)

        elif "shutdown" in request:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")

        elif "restart" in request:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")

        elif "lock screen" in request:
            speak("Locking the system.")
            ctypes.windll.user32.LockWorkStation()

        elif "write a note" in request:
            speak("What should I write?")
            note = command()
            with open("note.txt", "w") as f:
                f.write(note)
            speak("Note saved.")

        elif "read note" in request:
            try:
                with open("note.txt", "r") as f:
                    note = f.read()
                    speak("Here is your note.")
                    speak(note)
            except:
                speak("No note found.")

        elif "exit" in request or "quit" in request:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that. Please try again.")

            
if __name__ == "__main__":
    try:
        main_process()
    finally:
        engine.stop()  # Cleanup pyttsx3 engine to prevent exit error



# goodbye
#jarvis
#play music
#say time
#new task
#show task
#open youtube
#open google
#open <app_name>
#wikipedia <search_term>
#search google <query>
#screenshot
#ask ai <question>
#shutdown
#restart
#lock screen
#write a note
#read note
#exit
#quit
