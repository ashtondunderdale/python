import speech_recognition as sr
import pyttsx3 # for text to speech
import webbrowser
import requests
from bs4 import BeautifulSoup

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
    
        if query[1] == "hello":
            speak("Greetings, Ashton.")

        elif query[1] == "say":
            textToSpeak = ' '.join(query[2:])
            speak(f"{textToSpeak}")

        elif query[1] == "terminate":
            speak("Shutting Down")
            exit()

        elif query[1] == "search":
            searchQuery = ' '.join(query[2:])
            url = f"https://www.dictionary.com/browse/{searchQuery}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                definition = soup.find("div", class_="default-content").find("span").text
                speak(f"The definition of {searchQuery} is: {definition}")
            except:
                speak(f"Sorry, I could not find a definition for {searchQuery}.")
