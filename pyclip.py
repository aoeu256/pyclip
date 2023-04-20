import pyperclip
from googletrans import Translator
import requests

# Set the source and target languages
src_lang = 'en'
tgt_lang = 'zh'

# Access the Windows clipboard
text = pyperclip.paste()
api_key = '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'

if text:
    # Translate the text using Google Translate API
    translator = Translator()
    #translated_text = translator.translate(text, src=src_lang, dest=tgt_lang).text
    translated_text = text
    # Send a message to ChatGPT API and get response
    url = 'https://api.openai.com/v1/completions'
    payload = {
        "prompt": translated_text,
        "model":"text-davinci-003",
        "temperature": 0.9,
        "max_tokens": 100,
        "stop": ["\n"]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}' # replace with your API key        
    }
    response = requests.post(url, json=payload, headers=headers)
    print(translated_text)
    # Extract the generated text from the response
    generated_text = response.json()['choices'][0]['text']
    
    # pyperclip.copy(generated_text)
    from tkinter import *
    root = Tk()
    choices = ['A', 'B', 'C']

    var = StringVar()
    var.set('A')  # set the default option

    popupMenu = OptionMenu(root, var, *choices)
    popupMenu.grid(row=0, column=1)

    # place the popup menu at the current mouse position
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()

#write a python script for windows that when pressing Ctrl+. forces Ctrl+A key press to select text copies it into the clipboard then presses the delete key then shows a selectable dialog menu with three choices a, b, c.

import win32con, win32clipboard, ctypes

def select_all_and_copy():
    # Press Ctrl+A to select all text
    ctypes.windll.user32.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    ctypes.windll.user32.keybd_event(ord('A'), 0, 0, 0)
    ctypes.windll.user32.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

    # Copy the selected text to the clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

    # Press Delete to delete the selected text
    ctypes.windll.user32.keybd_event(win32con.VK_DELETE, 0, 0, 0)
    #ctypes.windll.user32.keybd_event(win
 

 # create wxPython menu with three options a, b, and c
 