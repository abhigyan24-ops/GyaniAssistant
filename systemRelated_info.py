import winshell
import pyautogui
from Speak import speak
import os
import subprocess
import ctypes
import requests
import random
def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Done, Recycle bin is successfully empty")
    except:
        speak("Recycle bin is already empty")
        pass
def shutdown():
            sample_space = [('Have a great day!'),('Take care!'),('It was a pleasure helping you.'),('Stay safe!'),('Best regards.'),('Cheers!'),('Have a fantastic day ahead.'),('May your day be filled with joy and success!')]
            greeting = random.choice(sample_space)
            pyautogui.press('win')
            pyautogui.press('right')
            speak("Ok Shutting down the system")
            pyautogui.press('enter')
            speak("Bye, Thanks for using Gyani Assistant"+ greeting)
def sleep_system():
            pyautogui.press('win')
            speak("Ok Sleeping the system")
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('up')
            pyautogui.press('enter')
            speak("Waiting for your soon arival to help you out")
def stop_shut():
            cont = "shutdown /a"
            os.system(cont)
def lock_win():
        speak("locking window")
        ctypes.windll.user32.LockWorkStation()
def close_video():
    subprocess.call("taskkill /f /IM acroRd32.exe")    
def ip_add():

    ipadd = requests.get('https://api.ipify.org').text
    location_url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
    geo_requests = requests.get(location_url)
    geo_data = geo_requests.json()
    organisation = geo_data['organization_name']
    region = geo_data['region']
    country = geo_data['country']
    print(organisation)
    speak("I am not sure, but I think we are in "  + region + " state of " + country)
def hibern():
    pyautogui.press('win')
    speak("Hibernating the system")
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('enter')
    speak("Waiting for your soon arival to help you out")

#shutdown()
#empty_recycle_bin()
#hibern()
#sleep_system()
#ip_add()
#lock_win()
