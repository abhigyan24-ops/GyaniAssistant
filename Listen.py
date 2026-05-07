import speech_recognition as sr #pip install speechrecognition
from deep_translator import GoogleTranslator

# 1 - Listen : Hindi or English

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,10) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
        if 'gyani' in query:
            query = query.replace('gyani', '')

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    result = GoogleTranslator(source='auto', target='en').translate(line)
    print("You :"  + result)
    return result

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
