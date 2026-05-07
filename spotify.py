import random
import pyautogui
import time
import webbrowser
from Speak import speak
def online_player():
    webbrowser.open("https://open.spotify.com/")
    speak("Sure, please leave the system untouched and let me control")
    time.sleep(25)
    backup = "1"
    sample_space = [(389,559), (606,554), (821,558), (1029,576), (1220, 556)]
    x,y = random.choice(sample_space)
    speak("Sorry for the unconvience caused but this proccesior takes about 1 minute")
    pyautogui.click(x,y)
    speak("Playing music as per your intrest from Spotify Daily Mix")
    pyautogui.click(287,471)
    speak("Hope you will Enjoy")
online_player()