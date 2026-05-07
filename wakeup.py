
i
import sounddevice as sd

def clap_detect():
    duration = 10  # seconds
    fs = 44100
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2)
    sd.wait()
    myrecording=myrecording[:,0]
    threshold_value=0.2
    count=0
    for i in range(1,len(myrecording)):
        if myrecording[i]>threshold_value and myrecording[i-1]<=threshold_value:
            count+=1

    if count>=2:
        print("Clap Detected")
        print("Hi, I am ready to assist you")
        
    else:
        print("No Clap Detected")
        import speech_recognition as sr

        r = sr.Recognizer()

        with sr.Microphone() as source:
                print("Say something!")
                r.pause_threshold = 1
                audio = r.listen(source,0,5) # Listening Mode.....

                if "wake up" in r.recognize_google(audio):
                    speak("Hi, I am ready to assist you")
                    
                else:
                    print("error")

while True:
    clap_detect()

