# In this tutorial we will learn two ways of semantic segmenatation of object detection in a live camera

# first , We will download the two models :

#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.3/deeplabv3_xception65_ade20k.h5
#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5

# lets copy the files to c:/models

import pixellib
from pixellib.semantic import semantic_segmentation
import cv2

cam = cv2.VideoCapture(0)

# set the capturing resolotion to 1920 X 1080
cam.set(3,1920)
cam.set(4,1080)

semgment_video = semantic_segmentation()

#semgment_video.load_ade20k_model("c:/models/deeplabv3_xception65_ade20k.h5")
#seg, result = semgment_video.process_camera_ade20k(cam ,overlay=True, frames_per_second=15 , show_frames=True , frame_name="frame", output_video_name="c:/demo/cameraSemanticSegmentation.mp4" )

# remember to press q to quit the camera !!!


#lets use the second model
semgment_video.load_pascalvoc_model('c:/models/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')
seg , result = semgment_video.process_camera_pascalvoc(cam ,overlay=True, frames_per_second=15 , show_frames=True , frame_name="frame", output_video_name="c:/demo/cameraSemanticSegmentation.mp4")
