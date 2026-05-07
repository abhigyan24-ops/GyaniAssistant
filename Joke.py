from Speak import speak
import pyjokes

def Jokee():
    
    joke = pyjokes.get_joke()
    speak(joke)
