import speech_recognition as sr
import webbrowser
import pyttsx3
import streamlit 
import openai

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8


def speak(text):
    print(f"Batman: {text}")

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


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
            speak(f"Opening {site}")
            webbrowser.open(url)
            return

    speak("Please send a valid request.")


if __name__ == "__main__":

    try:

        speak("Initializing Batman")

        with sr.Microphone() as source:

            print("Adjusting microphone for ambient noise...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Microphone ready!")

        speak("Batman is ready")

        while True:

            print("\n================================")
            print("Listening for the wake word...")
            print("Say: Batman")
            print("================================")

            try:

                with sr.Microphone() as source:

                    audio = recognizer.listen(
                        source,
                        timeout=10,
                        phrase_time_limit=5
                    )

                word = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                ).lower()

                print(f"You said: {word}")

            except sr.WaitTimeoutError:

                print("No speech detected.")
                continue

            except sr.UnknownValueError:

                print("Sorry, I did not understand that.")
                continue

            except sr.RequestError as e:

                print(f"Could not request results; {e}")
                continue


            # Batman + stop in one sentence

            if (
                ("batman" in word or "bad man" in word)
                and
                (
                    "stop" in word
                    or "exit" in word
                    or "shutdown" in word
                )
            ):

                speak("Goodbye")

                print("Batman shutting down...")

                break


            # Batman wake word

            if "batman" in word or "bad man" in word:

                speak("Yes?")

                print("Batman Active...")
                print("What is your name?")

                try:

                    with sr.Microphone() as source:

                        audio = recognizer.listen(
                            source,
                            timeout=8,
                            phrase_time_limit=5
                        )

                    name = recognizer.recognize_google(
                        audio,
                        language="en-IN"
                    ).lower()

                    print(f"You said: {name}")

                except sr.WaitTimeoutError:

                    print("No name detected.")
                    continue

                except sr.UnknownValueError:

                    print("Could not understand the name.")
                    continue

                except sr.RequestError as e:

                    print(f"Could not request results; {e}")
                    continue


                # Stop after Batman

                if (
                    "stop" in name
                    or "exit" in name
                    or "shutdown" in name
                ):

                    speak("Goodbye")

                    print("Batman shutting down...")

                    break


                # Surya

                if "surya" in name:

                    speak(
                        "Hi Surya! What can I do for you?"
                    )

                    print("Listening for Surya's command...")

                    try:

                        with sr.Microphone() as source:

                            audio = recognizer.listen(
                                source,
                                timeout=8,
                                phrase_time_limit=8
                            )

                        command = recognizer.recognize_google(
                            audio,
                            language="en-IN"
                        )

                        print(f"Command: {command}")

                        process_command(command)

                    except sr.UnknownValueError:

                        print("Could not understand command.")

                    except sr.WaitTimeoutError:

                        print("No command detected.")

                    except sr.RequestError as e:

                        print(f"Could not request results; {e}")


                # Akshay

                elif "akshay" in name:

                    speak(
                        "Hi Akshay! Brooooo neeku project ledu dengey!"
                    )

                    print("Listening for Akshay's command...")

                    try:

                        with sr.Microphone() as source:

                            audio = recognizer.listen(
                                source,
                                timeout=8,
                                phrase_time_limit=8
                            )

                        command = recognizer.recognize_google(
                            audio,
                            language="en-IN"
                        )

                        print(f"Command: {command}")

                        process_command(command)

                    except sr.UnknownValueError:

                        print("Could not understand command.")

                    except sr.WaitTimeoutError:

                        print("No command detected.")

                    except sr.RequestError as e:

                        print(f"Could not request results; {e}")


                # Abhi

                elif "abhi" in name:

                    speak(
                        "Hi Abhi! What can I do for you?"
                    )

                    print("Listening for Abhi's command...")

                    try:

                        with sr.Microphone() as source:

                            audio = recognizer.listen(
                                source,
                                timeout=8,
                                phrase_time_limit=8
                            )

                        command = recognizer.recognize_google(
                            audio,
                            language="en-IN"
                        )

                        print(f"Command: {command}")

                        process_command(command)

                    except sr.UnknownValueError:

                        print("Could not understand command.")

                    except sr.WaitTimeoutError:

                        print("No command detected.")

                    except sr.RequestError as e:

                        print(f"Could not request results; {e}")


                # Chandu

                elif "chandu" in name:

                    speak(
                        "Hi Chandu! Moddagudu!"
                    )

                    print("Listening for Chandu's command...")

                    try:

                        with sr.Microphone() as source:

                            audio = recognizer.listen(
                                source,
                                timeout=8,
                                phrase_time_limit=8
                            )

                        command = recognizer.recognize_google(
                            audio,
                            language="en-IN"
                        )

                        print(f"Command: {command}")

                        speak("sulla puka")

                    except sr.UnknownValueError:

                        print("Could not understand command.")

                    except sr.WaitTimeoutError:

                        print("No command detected.")

                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
                elif "sumit" in name:

                    speak(
                        "Anda Gandu! Dekh code run ho raha hai"
                    )


                # Ankit

                elif "ankit" in name:

                    speak(
                        "Dekh re Anda Code kaise run ho raha hai!"
                    )


                # Unknown name

                else:

                    name_split = name.split(" ")

                    speak(
                        f"Hello! {name_split[-1]}"
                    )


    except KeyboardInterrupt:

        print("\nBatman stopped.")

    except Exception as e:

        print("\n================================")
        print("ERROR")
        print("================================")
        print(e)