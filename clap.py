from Speak import speak
import time
import sounddevice as sd
from Listen import *
import sys
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

    if count>=1:
        print("Clap Detected")
        speak("Hi, I am ready to assist you")
        return True
    else:
        try:
                    print("No Clap Detected")
                    in_for_startup = MicExecution()
                    print("please speak wake up for starting")
                    time.sleep(1)
                    if "wake up" in in_for_startup:
                        speak("Hi, I am ready to assist you")
                        return True                       
                    else:
                        print("")
        except:
                    print("error")
                    in_for_startup = MicExecution()
                    print("please speak wake up for starting")
                    if "wake up" in in_for_startup:
                        speak("Hi, I am ready to assist you")
                        return True
