import pyautogui
import pygetwindow as gw
import time

def switch_to_edge():
    edge_windows = gw.getWindowsWithTitle("Edge")
    if edge_windows:
        # 如果有 Edge 窗口存在，则将焦点切换到第一个 Edge 窗口
        edge_windows[0].activate()
        print("已切换到 Microsoft Edge。")
        time.sleep(1)  # 等待 Edge 窗口激活
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('ctrl', 'v')
        print("地址栏已被突出显示并粘贴剪贴板内容。")
    else:
        print("未找到 Microsoft Edge 窗口。")

pyautogui.hotkey('ctrl', 'l')
pyautogui.hotkey('ctrl', 'c')

# 调用函数以切换到 Edge 并执行相应操作
switch_to_edge()
