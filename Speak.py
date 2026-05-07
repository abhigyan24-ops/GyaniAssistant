import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 3:
    engine.setProperty('voice', voices[3].id)
elif len(voices) > 0:
    engine.setProperty('voice', voices[0].id)
newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)

def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()