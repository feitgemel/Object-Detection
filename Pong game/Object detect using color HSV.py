import cv2
import numpy as np

def nothing(x):
    pass

print(cv2.__version__)
cam=cv2.VideoCapture(0)
cv2.namedWindow("TrackBars")

cv2.createTrackbar("lowerH","TrackBars",62,179, nothing)
cv2.createTrackbar("higherH","TrackBars",122,179, nothing)
cv2.createTrackbar("lowerS","TrackBars",105,255, nothing)
cv2.createTrackbar("higherS","TrackBars",255,255, nothing)
cv2.createTrackbar("lowerV","TrackBars",163,255, nothing)
cv2.createTrackbar("higherV","TrackBars",255,255, nothing)


while True : #the camera should never stop capturing (that means while true)
    ret, myFrame=cam.read() ## catch the latest frame

    hsv = cv2.cvtColor(myFrame, cv2.COLOR_BGR2HSV)

    lowerH=cv2.getTrackbarPos("lowerH","TrackBars")
    lowerS=cv2.getTrackbarPos("lowerS","TrackBars")
    lowerV=cv2.getTrackbarPos("lowerV","TrackBars")
    higherH=cv2.getTrackbarPos("higherH","TrackBars")
    higherS=cv2.getTrackbarPos("higherS","TrackBars")
    higherV=cv2.getTrackbarPos("higherV","TrackBars")
    
    lowerYellow = np.array([lowerH, lowerS, lowerV])
    higherYellow = np.array([higherH, higherS, higherV])

    maskImg = cv2.inRange (hsv,lowerYellow,higherYellow)
    
    # ( name of the mask , the mode , how many points )
    contours,_=cv2.findContours(maskImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #when can sort it using sort and get the biggest one
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    cnt=contours[0] # get the first one in the contours array

    #find the area in the image and draw rectangle
    area=cv2.contourArea(cnt)
    (x,y,w,h)=cv2.boundingRect(cnt)
    #cv2.rectangle(myFrame,(x,y),(x+w,y+h),(255,0,0),3) # should draw a rectangle 

    #draw a circle
    radius =int(w/2)
    xCircle = int(x+ w/2)
    yCircle = int(y + h/2)
    myFrame=cv2.circle(myFrame,(xCircle,yCircle),radius,(0,0,255),3)
   
    resultImg=cv2.bitwise_and(myFrame,myFrame,mask=maskImg)

    cv2.imshow('MyCam',myFrame) ## show the frame
    cv2.imshow('mask',maskImg)
    cv2.imshow('result',resultImg)

    cv2.moveWindow('TrackBars',2000,0)
    if cv2.waitKey(1)==ord('q'): ## how to quit ? check every 1 milisecit wait for press a key,  if the q key was pressed     
        break
cam.release() ## releasing the camera
cv2.destroyAllWindows() ## close the windows safe
