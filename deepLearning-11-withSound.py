import jetson.inference
import jetson.utils
import numpy as np 
import time
import os
from gtts import gTTS
import threading

speak=True
item='Lets start discovering objects'
confidence=0
itemOld=''


import cv2
print(cv2.__version__)
width=1280
height=720
flip=2

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
net=jetson.inference.imageNet('googlenet')
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0

def sayItem():
    global speak
    global item
    while True:
        if speak ==True:
            output=gTTS(text=item, lang='en',slow=False)
            output.save('output.mp3')
            os.system('mpg123 output.mp3')
            speak=False
x=threading.Thread(target=sayItem, daemon=True)
x.start()


while True:
    ret, frame = cam.read()
    if ret:
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
        img=jetson.utils.cudaFromNumpy(img)
        if speak==False:
            classID, confidence = net.Classify(img,width,height)
            if confidence>=.5:
                item=net.GetClassDesc(classID)
                if item!=itemOld:
                 speak=True
            if confidence<.5:
                item=''
            itemOld=item
        dt=time.time()-timeMark
        timeMark=time.time()
        fps=1/dt
        fpsFilter=.95*fpsFilter + .05 *fps
        cv2.putText(frame,str(round(fpsFilter,1))+'  fps  '+item+'   '+str(round(confidence,2)),(0,30),font,1,(0,0,255),2)
        cv2.imshow('myCam',frame)
        cv2.moveWindow('myCam',1000,300)
        if cv2.waitKey(1)==ord('q'):
            break

    else:
        print('Error : The frame is empty')
        
cam.release()
cv2.destroyAllWindows()