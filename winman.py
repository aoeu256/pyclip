import pygetwindow as gw
import pyautogui
import asyncio
import subprocess
from playwright.async_api import async_playwright

# Function to start Edge browser
async def start_edge():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://chat.openai.com")

# Function to start Chrome
async def start_chrome():
    async with async_playwright() as p:
        browser = await p.webkit.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.google.com/")

# Function to start Visual Studio Code
def start_visual_studio():
    subprocess.Popen(["code"])

# 获取所有窗口
窗口列表 = gw.getAllWindows()

def checkApps():
    [边缘窗口,谷歌窗口, 记事本窗口] = [None, None, None]
    for 窗口 in 窗口列表:
        if "Edge" in 窗口.title[-4:]:
            边缘窗口 = 窗口
        elif "Google Chrome" in 窗口.title:
            谷歌窗口 = 窗口
        #elif "IPython" in 窗口.title:
        #    ipython窗口 = 窗口
        elif "Visual Studio Code" in 窗口.title:
            记事本窗口 = 窗口    
    return [边缘窗口, 谷歌窗口, 记事本窗口]

# 根据标题查找窗口对象
[边缘窗口,谷歌窗口, 记事本窗口] = checkApps()
async def main():
    if not 边缘窗口: await start_edge()
    if not 谷歌窗口: await start_chrome()
    if not 记事本窗口:start_visual_studio()

    # 获取屏幕分辨率
    屏幕宽度, 屏幕高度 = pyautogui.size()

    # 计算屏幕宽度的三分之一
    第三宽度 = 屏幕宽度 // 3

    # 定位窗口
    evstr = '谷歌窗口,边缘窗口,ipython窗口, 记事本窗口'
    #print(evstr)
    #print(谷歌窗口,边缘窗口,ipython窗口, 记事本窗口)
    allwindows = [边缘窗口,谷歌窗口, 记事本窗口] = checkApps()

    if all(allwindows):
        # 谷歌放置在左边的水平三分之一
        谷歌窗口.moveTo(0, 0)
        谷歌窗口.resizeTo(第三宽度, 屏幕高度)

        # 边缘放置在中间的三分之一
        #边缘窗口.moveTo(第三宽度, 0)
        边缘窗口.moveTo(0, 0)
        边缘窗口.resizeTo(第三宽度, 屏幕高度)

        # 最后一个三分之一在垂直方向上分割为 ipython shell 和 记事本++
        记事本高度 = 屏幕高度 // 2
        #ipython窗口.moveTo(第三宽度 * 2, 0)
        #ipython窗口.resizeTo(第三宽度, 记事本高度)
        记事本窗口.moveTo(第三宽度, 0)
        记事本窗口.resizeTo(第三宽度*2, 屏幕高度)

        print("窗口平铺完成！")
    else:
        print("错误：无法找到所有所需的窗口。")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
