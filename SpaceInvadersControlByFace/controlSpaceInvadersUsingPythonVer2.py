import cv2
import numpy as np
import win32gui
import time
import dlib 
from math import hypot
import keyboard
from scipy.spatial import distance as dist
from imutils import face_utils
import imutils

# =============================
# The important libraries are :
# Dlib - the 68 face model 
# ----------------------------
# imutils library 
# pip install --upgrade imutils
# =============================

# This functions is important to compute the euclidean distances between the two sets of
# vertical eye landmarks (x, y)-coordinates
#  
def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])
	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)
	# return the eye aspect ratio
	return ear

# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold

# Many thanks to Adrian Rosebrock for the idea how to compute an eye blink

# you can ajust the threshold according to your room lighting or the camera
# the blinks trigger if the value is below this value
EYE_AR_THRESH = 0.22
EYE_AR_CONSEC_FRAMES = 3


# initialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0

camW = 1280
camH = 720 

# setting the Camera 
cam=cv2.VideoCapture(0)
cam.set(3,camW)
cam.set(4,camH)  

# setting the middle of the cam screen 
# any value out of this boundaries will be right or left of the head 

middleW1 = int(camW/2)-50
middleW2 = int(camW/2)+50
middleW  = int(camW/2)

font = cv2.FONT_HERSHEY_PLAIN

# setting the Dlib model (68 points)
detector = dlib.get_frontal_face_detector()

# you can google this file and downlond it "shape_predictor_68_face_landmarks.dat"
#==========================================================
predictor = dlib.shape_predictor('C:\Python-Code\FacialDetection\shape_predictor_68_face_landmarks.dat')

# grab the indexes of the facial landmarks for the left and  right eye

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

direction = ''
lastpress = ''

# Setting the name of the Atari window
# this is relevant for grabbing and focusing the Atari window
nameWindows = 'Stella 6.5.2: "Space Invaders (1980) (Atari)"'

# Function for finding the pointer of the window 
def get_window_by_caption(caption):
    try:
        hwnd = win32gui.FindWindow(None, caption)
        return hwnd
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1

# grabbing a pointer for the window and focusing 
spaceWindowsHandle = get_window_by_caption(nameWindows)
if spaceWindowsHandle > 0:
    win32gui.SetForegroundWindow( spaceWindowsHandle )

# starting the game as a loop of camera frames
while True :
    ret, frame=cam.read() ## catch the latest frame
    
    # get the windows handle 
    spaceWindowsHandle = get_window_by_caption(nameWindows)
    
    if spaceWindowsHandle > 0 :
        win32gui.SetForegroundWindow( spaceWindowsHandle )
                        
        #keyboard = Controller()  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # grabbing the faces 
        faces = detector(gray,0)

        for face in faces:
            # get the face coordinates

            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            

            # =======================================
            # lets handle with the grabbing a blink :
            #========================================

            # grabbing the face area :
            # since of the blink calculation should be on the face area only and not the whole frame  
            #======================================================================================
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0), 3)
            shape = predictor(gray, face)
            shape = face_utils.shape_to_np(shape)
            
            leftEye  = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR  = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

		    #average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            #compute the convex hull for the left and right eye, then
            #visualize each of the eyes
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            
            # draw eyes
            # ==========
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            #check to see if the eye aspect ratio is below the threshold
            # if yes : we have a blink , and we  increment the blink frame counter 
            if ear < EYE_AR_THRESH:
                COUNTER = COUNTER + 1
                win32gui.SetForegroundWindow( spaceWindowsHandle )
                keyboard.press('space')
                time.sleep(1.2)
                keyboard.release('space')
                print('space/fire')
		    # otherwise, the eye aspect ratio is not below the blink threshold
            else:
                # if the eyes were closed for a sufficient number of
                # then increment the total number of blinks
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    TOTAL += 1
                    # win32gui.SetForegroundWindow( spaceWindowsHandle )
                    # keyboard.press('space')
                    # time.sleep(1.2)
                    # keyboard.release('space')
                    # print('space/fire')
                # reset the eye frame counter
                #COUNTER = 0
		    # draw the total number of blinks on the frame along with
            # the computed eye aspect ratio for the frame
            
            cv2.putText(frame, "Blinks: {}".format(COUNTER), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "EAR blink ratio: {:.2f}".format(ear), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


            # Lets handle with the head movment .
            # we have 3 postions :
            # left , right , stand 
            # It is calculated according to the middleW, middleW1, middleW2 
            # which define the middle of the camera screen 

            # define directions of the face (right , left , stand)
            midFace=int((x1+x2)/2)

            if midFace < middleW1 :
                #print('go right')
                direction='right'
            elif midFace > middleW2 :
                #print('go left')
                direction='left'
            else :
                #print('stand')
                direction='stand'


             # After define the position of the head we activate a keyboard command (left/right arrow)
             # same for the blinks : "Fire" command using space

            if direction=='stand':
                keyboard.release('left')
                keyboard.release('right')
                print('press stand')

            if direction=='right' and direction != lastpress:
                keyboard.release('left')
                keyboard.press('right')
                print('press right')
            
            if direction=='left' and direction != lastpress:
                keyboard.release('right')
                keyboard.press('left')
                print('press left')

            lastpress = direction
            
    # Draw the middle ractangle
    # =========================         
    #cv2.rectangle(frame,(middleW1,0),(middleW2,camH),(0,255,255),3)
    
    cv2.imshow('Originalframe',frame) ## show the flipped frame
        
    if cv2.waitKey(1)==ord('q'):
        break


cam.release() ## releasing the camera
cv2.destroyAllWindows() ## close the windows safe

