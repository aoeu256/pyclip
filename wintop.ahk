; 将窗口置顶
!z::
WinGet, ExStyle, ExStyle, A
if (ExStyle & 0x8) ; Check if WS_EX_TOPMOST flag is set
{
    WinSet, AlwaysOnTop, Off, A ; Turn off always on top
}
else
{
    WinSet, AlwaysOnTop, On, A ; Turn on always on top
}
return

; 设置窗口透明度为50%
!m::
WinGet, Transparent, Transparent, A

if (Transparent > 151) ; Check if window is fully opaque
{
    WinSet, Transparent, 150, A ; Set transparency to 150 (50% transparent)
}
else
{
    WinSet, Transparent, 255, A ; Make the window opaque
}
return

; 定义热键组合（CTRL + WINDOWS + 左键单击）
^#LButton::
	StartX = 0
	StartY = 0
    ; 保存当前鼠标坐标
    MouseGetPos, X, Y

	; 存储鼠标的绝对坐标
    ; 保存当前活动窗口的ID和标题
    WinGetActiveTitle, ActiveTitle
    WinGet, ActiveWindow, ID, A
	WinGetPos, WinX, WinY, WinWidth, WinHeight, ahk_id %A%
	
	StartX := X + WinX
	StartY := Y + WinY


    ; 调试消息框显示 StartX、StartY、ActiveWindow 和 ActiveTitle
    MsgBox, StartX: %StartX% StartY: %StartY%`nActiveWindow: %ActiveWindow%ActiveTitle: %ActiveTitle%`nX: %X%

    ; 查找当前活动窗口之下的窗口
    BelowWindow := ""
    WinGet, WindowList, List
    Loop, % WindowList
    {
        hWnd := WindowList%A_Index%
        if (hWnd != ActiveWindow)
        {
            ; 检查鼠标坐标是否在窗口内
            WinGetPos, WinX, WinY, WinWidth, WinHeight, ahk_id %hWnd%
			WinGetTitle, Title, ahk_id %hWnd%
			;MsgBox, % "Window " A_Index ": " Title
			;MsgBox, StartX: %StartX%`nWinX: %WinX%`nWinX + WinWidth: %WinX% + %WinWidth%`nStartY: %StartY%`nWinY: %WinY%`nWinY + WinHeight: %WinY% + %WinHeight%			
            if (StartX >= WinX && StartX <= WinX + WinWidth && StartY >= WinY && StartY <= WinY + WinHeight)
            {
                BelowWindow := hWnd
                ; 调试消息框显示当前循环索引窗口的标题
                WinGetTitle, Title, ahk_id %BelowWindow%
                MsgBox, % "Window " A_Index ": " Title
                break
            }
        }
    }

    ; 如果找到合适的窗口，则激活该窗口
    if (BelowWindow)
        WinActivate, ahk_id %BelowWindow%

    ; 单击保存的鼠标坐标
    Click, %StartX%, %StartY%

    ; 恢复焦点到原始活动窗口
    WinActivate, %ActiveTitle%
return
