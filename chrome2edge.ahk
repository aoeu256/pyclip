
; Define a hotkey (Ctrl + Shift + G) to trigger the script
^+g::
    ; Check if Microsoft Edge process exists
    WinGet, edgeID, ID, ahk_exe msedge.exe
    If (edgeID != "")
    {
        ; Activate Microsoft Edge window
        WinActivate, ahk_pid %edgeID%
        
        ; Send Ctrl + T to open a new tab
        Send, ^t
        Sleep, 100
        
        ; Send the URL to navigate to (Google.com)
        Send, https://www.google.com{Enter}
    }
    else
    {
        ; If Microsoft Edge process does not exist, show a message box
        MsgBox, Microsoft Edge is not running.
    }
return