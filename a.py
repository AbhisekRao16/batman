import speech_recognition as sr
import webbrowser
import pyttsx3


# ==========================================
# INITIALIZE SPEECH RECOGNIZER
# ==========================================

recognizer = sr.Recognizer()

# Helps recognize speech with small pauses
recognizer.pause_threshold = 0.8


# ==========================================
# TEXT TO SPEECH
# ==========================================

def speak(text):
    print(f"Batman: {text}")

    # Create a fresh TTS engine every time
    # This fixes the microphone + pyttsx3 issue
    engine = pyttsx3.init()

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()


# ==========================================
# PROCESS COMMAND
# ==========================================

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


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    speak("Initializing Batman")
    try:

        # ======================================
        # MICROPHONE
        # ======================================

        with sr.Microphone() as source:

            print("Adjusting microphone for ambient noise...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Microphone ready!")

        speak("Batman is ready")


        # ======================================
        # CONTINUOUS BATMAN LOOP
        # ======================================

        while True:

            print("\n================================")
            print("Listening for the wake word...")
            print("Say: Batman")
            print("================================")


            # ==================================
            # LISTEN FOR BATMAN
            # ==================================

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
                )

                word = word.lower()

                print(f"You said: {word}")


            except sr.WaitTimeoutError:

                print("No speech detected.")
                continue


            except sr.UnknownValueError:

                print("Could not understand.")
                continue


            except sr.RequestError as e:

                print(f"Speech recognition error: {e}")
                continue


            # ==================================
            # BATMAN WAKE WORD
            # ==================================

            if "batman" in word or "bad man" in word:

                speak("Yes?")

                print("Batman Active!")
                print("Waiting for name...")


                # ==================================
                # LISTEN FOR NAME
                # ==================================

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
                    )

                    name = name.lower()

                    print(f"You said: {name}")


                except sr.WaitTimeoutError:

                    print("No name detected.")
                    continue


                except sr.UnknownValueError:

                    print("Could not understand the name.")
                    continue


                except sr.RequestError as e:

                    print(f"Speech recognition error: {e}")
                    continue


                # ==================================
                # SURYA
                # ==================================

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


                # ==================================
                # AKSHAY
                # ==================================

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


                # ==================================
                # ABHI
                # ==================================

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


                # ==================================
                # CHANDU
                # ==================================

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


                # ==================================
                # SUMIT
                # ==================================

                elif "sumit" in name:

                    speak(
                        "Anda Gandu! Dekh code run ho raha hai"
                    )


                # ==================================
                # ANKIT
                # ==================================

                elif "ankit" in name:

                    speak(
                        "Dekh re Anda Code kaise run ho raha hai!"
                    )


                # ==================================
                # STOP
                # ==================================

                elif "stop" in name:

                    speak("Goodbye!")

                    print("Batman shutting down...")

                    break


                # ==================================
                # UNKNOWN NAME
                # ==================================

                else:
                    name_split=name.split(" ")
                    speak(f"Hello! {name_split[-1]}")

    except Exception as e:
        print("\n================================")
        print("ERROR")
        print("================================")
        print(e)