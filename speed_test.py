import speedtest
from Speak import speak
def speed_test():

                          print("Checking internet speed....")
                          speak("Please wait, Checking internet speed ")
                          st = speedtest.Speedtest()
                          downloading = st.download()
                          correctDown = int(downloading / 800000)
                          uploading = st.upload()
                          correctUp = int(uploading / 800000)
                          speak("Downloading speed is")
                          speak(str(correctDown) + " mbps")
                          speak("Uploding speed is")
                          speak(str(correctUp) + " mbps")




