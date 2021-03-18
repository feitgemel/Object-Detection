import cv2
import numpy as np
import win32gui
from pynput.keyboard import Key, Controller
import time

print(cv2.__version__)
cam=cv2.VideoCapture(0)

direction = ''
lastpress = ''
nameWindows = 'Stella 6.5.2: "Pac-Man (1982) (Atari)"'


def get_window_by_caption(caption):
    try:
        hwnd = win32gui.FindWindow(None, caption)
        return hwnd
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1

pacManWindowsHandle = get_window_by_caption(nameWindows)
if pacManWindowsHandle > 0:
    win32gui.SetForegroundWindow( pacManWindowsHandle )

while True :
    ret, myFrame=cam.read() ## catch the latest frame

    hsv = cv2.cvtColor(myFrame, cv2.COLOR_BGR2HSV)

    #Handle the green part of the marker
    #===================================

    lowerGreen = np.array([36, 114, 0])
    higherGreen = np.array([104, 255, 255])
    maskImg1 = cv2.inRange (hsv,lowerGreen,higherGreen)

    # ( name of the green mask , the mode , how many points )
    contours,_=cv2.findContours(maskImg1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #when can sort it using sort and get the biggest one
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    if len(contours) > 1:
        cnt=contours[0] # get the first one in the contours array

        #find the area in the first image and draw rectangle
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        #cv2.rectangle(myFrame,(x,y),(x+w,y+h),(255,0,0),3) # should draw a rectangle 

    #Handle the pink part of the marker
    #===================================

    lowerPink = np.array([149, 88, 0])
    higherPink = np.array([179, 255, 255])

    maskImg2 = cv2.inRange (hsv,lowerPink,higherPink)

    # ( name of the first mask , the mode , how many points )
    contours2,_=cv2.findContours(maskImg2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #when can sort it using sort and get the biggest one
    contours2=sorted(contours2,key=lambda x:cv2.contourArea(x),reverse=True)
    if len(contours2) > 1 :
        cnt2=contours2[0] # get the first one in the contours array

        #find the area in the first image and draw rectangle
        area2=cv2.contourArea(cnt2)
        (x2,y2,w2,h2)=cv2.boundingRect(cnt2)
        #cv2.rectangle(myFrame,(x2,y2),(x2+w2,y2+h2),(255,0,0),3) # should draw a rectangle 


    if len(contours)>1 and len(contours2) > 1:
        
        #check the direction before the keyboard command

        if (y - y2) > 50 :
            direction='up'
    
        if (y - y2) < -50 :
            direction='down'
    
        if (x - x2) > 50 :
            direction='right'   

        if (x - x2) < -50 :
            direction='left'   
    
        pacManWindowsHandle = get_window_by_caption(nameWindows)
        #print (pacManWindowsHandle)
        if pacManWindowsHandle > 0 :
        # if we got the handle of the Atari Pacman Windows
            #print('got handle of Pacman Windows')
            
           # win32gui.SetActiveWindow(pacManWindowsHandle)
            win32gui.SetForegroundWindow( pacManWindowsHandle )
                        
            keyboard = Controller()  
        
            if direction == 'left' :#and direction != lastpress :
                keyboard.press(Key.left)
                time.sleep(0.1)
                keyboard.release(Key.left)
                print('left')
            elif direction == 'right' :#and direction != lastpress :
                keyboard.press(Key.right)
                time.sleep(0.1)
                keyboard.release(Key.right)
                print('right')
            elif direction == 'up' :#and direction != lastpress :
                keyboard.press(Key.up)
                time.sleep(0.1)
                keyboard.release(Key.up)
                print('up')
            elif direction == 'down' :#and direction != lastpress :
                keyboard.press(Key.down)
                time.sleep(0.1)
                keyboard.release(Key.down)
                print('down')
            
            lastpress = direction
            
    flipFrame=cv2.flip(myFrame,1)
    cv2.imshow('MyCam',flipFrame) ## show the frame
    #cv2.moveWindow('MyCam',0,0)


    if cv2.waitKey(1)==ord('q'): 
        break



cam.release() ## releasing the camera
cv2.destroyAllWindows() ## close the windows safe

