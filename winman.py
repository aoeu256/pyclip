import pygetwindow as gw
import pyautogui

# 获取所有窗口
窗口列表 = gw.getAllWindows()

# 根据标题查找窗口对象
边缘窗口 = None
谷歌窗口 = None
ipython窗口 = None
记事本窗口 = None
for 窗口 in 窗口列表:
    if "Edge" in 窗口.title[-4:]:
        边缘窗口 = 窗口
    elif "Google Chrome" in 窗口.title:
        谷歌窗口 = 窗口
    #elif "IPython" in 窗口.title:
    #    ipython窗口 = 窗口
    elif "Visual Studio Code" in 窗口.title:
        记事本窗口 = 窗口

# 获取屏幕分辨率
屏幕宽度, 屏幕高度 = pyautogui.size()

# 计算屏幕宽度的三分之一
第三宽度 = 屏幕宽度 // 3

# 定位窗口
evstr = '谷歌窗口,边缘窗口,ipython窗口, 记事本窗口'
#print(evstr)
#print(谷歌窗口,边缘窗口,ipython窗口, 记事本窗口)
allwindows = [边缘窗口, 谷歌窗口, 记事本窗口]

if 谷歌窗口 and 边缘窗口 and ipython窗口 and 记事本窗口:
    # 谷歌放置在左边的水平三分之一
    谷歌窗口.moveTo(0, 0)
    谷歌窗口.resizeTo(第三宽度, 屏幕高度)

    # 边缘放置在中间的三分之一
    边缘窗口.moveTo(第三宽度, 0)
    边缘窗口.resizeTo(第三宽度, 屏幕高度)

    # 最后一个三分之一在垂直方向上分割为 ipython shell 和 记事本++
    记事本高度 = 屏幕高度 // 2
    #ipython窗口.moveTo(第三宽度 * 2, 0)
    #ipython窗口.resizeTo(第三宽度, 记事本高度)
    记事本窗口.moveTo(第三宽度 * 2, 屏幕高度)
    记事本窗口.resizeTo(第三宽度, 屏幕高度)

    print("窗口平铺完成！")
else:
    print("错误：无法找到所有所需的窗口。")
