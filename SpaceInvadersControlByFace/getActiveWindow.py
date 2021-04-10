import win32gui
from pynput.keyboard import Key, Controller

from win32gui import GetWindowText, GetForegroundWindow

def get_window_by_caption(caption):
    try:
        hwnd = win32gui.FindWindow(None, caption)
        return hwnd
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1

w = get_window_by_caption('Stella 6.5.2: "Space Invaders (1980) (Atari)"')
print (w)

if w > 0:
    win32gui.SetForegroundWindow( w )
    
