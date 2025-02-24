import speech_recognition as sr
import pyttsx3

def recognize_speech():
    """Converts spoken audio into text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)

def text_to_speech(text):
    """Converts text into spoken audio output."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
