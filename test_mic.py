import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the system's default microphone as the audio source
with sr.Microphone() as source:
    print("Speak now...")
    # Adjust for ambient noise levels, if any
    r.adjust_for_ambient_noise(source)

    # Listen for user input
    audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error occurred during speech recognition:", str(e))
