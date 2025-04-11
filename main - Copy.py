import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import os
import handlewikipedia
import handleyoutube
import handlechatgpt
import handlingsteam

# Initialize the speech engine once
engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")

def get_temperature():
    speak("Opening weather website...")
    webbrowser.open("https://weather.com")

def get_latest_news():
    speak("Opening latest news...")
    webbrowser.open("https://news.google.com")

def tell_jokes():
    speak("Opening jokes website...")
    webbrowser.open("https://www.reddit.com/r/Jokes")

def process_command(command):
    command = command.lower()

    commands = {
        "how are you": "I am fine sir, what about you?",
        "kesa hai bhai": "Mai badiya hu sir",
        "kya haal hai bhai": "Mai badiya hu sir",
        "tu kitna harami hai": "Rukh, teri mummy ko bolta hu",
        "open google": "Opening Google...",
        "open youtube": "Opening YouTube...",
        "open epic games": "Opening Epic Games...",
        "open telegram": "Opening Telegram...",
        "tell me the time": tell_time,
        "what's the temperature": get_temperature,
        "latest news": get_latest_news,
        "tell me a joke": tell_jokes
    }

    for key, response in commands.items():
        if key in command:
            if callable(response):
                response()
            else:
                speak(response)
                if "open" in key:
                    webbrowser.open({"open google": "https://google.com",
                                     "open youtube": "https://www.youtube.com",
                                     "open epic games": "https://epicgames.com",
                                     "open telegram": "https://web.telegram.org/k/"}.get(key))
            return

    if "search on google" in command:
        speak("What do you want to search for?")
        query = get_user_input()
        search_query = '+'.join(query.split())
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "search on youtube" in command:
        speak("What would you like to search, sir?")
        query = get_user_input()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif "information" in command:
        speak("What would you like to know, sir?")
        query = get_user_input()
        speak(f"Searching {query} on Wikipedia")
        assist = handlewikipedia.Inflow()
        assist.get_info(query)

    elif "open spotify" in command:
        speak("Opening Spotify...")
        try:
            os.startfile("C:\\Users\\skmub\\AppData\\Roaming\\Spotify\\Spotify.exe")
        except Exception as e:
            speak("Unable to open Spotify.")
            print(f"Error: {e}")

    elif "play " in command:
        speak("What would you like to play, sir?")
        query = get_user_input()
        speak(f"Playing {query} on YouTube")
        assist = handleyoutube.Inflow()
        assist.get_info(query)

    elif "games" in command or "game" in command:
        speak("What game would you like to search, sir?")
        ans = get_user_input()
        speak(f"Searching {ans} on Steam")
        assist = handlingsteam.Inflow()
        assist.get_info(ans)

    elif "chat" in command.lower():
        speak("What do you want to chat with, sir?")
        ans = get_user_input()
        speak("Giving query to ChatGPT")
        assist = handlechatgpt.Inflow()
        assist.get_info(ans)

    elif "exit" in command or "stop" or "by" in command:
        speak("Goodbye, sir!")
        exit()
    else:
        speak("I did not understand the command.")

def get_user_input():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Could not request results from Google Speech Recognition service.")
        return ""

def listen_for_wake_word():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5)
                command = r.recognize_google(audio)
                if "jarvis" in command.lower():
                    speak("Yes sir, how may I help you?")
                    process_commands()
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                speak("Could not request results from Google Speech Recognition service.")
            except Exception as e:
                print(f"Error: {e}")
                

def process_commands():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Listening for command...")
                audio = r.listen(source, timeout=5)
                command = r.recognize_google(audio)
                if command:
                    print(f"Command: {command}")
                    process_command(command)
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                speak("Could not request results from Google Speech Recognition service.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    speak("Hello sir, Jarvis here")
    listen_for_wake_word()
