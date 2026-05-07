import pyttsx3
import requests
import playsound
from Speak import speak
import time
import speech_recognition as sr
    #Initialize the recognizer
def news():
    r = sr.Recognizer()

        #Reading audio from the microphone
    with sr.Microphone() as source:
            speak("What type of news do u want to hear? ")
            speak("buisness, entertainment, general, health, science, sports, technology or as per my wish, Please tell")
            audio = r.listen(source,0,4)
            command = r.recognize_google(audio).lower() 

        #Recognizing the audio
            try:
                print("You said: " + command)
            except Exception as e:
                print("Error: ", e)



    print ("you choosed:"+command)
    if  "as per your wish" == command:   
        speak("please wait sir, fetching the latest news")
        url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=e25cf5da380d4ea58eb67b4f2fd22e55')
        response = requests.get(url).json()
        for i in range(0,5):
            title = (response['articles'][i]['title'])
            speak (title)
    else:
        speak("please wait, fetching the latest "+command+" news")
        try:
            new_url = 'https://newsapi.org/v2/top-headlines?country=in&category='+command+'&apiKey=e25cf5da380d4ea58eb67b4f2fd22e55'
            url_category = (new_url)

            response = requests.get(url_category).json()
            for i in range(0,5):
                title = (response['articles'][i]['title'])

                speak (title)
        except:
                url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=e25cf5da380d4ea58eb67b4f2fd22e55')
                response = requests.get(url).json()
                for i in range(0,5):
                    title = (response['articles'][i]['title'])
                    speak (title)

