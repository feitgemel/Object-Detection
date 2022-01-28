import cv2
print(cv2.__version__)

def nothing(x):
    pass

import numpy as np 

cv2.namedWindow('controls')

cv2.createTrackbar('hueLower','controls',0,179,nothing) # 179 is the max value for hue
cv2.createTrackbar('hueUpper','controls',179,179,nothing)
cv2.createTrackbar('satLow','controls',0,255,nothing) # 255 is the max value for sturation
cv2.createTrackbar('satHigh','controls',255,255,nothing)
cv2.createTrackbar('valLow','controls',0,255,nothing) # 255 is the max value for Value
cv2.createTrackbar('valHigh','controls',255,255,nothing)




cam=cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True : 
    ret, frame=cam.read() ## catch the latest frame

    cv2.imshow('cam',frame) ## show the frame
    cv2.moveWindow('cam',0,0)

    # convert the frame to HSV paramters space
    hsvFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # get the variables from the trackbar
    hueLow=cv2.getTrackbarPos('hueLower','controls') # get the low Hue
    hueUp=cv2.getTrackbarPos('hueUpper','controls')# get the high Hue
    

    Ls=cv2.getTrackbarPos('satLow','controls') # get the lowsaturation
    Us=cv2.getTrackbarPos('satHigh','controls') # get the highsaturation

    Lv=cv2.getTrackbarPos('valLow','controls') # get the low Value
    Uv=cv2.getTrackbarPos('valHigh','controls') # get the high Value

    l_b=np.array([hueLow,Ls,Lv]) 
    u_b=np.array([hueUp,Us,Uv])

    

    FGmask=cv2.inRange(hsvFrame,l_b,u_b) 
    cv2.imshow('FGmask',FGmask)
    

    if cv2.waitKey(1)==ord('q'): 
        break
cam.release() 
cv2.destroyAllWindows() 
