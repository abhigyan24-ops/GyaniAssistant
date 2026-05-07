import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from Speak import speak



search = "temerature in chhattisgarh bhilai"
url = "https://www.google.com/search?q=" + search
r = requests.get(url)
data = BeautifulSoup(r.text, "html.parser")
temp = data.find("div", class_="BNeawe").text
speak("The current temperature in bhilaai is " + temp)