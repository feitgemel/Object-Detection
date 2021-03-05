import numpy as np
import cv2
import time
print(cv2.__version__)


cam=cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fnt=cv2.FONT_HERSHEY_DUPLEX

print(width)
print(height)


MiddleLineThick=5
middleLineX1=int((width/2)-20)
middleLineY1=100

middleLineX2=int((width/2)+20)
middleLineY2=height-10

textX1=int((width/2)-80)
textY1=50

circleRaduisPlayers=60

#Player 2
redCircleX=1200
redCircleY=400
redCircleStep=10


ScorePlayer1=0
ScorePlayer2=0

xBall = int (width/2)
yBall = int (height/2)

xCirclePre=0
yCirclePre=0

radiusBall = 40
changeX=-20
changeY=-20

while True : 
    ret, myFrame=cam.read() ## catch the latest frame
    flipFrame = cv2.flip(myFrame, 1)
    
    xBall=xBall+changeX
    yBall=yBall+changeY
    
    # borders
    if (yBall+radiusBall>=height):
        yBall=height-radiusBall-1
        changeY=changeY*-1

    if (yBall-radiusBall<=0):
        yBall=0+radiusBall+1
        changeY=changeY*-1

    if (xBall+radiusBall>=width):
        ScorePlayer1=ScorePlayer1+1
        xBall = int (width/2)
        yBall = int (height/2)
        time.sleep(1)

    if (xBall-radiusBall<=0):
        ScorePlayer2=ScorePlayer2+1
        xBall = int (width/2)
        yBall = int (height/2)
        time.sleep(1)

    

    #============================================================================
    # Finding player 1
    #============================================================================
    hsv = cv2.cvtColor(flipFrame, cv2.COLOR_BGR2HSV)
    # borders for Blue color of the ball 
    lowerHSV = np.array([62, 105, 163])
    higherHSV = np.array([122, 255, 255])

    maskImg = cv2.inRange (hsv,lowerHSV,higherHSV)
    
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
    
    # show the blue ball
    if xCircle+radius > middleLineX1 :
        flipFrame=cv2.circle(flipFrame,(xCircle,yCircle),radius,(0,0,255),-1)
    else :
        flipFrame=cv2.circle(flipFrame,(xCircle,yCircle),radius,(0,255,255),3)
    


    # Ball and Player 1
    if (xBall>= xCircle-radius) and xBall<=xCircle+radius and (yBall>= yCircle-radius) and (yBall<= yCircle+radius) :
        
        if xCircle>xCirclePre :
            changeX=abs(changeX)
        if xCircle<xCirclePre :
            changeX=-abs(changeX)

        if yCircle>yCirclePre :
           changeY=abs(changeY) 
        if yCircle<yCirclePre :
           changeY=-abs(changeY) 

        xCirclePre=xCircle
        yCirclePre=yCircle
        
    # Ball and Player 2
    if (xBall>= redCircleX-circleRaduisPlayers) and xBall<=redCircleX+circleRaduisPlayers and (yBall>= redCircleY-circleRaduisPlayers) and (yBall<= redCircleY+circleRaduisPlayers) :
        print("TouchRed")
        changeX=changeX*-1
     
    resultImg=cv2.bitwise_and(flipFrame,flipFrame,mask=maskImg)

    # ====================================================================
    #                           the game 
    # ====================================================================
    scoreText='Score '+str(ScorePlayer1)+ '-' + str(ScorePlayer2) 
    
    flipFrame=cv2.rectangle(flipFrame,(middleLineX1,middleLineY1),(middleLineX2,middleLineY2),(255,0,0),-1)
    flipFrame=cv2.putText(flipFrame,scoreText,(textX1,textY1),fnt,1,(255,0,0),2) 

    # Red circle - Player 2
    flipFrame=cv2.circle(flipFrame,(redCircleX,redCircleY),circleRaduisPlayers,(0,0,255),-1)
    
    # red circle movement
    redCircleY = redCircleY + redCircleStep

    if redCircleY>=height :
        redCircleStep=redCircleStep*-1
        redCircleY=redCircleY+redCircleStep
    elif redCircleY<=0 :
        redCircleStep=redCircleStep*-1
        redCircleY=redCircleY+redCircleStep
    elif redCircleY>yBall :
        redCircleStep=-abs(redCircleStep)
    elif redCircleY<yBall :
        redCircleStep=abs(redCircleStep)



    #Ball Movemnet 
    flipFrame=cv2.circle(flipFrame,(xBall,yBall),radiusBall,(0,255,0),-1)


    # show the frame
    cv2.imshow('Pong',flipFrame) ## show the frame
    cv2.imshow('mask',maskImg)
    cv2.imshow('result',resultImg)

    if cv2.waitKey(1)==ord('q'):
        break
    

cam.release() ## releasing the camera
cv2.destroyAllWindows() ## close the windows safe


