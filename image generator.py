import openai
import webbrowser

openai.api_key = [


        'YOUR_OPENAI_API_KEY',
        'YOUR_OPENAI_API_KEY',
        'YOUR_OPENAI_API_KEY',
        'YOUR_OPENAI_API_KEY'
]  # Add more keys as needed

for openai.api_key in openai.api_key:
        try:
            response = openai.Image.create(
            model="dall-e-2",
            prompt="sunrise",
            size="1024x1024",
            quality="standard",
            n=1,
            )

            image_url = response.data[0].url

            webbrowser.open(image_url)
        except Exception as e:
            print("Error:", e)
            break
