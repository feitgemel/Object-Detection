# In this tutorial we will learn how to extract objects in a video
# this tutorial is based on Pixellib with instance segmentation

# this is our demo video 
# We would like to extract the players and the ball

#first download the model :
#https://github.com/matterport/Mask_RCNN/releases
# we should download the Mask R-CNN 2.0 model !!!!

# copy the file to c:/models

import pixellib
from pixellib.instance import instance_segmentation
import cv2

segmentation_model = instance_segmentation()
segmentation_model.load_model('c:/models/mask_rcnn_coco.h5')

# our video
videoPath = 'c:/demo/football.mp4'

# lets target a specific object in the video
# we will target the ball

target_classes = segmentation_model.select_target_classes(sports_ball=True)
# if , for example we will write person=True it will detect the players.


# use the model
segmask , output = segmentation_model.process_video(videoPath,show_bboxes=True,segment_target_classes=target_classes ,extract_segmented_objects=True,
save_extracted_objects=True, frames_per_second=5, output_video_name="c:/demo/footballOutTargetObject.mp4")
