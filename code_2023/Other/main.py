import speech_recognition as sr
import pyttsx3 # for text to speech

# speech engine initilisation
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) # 0 - male, 1 - female
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
        print("Recognizing speech...")
        query = listener.recognize_google(inputSpeech, language="en_gb")
        print(f"The input speech was: {query}")
    except Exception as exception:
        print("I did not quite catch that")
        speak("I did not quite catch that")
        print(exception)
        return "None"
    
    return query

# main loop
if __name__ == "__main__":
    speak("System Online")

    while True:
        # Parse as a list
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