import pyautogui
import sys
import time
import os
import pygetwindow as gw

def alert(text, title="标题"):
	import tkinter as tk
	from tkinter import messagebox
	root = tk.Tk()
	root.withdraw()
	messagebox.showinfo(title, text)


def save_focus():
	# Save the current mouse position
	current_x, current_y = pyautogui.position()
	return current_x, current_y

def switch_to_anki():
	# Find the Anki window and bring it to the foreground
	anki_window = gw.getWindowsWithTitle("Anki")
	if anki_window:
		anki_window[0].activate()
	else:
		alert("Anki窗口未找到！")

def press_button(argument):
	# 如果参数是数字或字母，请使用 pyautogui.hotkey(入数);否则，按参数
	if argument.isdigit() or argument.isalpha():
		pyautogui.hotkey(argument)
	else:
		pyautogui.press(argument.lower())
	#alert('argument is '+argument)

def switch_to_previous_focus(x, y):
	# 切换回原来的应用程序并将其置于焦点
	pyautogui.moveTo(x, y)
	pyautogui.click(x=x, y=y)

# 执行自动化的主要函数
def main(argument):
	# 保存当前鼠标位置
	saved_x, saved_y = save_focus()
	switch_to_anki()
	time.sleep(0.2)
	press_button(argument)
	switch_to_previous_focus(saved_x, saved_y)

if __name__ == "__main__":
	#main('space')
	if len(sys.argv) < 2:
		alert("请提供参数：1、2、3、4或enter")

	main(sys.argv[-1])    
