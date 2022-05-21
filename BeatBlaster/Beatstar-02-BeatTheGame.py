from pyautogui import *
import pyautogui
import time
import keyboard

import win32con
import win32api 

Y = 897

xPos1 = 158
xPos2 = 361
xPos3 = 560

# mouse click function by x and y

def mouseClick(x,y):

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# create a loop . press 'q' to exit the loop

while keyboard.is_pressed('q') ==False :

    r1,b1,g1 = pyautogui.pixel(xPos1,Y)
    r2,b2,g2 = pyautogui.pixel(xPos2,Y)
    r3,b3,g3 = pyautogui.pixel(xPos3,Y)

    # check of the color is dark (close to black )
    # we check that the all numbers are under 50
    # 0,0,0 is full black

    if r1<50 and b1<50 and g1<50 :
        mouseClick(xPos1 , Y)

    if r2<50 and b2<50 and g2<50 :
        mouseClick(xPos2 , Y)

    if r3<50 and b3<50 and g3<50 :
        mouseClick(xPos3 , Y)



