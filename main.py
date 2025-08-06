import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import time

def speak(text):
    engine = pyttsx3.init('sapi5')  # Create fresh engine every time
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com")
    elif "song sunao" in c.lower() or "play song" in c.lower():
        speak("Playing a song for you.")
        webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    elif "play" in c.lower():
        song_name = c.lower().replace("play", "").strip()
        speak(f"Playing {song_name} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
        
        time.sleep(5.5)
    
        pyautogui.click(793, 404)         # Fourth click
        
        
    # else:
    #     speak("search")
    #     time.sleep(1)
    #     pyautogui.click(1286, 1048)  # Input box
    #     pyautogui.click(1286, 1048)  # Input box
    #     time.sleep(1.5)
    #     pyautogui.typewrite(c)
    #     time.sleep(0.5)
    #     pyautogui.click(1510, 949)  # Send button

speak("Initializing hello...")

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Say 'hello' to activate...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            try:
                word = recognizer.recognize_google(audio)
                print("Heard:", word)

                if word.lower() == "hello":
                    print("Hello detected!")
                    speak("Yes, how can I help you?")
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        print("Listening for your command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

            except sr.UnknownValueError:
                print("Didn't understand.")
            except sr.RequestError:
                print("Check your internet.")
    except Exception as e:
        print("Error:", e)
