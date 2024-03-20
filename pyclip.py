import pyperclip
from googletrans import Translator
import firebase_admin
from firebase_admin import credentials, db
import requests, re

cred = credentials.Certificate("micro-autumn-825-firebase-adminsdk-qu39w-046a4a6078.json")
firebase_admin.initialize_app(cred, {
	'storageBucket': 'micro-autumn-825.appspot.com',
	'databaseURL': 'https://558927058897.firebaseio.com'
})
prompt_ref = db.reference('prompt')
prompts = prompt_ref.get()
print('prompts are:', prompts)

src_lang, tgt_lang = 'en', 'zh'

past = pyperclip.paste() # Access the Windows clipboard

tex1 = 'My brother went to a fishing trip'
text = 'Give ７ text completions in mandarin for the words: ' + tex1

varsu = {} # maybe set variables in a firebase store?
# Get functions from other people's promps, and maybe have a function that lists all prompts

if text and text[0] == '=':
	match = re.match(r'=(\w+)\s+(.*)', text)
	if match:
		word, rest = match.groups()	
		prompts[word] = rest
		prompt_ref.update({word:rest})

elif text:	
	# Translate the text using Google Translate API
	#translator = Translator()
	#translated_text = translator.translate(text, src=src_lang, dest=tgt_lang).text
	translated_text = text

	import openai
	
	openai.api_key = os.environ.get('OPENAIKEY')
	model_engine = "gpt-3.5-turbo" 

	response = openai.ChatCompletion.create(
		model='gpt-3.5-turbo',
		messages=[			
			{"role": "user", "content": text},
		])

	message = response.choices[0]['message']
	print("{}: {}".format(message['role'], message['content']))

	# pyperclip.copy(generated_text)
	from tkinter import *
	root = Tk()
	root.overrideredirect(1) # get rid menu bar

	#x, y = root.winfo_pointerxy()
	import win32api, pyautogui

	#hwnd = win32gui.GetForegroundWindow()
	#rect = win32gui.GetWindowRect(hwnd)
	x, y = win32api.GetCursorPos()
	root.geometry(f'+{x-5}+{y-5}')
	listbox = Listbox(root, selectmode=SINGLE)
	#menu= Menu(root, tearoff=0)
	
	#listbox.config(height=1)
	for x, text in enumerate(message['content'].split('\n')):
		listbox.insert(x+1, text)
		#menu.add_command(label=text, command=lambda: print(text))
	listbox.place(x=x, y=y)

	def print_selection(u):
		pyautogui.typewrite(listbox.get(listbox.curselection()))
		root.destroy()

	# bind callback to listbox selection
	def close_window(evt): root.destroy()
	root.bind('&lt;BackSpace&gt;', close_window)
	root.bind('&lt;Escape&gt;', close_window)

	listbox.bind('<<ListboxSelect>>', print_selection)
	listbox.config(height=len(listbox.get(0, "end")))
	listbox.pack()
	root.mainloop()



#import pyautogui
#pyautogui.hotkey('ctrl', 'a')
#print(pyautogui.screenshot().text())

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

	ctypes.windll.user32.keybd_event(win32con.VK_DELETE, 0, 0, 0)
	#ctypes.windll.user32.keybd_event(win
 
 # create wxPython menu with three options a, b, and c


def pyhook():
	import pyHook
	import pythoncom

	def onKeyboardEvent(event):
		if event.Key == "Oem_Comma" and event.MessageName == "key down" and event.Control == True:
			print("Hi")
		return True

	hooks_manager = pyHook.HookManager()
	hooks_manager.KeyDown = onKeyboardEvent
	hooks_manager.HookKeyboard()
	pythoncom.PumpMessages()