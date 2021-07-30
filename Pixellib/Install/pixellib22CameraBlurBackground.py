# In this tuturial we will learn to replace the background in live camera
# This model enables to blur the background , or replace the background with another color , or replace the backgound with gray (Black and white), 
# Or replace the back ground with a background of another video file .

# lets begin.

# first , lets download the model :

# model link :
# https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/xception_pascalvoc.pb

# copy the file to c:/models

import pixellib
from pixellib.tune_bg import alter_bg
import cv2

cam = cv2.VideoCapture(0) # connet to camera

# set the captue resolution
cam.set(3,1920)
cam.set(4,1080)

change_bg = alter_bg(model_type="pb")
change_bg.load_pascalvoc_model('c:/models/xception_pascalvoc.pb')

# remember : Exit the camera using the q

seq , result = change_bg.blur_camera(cam, frames_per_second=10 , extreme = True, show_frames=True , frame_name="frame", detect="person", output_video_name="c:/demo/cameraBlur.mp4")

