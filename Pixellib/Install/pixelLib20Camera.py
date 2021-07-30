# detcting object on live camera using PixelLib , OpenCV and Python

# first , install these libraries :
#pip install tensorflow==2.4.1 tensorflow-gpu==2.4.1 pixellib opencv-python 

#download the model :
# https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5

# copy the model to c:/models

import pixellib
from pixellib.instance import instance_segmentation
import cv2

segmentation_model = instance_segmentation()
segmentation_model.load_model('c:/models/mask_rcnn_coco.h5')


# lets target a specific object
target_classes = segmentation_model.select_target_classes(person=True)


# open the camera
cam = cv2.VideoCapture(0) # 0 is the first connected camera

#use the model

seg,result = segmentation_model.process_camera(cam, segment_target_classes=target_classes, show_bboxes=True, show_frames=True, extract_segmented_objects=True, save_extracted_objects=True,frame_name='frame',frames_per_second=25,output_video_name="c:/demo/cameraObjectDetec.mp4")

# important - Remember
# in order to quit the camera and the running program you should press q !!!!!

#lets run it




