# in this lesson we would learn how to use our model , and detect sevral objects in an image
# Moreover , we will extract the object to seperated images

import pixellib
import cv2
import numpy as np
from pixellib.instance import custom_segmentation


segment_image = custom_segmentation()
segment_image.inferConfig(network_backbone="resnet101",num_classes=3,class_names=["BG","Banana","Apple","Tomato"])
segment_image.load_model("c:/models/eval/mask_rcnn_model.032-0.200773.h5") 

segmask, output = segment_image.segmentImage("C:/GitHub/Object-Detection/Pixellib/moreThanOneApple.jpg",show_bboxes=True,extract_segmented_objects=True,save_extracted_objects=True,output_image_name="C:/GitHub/Object-Detection/Pixellib/moreThanOneAppleOut.jpg")

# lets see the object 
#print(segmask)

# We need this section : extracted_objects

res = segmask["extracted_objects"]
#firstImage = res[0]
#firstImageArr = np.uint8(firstImage)

# lets print the shape of the array
#print(firstImageArr.shape)
# this is the width and height of the first extarcted image (the first apple)
#(282, 274, 3)
# lets show it

#cv2.imshow('firstImageArr',firstImageArr)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# lets extract all the apples
# ===========================

title = 0

# loop all the objects

for img in res:
    title = title + 1
    imageArr = np.uint8(img)
    cv2.imshow(str(title), imageArr)

cv2.waitKey(0)
cv2.destroyAllWindows()   


