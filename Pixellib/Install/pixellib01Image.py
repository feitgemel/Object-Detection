# download the model
#https://github.com/matterport/Mask_RCNN/releases
# https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5

# copy the model to c:\models

import pixellib
from pixellib.instance import instance_segmentation
import cv2

segmentation_model = instance_segmentation()
segmentation_model.load_model('c:/models/mask_rcnn_coco.h5')

# use the model
# We will use the image : friends.jpg 
# we are going to detects the objects and later extarct them

segmask, output = segmentation_model.segmentImage('Object-Detection/PixelLib/friends.jpg', extract_segmented_objects=True, save_extracted_objects = True,  show_bboxes=True , output_image_name = "Object-Detection/PixelLib/friendsOut.jpg")


cv2.imshow('img',output)

cv2.waitKey(0)

cv2.destroyAllWindows()