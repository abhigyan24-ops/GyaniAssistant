'''import requests
import speech_recognition as sr

# Define your API key
GENIUS_API_KEY = 'jd6fboVa5IyOmIqutpSvxT9athyqwK6QzUTUvDjxpxCXsu-dBmNeSWOBS4ZNzzsT'

# Define the base URL for the Genius API
BASE_URL = 'https://api.genius.com'

# Define a function to transcribe speech from the microphone
def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Please speak:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Define a function to search for English song titles from lyrics
def search_english_songs(lyrics):
    # Construct the search endpoint URL
    search_url = f'{BASE_URL}/search?q={lyrics}'

    # Add your API key to the request headers
    headers = {'Authorization': f'Bearer {GENIUS_API_KEY}'}

    # Make the API request
    response = requests.get(search_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract relevant information (e.g., song titles) from the response
        english_songs = [hit['result']['title'] for hit in data['response']['hits']]

        return english_songs
    else:
        # Print the error message
        print('Error:', response.status_code)

        # Print the response content for further inspection
        print(response.content)

        return []

# Main function
def main():
    # Get input from the microphone
    lyrics = transcribe_speech()

    if lyrics:
        # Search for English song titles using the provided lyrics
        english_songs = search_english_songs(lyrics)[:2]
        if english_songs:
            print('Matching English song titles:', english_songs)
        else:
            print('No matching English song titles found')
    else:
        print('No speech input detected')

if __name__ == "__main__":
    main()
'''
import requests
import speech_recognition as sr
import wave
import pyaudio

# Define your API key
GENIUS_API_KEY = 'jd6fboVa5IyOmIqutpSvxT9athyqwK6QzUTUvDjxpxCXsu-dBmNeSWOBS4ZNzzsT'

# Define the base URL for the Genius API
BASE_URL = 'https://api.genius.com'

# Function to capture audio from the microphone
def record_audio(filename, duration):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording audio...")

    frames = []

    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Audio recording complete.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Define a function to transcribe speech from the microphone and detect song titles

def transcribe_and_detect_song():
    # Record audio from the microphone
    record_audio("audio.wav", duration=10)

    # Use speech recognition to transcribe the recorded audio in chunks
    recognizer = sr.Recognizer()
    audio_file = "audio.wav"

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        print("Transcribing...")
        lyrics = recognizer.recognize_google(audio_data, show_all=True)  # Use show_all=True to get all possible transcriptions
        print("Transcribed lyrics:", lyrics)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return

    # Process the transcribed lyrics and detect song titles
    if lyrics:
        for result in lyrics["alternative"]:
            transcription = result["transcript"]
            # Search for English song titles using the provided lyrics
            search_url = f'{BASE_URL}/search?q={transcription}'
            headers = {'Authorization': f'Bearer {GENIUS_API_KEY}'}
            response = requests.get(search_url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                english_songs = [hit['result']['title'] for hit in data['response']['hits']]
                print('Matching English song titles:', english_songs[:2])
            else:
                print('Error:', response.status_code)
                print(response.content)


# Main function
def main():
    # Transcribe speech and detect song titles
    transcribe_and_detect_song()

if __name__ == "__main__":
    main()
'''import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(sample_rate=44100)

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for high background noise
        audio = recognizer.listen(source, timeout=15)  # Increase timeout for capturing audio

    return audio

def transcribe_audio(audio):
    recognizer = sr.Recognizer()

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service:", e)
        return None

def main():
    # Record audio from the microphone
    audio = record_audio()

    if audio:
        # Transcribe the audio
        audio_text = transcribe_audio(audio)

        if audio_text:
            print("Transcribed audio:", audio_text)
        else:
            print("No speech detected or transcription failed")
    else:
        print("No audio recorded")

if __name__ == "__main__":
    main()'''

