import cv2
import numpy as np

def nothing(x):
    pass

print(cv2.__version__)
cam=cv2.VideoCapture(0)
cv2.namedWindow("TrackBars")
cv2.namedWindow("TrackBars2")

cv2.createTrackbar("lowerH1","TrackBars",0,179, nothing)
cv2.createTrackbar("higherH1","TrackBars",179,179, nothing)
cv2.createTrackbar("lowerS1","TrackBars",0,255, nothing)
cv2.createTrackbar("higherS1","TrackBars",255,255, nothing)
cv2.createTrackbar("lowerV1","TrackBars",0,255, nothing)
cv2.createTrackbar("higherV1","TrackBars",255,255, nothing)

cv2.createTrackbar("lowerH2","TrackBars2",0,179, nothing)
cv2.createTrackbar("higherH2","TrackBars2",179,179, nothing)
cv2.createTrackbar("lowerS2","TrackBars2",0,255, nothing)
cv2.createTrackbar("higherS2","TrackBars2",255,255, nothing)
cv2.createTrackbar("lowerV2","TrackBars2",0,255, nothing)
cv2.createTrackbar("higherV2","TrackBars2",255,255, nothing)


while True :
    ret, myFrame=cam.read() ## catch the latest frame

    hsv = cv2.cvtColor(myFrame, cv2.COLOR_BGR2HSV)

    #================================================================================
    # First masking
    #================================================================================
    lowerH1=cv2.getTrackbarPos("lowerH1","TrackBars")
    lowerS1=cv2.getTrackbarPos("lowerS1","TrackBars")
    lowerV1=cv2.getTrackbarPos("lowerV1","TrackBars")
    higherH1=cv2.getTrackbarPos("higherH1","TrackBars")
    higherS1=cv2.getTrackbarPos("higherS1","TrackBars")
    higherV1=cv2.getTrackbarPos("higherV1","TrackBars")
    
    lower1 = np.array([lowerH1, lowerS1, lowerV1])
    higher1 = np.array([higherH1, higherS1, higherV1])

    maskImg1 = cv2.inRange (hsv,lower1,higher1)
    
    # ( name of the first mask , the mode , how many points )
    contours,_=cv2.findContours(maskImg1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #when can sort it using sort and get the biggest one
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    cnt=contours[0] # get the first one in the contours array

    
    #find the area in the first image and draw rectangle
    area=cv2.contourArea(cnt)
    (x,y,w,h)=cv2.boundingRect(cnt)
    cv2.rectangle(myFrame,(x,y),(x+w,y+h),(255,0,0),3) # should draw a rectangle 



    #================================================================================
    # Second masking
    #================================================================================
    lowerH2=cv2.getTrackbarPos("lowerH2","TrackBars2")
    lowerS2=cv2.getTrackbarPos("lowerS2","TrackBars2")
    lowerV2=cv2.getTrackbarPos("lowerV2","TrackBars2")
    higherH2=cv2.getTrackbarPos("higherH2","TrackBars2")
    higherS2=cv2.getTrackbarPos("higherS2","TrackBars2")
    higherV2=cv2.getTrackbarPos("higherV2","TrackBars2")
       

    lower2 = np.array([lowerH2, lowerS2, lowerV2])
    higher2 = np.array([higherH2, higherS2, higherV2])

    maskImg2 = cv2.inRange (hsv,lower2,higher2)

    # ( name of the first mask , the mode , how many points )
    contours2,_=cv2.findContours(maskImg2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #when can sort it using sort and get the biggest one
    contours2=sorted(contours2,key=lambda x:cv2.contourArea(x),reverse=True)
    cnt2=contours2[0] # get the first one in the contours array

    #find the area in the first image and draw rectangle
    area2=cv2.contourArea(cnt2)
    (x2,y2,w2,h2)=cv2.boundingRect(cnt2)
    cv2.rectangle(myFrame,(x2,y2),(x2+w2,y2+h2),(255,0,0),3) # should draw a rectangle 

    

    #================================================================================
    # Handle both masking
    #================================================================================



    resultImg1=cv2.bitwise_and(myFrame,myFrame,mask=maskImg1)
    resultImg2=cv2.bitwise_and(myFrame,myFrame,mask=maskImg2)

    cv2.imshow('MyCam',myFrame) ## show the frame
    cv2.moveWindow('MyCam',0,0)

    
    cv2.imshow('mask',maskImg1)
    cv2.moveWindow('mask',800,0)

    cv2.imshow('mask2',maskImg2)
    cv2.moveWindow('mask2',800,600)
   
    cv2.imshow('result1',resultImg1)
    cv2.moveWindow('result1',1500,0)

    cv2.imshow('result2',resultImg2)
    cv2.moveWindow('result2',1500,600)


    cv2.moveWindow('TrackBars',2200,0)
    cv2.moveWindow('TrackBars2',2200,400)

    if cv2.waitKey(1)==ord('q'): ## how to quit ? check every 1 milisecit wait for press a key,  if the q key was pressed     
        break
cam.release() ## releasing the camera
cv2.destroyAllWindows() ## close the windows safe
