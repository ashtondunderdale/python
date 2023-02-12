import speech_recognition as sr
import pyttsx3 # for text to speech
import webbrowser
import requests
from bs4 import BeautifulSoup
import time
import math
import json # for jokes

# speech engine initilisation
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
activationWord = "computer"

def speak(text, rate = 120):
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():

    listener = sr.Recognizer()
    print("Awaiting command input")

    with sr.Microphone() as source:
        listener.pauseThreshold = 2
        inputSpeech = listener.listen(source)

    try:
        print("Processing Speech...")
        query = listener.recognize_google(inputSpeech, language="en_gb")
        print(f"The input speech was: {query}")
    except Exception as exception:
        speak("I could not understand that")
        print(exception)
        return "None"
    
    return query

if __name__ == "__main__":
    speak("System Online")

while True:
    query = parseCommand().lower().split()

    if query[0] == "computer":
    
        if query[1] == "hello": # greetings command
            speak("Greetings, Ashton.")

        elif query[1] == "thank": # thank you command
            if "you" in query[2:] or "thanks" in query[2:]:
                speak("You're very welcome, Ashton.")

        elif query[1] == "say": # repeat query command
            textToSpeak = ' '.join(query[2:])
            speak(f"{textToSpeak}")

        elif query[1] == "terminate": # exit command
            speak("Shutting Down")
            exit()

        elif query[1] == "search": # search query command
            searchQuery = ' '.join(query[2:])
            webbrowser.open(f"https://www.google.com/search?q={searchQuery}")

        elif query[1] == "define": # define query command
            searchQuery = ' '.join(query[2:])
            url = f"https://www.dictionary.com/browse/{searchQuery}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                definition = soup.find("div", class_="default-content").find("span").text
                speak(f"The definition of {searchQuery} is: {definition}")
            except:
                speak(f"Sorry, I could not find a definition for {searchQuery}.")

        elif query[1] == "help": # help command
            speak("Here is a list of commands I can perform. Say command - i will repeat whatever you tell me to. Terminate command - i will shut myself down. Search command - I will search for a query of your choice. Define command - I will define a word for you.")
            exit()

        elif query[1] == "calculate": # calculate command
            expression = ' '.join(query[2:])
            expression = expression.replace("asterisk", "*").replace("x", "*") # allows the computer to perform multiplication
            try:
                result = eval(expression)
                speak(f"The result of {expression} is {result}")
            except:
                speak("Sorry, I could not evaluate that expression.")

        elif query[1] == "timer": # timer command
            try:
                seconds = int(query[2])
                speak(f"Timer set for {seconds} seconds.")
                time.sleep(seconds)
                speak("Timer is up.")
            except:
                speak("Sorry, I could not set the timer.")

        elif "list" in query and "pi" in query: # list pi command
                digits = int(''.join(filter(str.isdigit, ' '.join(query)))) # extract number of digits from query
                if digits > 25:
                    speak("I'm sorry, I can't list that many digits of pi. Well actually, i could, i just dont want to.")
                else:
                    pi = str(math.pi)
                    speak(f"Here are the first {digits} digits of pi: {pi[:1]}.{pi[1:digits+1]}")

        elif query[1] == "joke":
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url)
            data = json.loads(response.text)
            setup = data['setup']
            punchline = data['punchline']
            joke = f"{setup} ... {punchline}"
            speak(joke)

        else:
            speak("Sorry, I dont recognise that command.")
        