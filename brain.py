'''# Importing
import openai
from dotenv import load_dotenv
from Speak import speak
import speech_recognition as sr
from googletrans import Translator
import googletrans

def chatGTP():



#Coding

    r = sr.Recognizer()
    mic = sr.Microphone()

    # Take input from microphone
    with mic as source:
        print("Say something!")        
        r.pause_threshold = 1
        audio = r.listen(source,0,6) # Listening Mode.....
        translator = Translator()
        hindi_text = query = r.recognize_google(audio,language="hi")

        result = translator.translate(hindi_text, src='hi', dest='en')

        input_text = result.text
        print("You:" + input_text)
    model = "text-davinci-003"
    openai.api_key = "YOUR_OPENAI_API_KEY"
    prompt=str(input_text)
    comletion = openai.Completion.create(
                engine=model,
                prompt=prompt,   
                max_tokens = 140,
                n=1,
                stop=None,
                temperature = 0.9,)

    response = comletion.choices[0].text
    lines = response.split('.')
    for line in lines[:2]:
        speak(line)
    print(response)
    #Save the chatlog
    file_name = 'chatlogs.txt'
    with open(file_name, 'a+') as f:
        f.write("You: " + input_text + "\n")
        f.write("Gyani: " + response + "\n")

while True:
    try:
        chatGTP()
    except:
        pass'''

#api_keys = ['YOUR_OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY']  # Add more keys as needed
'''
import openai

# List of API keys from different accounts
api_keys = ['YOUR_OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY']  # Add more keys as needed

def generate_text(prompt):
    for api_key in api_keys:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": prompt}]
            )
            return response['choices'][0]['message']['content']
        except openai.error.RateLimitError:
            continue  # Try the next API key if rate limit error occurs
    return "All API keys exceeded their quotas."

# Example usage
prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)'''

from openai import OpenAI
from Speak import speak
import speech_recognition as sr
from deep_translator import GoogleTranslator

def chatGTP():
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Take input from microphone
    with mic as source:
        print("Say something!")        
        r.pause_threshold = 1
        audio = r.listen(source, 0, 6)  # Listening Mode.....
        hindi_text = query = r.recognize_google(audio, language="hi")
        result = GoogleTranslator(source='auto', target='en').translate(hindi_text)

        input_text = result.text
        print("You: " + input_text)
    
    # List of API keys from different accounts
    api_keys = [
        'your-api-key-1-here',
        'your-api-key-2-here'
    ]  # Add more keys as needed

    for api_key in api_keys:
        try:
            model = "gpt-3.5-turbo-1106"  # Change to your desired model
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are Gyani, a helpful voice assistant. Keep answers short and conversational, under 3 sentences."},
                    {"role": "user", "content": input_text}
                ]
            )

            generated_text = response.choices[0].message.content
            lines = generated_text.split('.')
            for line in lines[:2]:
                speak(line)
            print("Gyani: " + generated_text)

            # Save the chatlog
            file_name = 'chatlogs.txt'
            with open(file_name, 'a+') as f:
                f.write("You: " + input_text + "\n")
                f.write("Gyani: " + generated_text + "\n")

            break  # Break out of the loop if successful
        except Exception as e:
            print("Error:", e)
            continue

def get_brain_response(input_text):
    api_keys = [
        'your-api-key-1-here',
        'your-api-key-2-here'
    ]
    for api_key in api_keys:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "system", "content": "You are Gyani, a helpful voice assistant. Keep answers short and conversational, under 3 sentences."},
                    {"role": "user", "content": input_text}
                ]
            )
            generated_text = response.choices[0].message.content
            
            # Save the chatlog
            with open('chatlogs.txt', 'a+', encoding='utf-8') as f:
                f.write("You: " + input_text + "\n")
                f.write("Gyani: " + generated_text + "\n")
                
            return generated_text
        except Exception as e:
            print("Error:", e)
            continue
    return "I am sorry, my brain is not working right now."

