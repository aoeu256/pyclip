import pyautogui
import pygetwindow as gw
import time

import tkinter as tk
import sys
from tkinter import messagebox

from io import StringIO

sys.stderr = StringIO()
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

print = lambda x: messagebox.showinfo('信息', x)
# 弹出警报框
#messagebox.showinfo("警报", "这是一个警报框！")

#root.mainloop()

def switch_to_edge():    
    edge_windows = gw.getWindowsWithTitle("Microsoft\u200b Edge")
    
    if edge_windows:        
        edge_windows[0].activate()        
        time.sleep(1)  # 等待 Edge 窗口激活
        pyautogui.hotkey('ctrl', 't'); time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'l'); time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v'); time.sleep(0.1)
        pyautogui.hotkey('enter')
        
    else:
        import subprocess
        subprocess.run(command, shell=True)
        time.sleep(1)
        switch_to_edge()
        return        

chrome = [g for g in gw.getWindowsWithTitle('Google Chrome') if 'Translate' not in g.title]
chrome[0].activate()
time.sleep(1)
pyautogui.hotkey('ctrl', 'l'); time.sleep(0.1)
pyautogui.hotkey('ctrl', 'c'); time.sleep(0.1)

# 调用函数以切换到 Edge 并执行相应操作
switch_to_edge()

root.mainloop()