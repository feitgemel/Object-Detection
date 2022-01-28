
# conda create -n tennis python=3.6
# pip install opencv-python
# pip install pywin32
# pip install pynput



import cv2
import numpy as np
import win32gui 
import win32con

from pynput.keyboard import Key, Controller
import time
keyWaitTime = 0.02

print(cv2.__version__)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

centerX = int(1280/2)

centerOfXPosition= centerX
listOfAreas=[]
 

directionRightLeft = ''
directionUpDown = ''

nameWindows = 'Stella 6.5.2: "Tennis (1981) (Activision) (PAL)"'


def get_window_by_caption(caption):
    try:
        hwnd = win32gui.FindWindow(None, caption)
        return hwnd
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1

tennisManWindowsHandle = get_window_by_caption(nameWindows)
if tennisManWindowsHandle > 0:
    # SetWindowPos(hWnd, InsertAfter, X, Y, new width, new height, Flags)
    print(tennisManWindowsHandle)

    win32gui.SetWindowPos(tennisManWindowsHandle,win32con.HWND_TOPMOST,100,100,200,200,0)
    win32gui.SetForegroundWindow( tennisManWindowsHandle )
    
    
while True :
    ret, myFrame=cam.read() ## catch the latest frame

    hsv = cv2.cvtColor(myFrame, cv2.COLOR_BGR2HSV)

    #Handle the Blue racket
    #===================================

    lowerGreen = np.array([79, 203, 102])
    higherGreen = np.array([112, 255, 255])
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
        cv2.rectangle(myFrame,(x,y),(x+w,y+h),(255,0,0),3) # should draw a rectangle 
        
        # Calulate the Avarage of area
        areaRecPerFrame = int(w * h /2)
        listOfAreas.append(areaRecPerFrame)
        last100areas = listOfAreas[-100:]
        last100areasNumpy = np.array(last100areas)
        avarageArea = np.average(last100areasNumpy)

        dif = int(areaRecPerFrame-avarageArea )

        #print('avarageArea: ',avarageArea, ' Last Area : ',areaRecPerFrame, ' Dif : ', dif)
        
        
        
        centerOfXPosition=int(w/2) + x
        if centerOfXPosition < 30 :
            centerOfXPosition = 30

        if centerOfXPosition > 1250:
            centerOfXPosition = 1250

      

    if len(contours)>1 :
        
          
        if  centerOfXPosition > (centerX+100):
            directionRightLeft='left'   

        if centerOfXPosition < (centerX-100) :
            directionRightLeft='right'   
    
        if centerOfXPosition > centerX-100 and centerOfXPosition < centerX+200:
            directionRightLeft='hold'   

        if dif > 20000 :
            directionUpDown='fire'

        if dif > 1000 and dif < 20000:
            directionUpDown='up'

        if dif <0 :
            directionUpDown='down'


        #print('Direction: ',direction,' centerOfXPosition: ',centerOfXPosition,' CenterX : ', centerX )

        tennisManWindowsHandle = get_window_by_caption(nameWindows)
 
        # if we got the handle of the Atari Tennis Windows
       
        if tennisManWindowsHandle > 0 :
        
        
          
           
            win32gui.SetForegroundWindow( tennisManWindowsHandle )
                        
            keyboard = Controller()  
        
            if directionRightLeft == 'left' :
                 keyboard.press(Key.left)
                 #time.sleep(keyWaitTime)
                 #keyboard.release(Key.left)
                 print('left')
            elif directionRightLeft == 'right' :
                 keyboard.press(Key.right)
                 #time.sleep(keyWaitTime)
                 #keyboard.release(Key.right)
                 print('right')

            elif directionRightLeft == 'hold' :
                 keyboard.release(Key.right)
                 keyboard.release(Key.left)
                 keyboard.release(Key.up)
                 keyboard.release(Key.down)
                 keyboard.release(Key.space)


            if directionUpDown == 'fire' :
                keyboard.press(Key.space)
                #time.sleep(keyWaitTime)
                #keyboard.release(Key.space)
                print('fire')

            elif directionUpDown == 'up' :
                keyboard.press(Key.up)
                #time.sleep(keyWaitTime)
                #keyboard.release(Key.up)
                print('up')

            elif directionUpDown == 'down' :
                keyboard.press(Key.down)
                #time.sleep(keyWaitTime)
                #keyboard.release(Key.down)
                print('down')

                
             
    flipFrame=cv2.flip(myFrame,1)
    flipMask= cv2.flip(maskImg1,1)
     
    cv2.imshow('MyCam',flipFrame) ## show the frame
    cv2.imshow('mask image',flipMask) ## show the frame
    
    #cv2.moveWindow('MyCam',0,0)


    if cv2.waitKey(1)==ord('q'): 
        break



cam.release() ## releasing the camera
cv2.destroyAllWindows() ## close the windows safe

