# In this tutorial we will learn how to blur background in a video file
# This tutorial is based on Pixel lib

# first , Download the model , and copy it to c:/models
#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/xception_pascalvoc.pb

import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg(model_type="pb")
change_bg.load_pascalvoc_model("c:/models/xception_pascalvoc.pb")

img_path = "c:/demo/football.mp4" # this is our video file

# use the model
output = change_bg.blur_video(img_path,extreme=True,frames_per_second=10,output_video_name='c:/demo/footballBlur.mp4')

print('Finish')


