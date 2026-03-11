import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Sorry, could not understand.")
        return ""

def run_assistant():
    speak("Hello, I am your voice assistant. How can I help you")

    while True:
        command = take_command()

        if command == "":
            continue

        # TIME
        if "time" in command or "clock" in command:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            print("Time:", current_time)
            speak("The time is " + current_time)

        # DATE
        elif "date" in command or "day" in command or "today" in command:
            now = datetime.datetime.now()
            today_date = now.strftime("%d %B %Y")
            print("Date:", today_date)
            speak("Today's date is " + today_date)

        # OPEN YOUTUBE
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        # OPEN GOOGLE
        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        # WIKIPEDIA SEARCH
        elif "wikipedia" in command:
            speak("Searching Wikipedia")
            topic = command.replace("wikipedia", "")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I could not find information")

        # PLAY SONG
        elif "play" in command:
            song = command.replace("play", "")
            speak("Playing " + song)
            pywhatkit.playonyt(song)

        # EXIT PROGRAM
        elif "stop" in command or "exit" in command:
            speak("Goodbye")
            break

if __name__ == "__main__":
    run_assistant()