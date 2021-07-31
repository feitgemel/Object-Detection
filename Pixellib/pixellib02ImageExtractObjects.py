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
# We will use the image : animals.jpg 
# we are going to detects the objects and extarct them

segmask, output = segmentation_model.segmentImage('Object-Detection/PixelLib/animals.jpg', extract_segmented_objects=True, save_extracted_objects = True,  show_bboxes=True , output_image_name = "Object-Detection/PixelLib/animalsOut.jpg")


#print (segmask)

# this contains all the objects 
# lets see first the image 

res = segmask["extracted_objects"]

#a = res[0]

# this is the outcome of the object extarcation
#a is a the image
# The shape should be :  XXX , YYY , 3
#print (a.shape)

# lets display all the objects :

title = 0

for a in res :
    title = title + 1 # this is only the title for each object image
    # show each object image 
    cv2.imshow(str(title), a)


# show the final image 
cv2.imshow('img',output)

cv2.waitKey(0)

cv2.destroyAllWindows()