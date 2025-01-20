import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
# Initialize speech recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    actions = {
        "google": "https://google.com",
        "facebook": "https://facebook.com",
        "youtube": "https://youtube.com",
        "linkedin": "https://linkedin.com",
    }
    
    for site, url in actions.items():
        if site in command:
            webbrowser.open(url)
            return
    speak("Please send a valid request.")

if __name__ == "__main__":
    speak("Initializing batman....")
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise once
        while True:
            print("Listening for the wake word...")
            try:
                audio = recognizer.listen(source, timeout=2)
                word = recognizer.recognize_google(audio)

                if "batman" in word.lower():
                    speak("Yes?")
                    print("Batman Active...")

                    # Listen for the name command
                    audio = recognizer.listen(source)
                    name = recognizer.recognize_google(audio).lower()

                    # Respond to specific names with commands
                    if "surya" in name:
                        speak("Hi batman! What can I do for you?")
                        audio = recognizer.listen(source)
                        surya_command = recognizer.recognize_google(audio)
                        process_command(surya_command)

                    elif "akshay" in name:
                        speak("Hi akshay! brooooo neeku project ledu dengey!")
                        audio = recognizer.listen(source)
                        vchandu_command = recognizer.recognize_google(audio)
                        process_command(vchandu_command)

                    elif "abhi" in name:
                        speak("Hi Abhi! What can I do for you?")
                        audio = recognizer.listen(source)
                        abhi_command = recognizer.recognize_google(audio)
                        process_command(abhi_command)

                    elif "chandu" in name:
                        speak("Hi Chandu! Moddagudu!")
                        audio = recognizer.listen(source)
                        chandu_command = recognizer.recognize_google(audio)
                        speak("sulla puka")
                    elif "stop" in name:
                        speak("goodbye")
                        print("bye")
                        break
                    else:
                        speak("Hi",word[-1])
                # Optional exit condition
                # if "exit" in command.lower():
                #     speak("Goodbye!")
                #     break

            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")