import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    """Convert text to speech"""
    print("Asia:", text)
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=8):
    """Listen from microphone and return text"""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print("Error:", e)
        return ""
