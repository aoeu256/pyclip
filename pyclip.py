import pyperclip
from googletrans import Translator
import requests

# Set the source and target languages
src_lang = 'en'
tgt_lang = 'fr'

# Access the Windows clipboard
text = pyperclip.paste()

# Check if the clipboard contains text
if text:
    # Translate the text using Google Translate API
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=tgt_lang).text
    
    # Send a message to ChatGPT API and get response
    url = 'https://api.openai.com/v1/engine/chat'
    payload = {
        "prompt": translated_text,
        "temperature": 0.9,
        "max_tokens": 100,
        "stop": ["\n"]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY' # replace with your API key
    }
    response = requests.post(url, json=payload, headers=headers)
    
    # Extract the generated text from the response
    generated_text = response.json()['choices'][0]['text']
    
    # Copy the generated text to the clipboard
    pyperclip.copy(generated_text)
