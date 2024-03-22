#Persistent
SetTitleMatchMode, 2 ; 匹配包含指定文本的窗口标题
WinActivate, Anki ; 激活标题包含"Anki"的窗口

Loop, 10 { ; Loop from 1 to 10
    LoopIndexMinusOne := A_Index - 1 ; Subtract 1 from loop index
    Hotkey, ^!%LoopIndexMinusOne%, HotkeyFunction ; Define hotkey with Ctrl+Alt+loop index
}

Loop, 12 { ; Loop through F1 to F12 keys
	#Persistent
    Hotkey, ^!F%A_Index%, HotkeyFunction ; Define hotkey for F1 to F12 keys
}

Loop, 26 { ; Loop through letters A to Z
	c_index := Chr(A_Index + 64)	
     Hotkey, ^!%c_index%, HotkeyFunction
}

Hotkey, ^!Space, HotkeyFunction ; CTRL+ALT+Space
Hotkey, ^!Enter, HotkeyFunction ; CTRL+ALT+Enter
  
HotkeyFunction:	
	;MsgBox, You pressed Ctrl+Alt+%A_ThisHotkey% ; Replace this with your desired action
    ; 激活标题为 "anki" 的窗口
    key := StrReplace(A_ThisHotkey, "^!")
	HotKey, %A_ThisHotkey%, HotkeyFunction
	
	SetTitleMatchMode, 2
	; 等待*Anki*窗口激活，超时设置为5秒	
	WinActivate, ahk_exe anki.exe
	Send, {%key%}
	/*Run, %A_ScriptDir%\flipkey.py %A_ThisHotkey%*/
	/*MsgBox, You pressed Ctrl+Alt+%A_ThisHotkey% ; Replace this with your desired action*/
