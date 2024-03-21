def check(pname='msedge'):
	processes = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE, universal_newlines=True)
	return any(pname in process for process in processes.stdout)

def type_text(text):
	pyautogui.write(text)
	
def open_msedge():
	subprocess.Popen(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", 'https://chat.openai.com/c/70df0632-bbe3-4fa1-a314-eb01f3304f94'])
	time.sleep(2)  # Wait for Edge to open

def open_keep():
	subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "https://keep.google.com/"])
	time.sleep(2)  # Wait for Google Keep to open
	
def open_dongtai():
	subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "https://www.bilibili.com/"])
	time.sleep(2)  # Wait for Google Keep to open
	
def open_google():	
	subprocess.Popen(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", 'https://www.google.com'])
	time.sleep(2)  # Wait for Edge to open

def popen(arg):	
	subprocess.Popen(arg)
	time.sleep(1.5)  # Wait for open
	
def check(arg):
	argT = {'msedege': 'Microsoft\u200b Edge"', 'chrome': 'Google Chrome'}
	edge_windows = [g for g in gw.getWindowsWithTitle(argT[arg]) if 'Translate' not in g.title]
	if edge_windows:
		edge_windows[0].activate()
	time.sleep(0.25)

def main():    
	if keyboard.is_pressed('ctrl'):
		pname, path = 'msedge, ["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", 'https://chat.openai.com/']
	elif keyboard.is_pressed('alt'):
		pname, path = 'chrome', ["C:\Program Files\Google\Chrome\Application\chrome.exe", "https://keep.google.com/"] 
	else:
		pname, path = 'chrome', ["C:\Program Files\Google\Chrome\Application\chrome.exe", "https://www.bilibili.com/"] 
	if check(pname):
		switch(pname)
	else:
		popen(path)
	
	if 'chat' in path[1]:
		pass


###

import tkinter as tk

def on_key_press(event):
	if event.keysym == "Return":
		# 按下 Enter 键时保存输入的文本并关闭窗口
		global text
		text = entry.get()
		root.destroy()
	elif event.keysym == "Escape":
		# 按下 Escape 键时关闭窗口
		root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("输入框")

# 创建输入框
entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

# 确保主窗口具有焦点
root.focus_force()

# 设置输入焦点
entry.focus_set()

# 绑定按键事件
entry.bind("<KeyPress>", on_key_press)

# 运行主循环
root.mainloop()

# 打印保存的文本
print("您输入的文本是：", text)
