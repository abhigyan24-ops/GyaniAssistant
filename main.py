import requests

# Define your OpenAI API key
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

# Define the URL for the transcriptions API
TRANS_API_URL = 'https://api.openai.com/v1/transcriptions'

# Define the path to your audio file
audio_file_path = 'audio.wav'

# Define the desired output file format for the transcription
output_format = 'txt'

# Read the audio file as binary data
with open(audio_file_path, 'rb') as audio_file:
    audio_data = audio_file.read()

# Set up the request headers with your API key
headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'audio/wav'  # Adjust according to your audio file format
}

# Set up the request data
data = {
    'file': audio_data,
    'output_format': output_format
}

# Send the transcription request
response = requests.post(TRANS_API_URL, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Get the transcription result
    transcription = response.json()
    
    # Print or process the transcription as needed
    print(transcription)
else:
    # Print the error message
    print('Transcription request failed:', response.text)
