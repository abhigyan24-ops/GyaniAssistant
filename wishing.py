import datetime
from Speak import speak
def wishing():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
        speak("I'm Gyani, I'm Ready To Assist You.")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
        speak("I'm Gyani, I'm Ready To Assist You.")
    else:
        speak("Good Evening") 
        speak("I'm Gyani, I'm Ready To Assist You.")
