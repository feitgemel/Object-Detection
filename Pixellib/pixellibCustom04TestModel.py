import pixellib
import cv2
from pixellib.instance import custom_segmentation


segment_image = custom_segmentation()
segment_image.inferConfig(num_classes=3,class_names=["BG","Banana","Apple","Tomato"] )
# BG - refers to the background image , and basicly it is like the default
# it is the first class and must be declared along with the names of the classes

# num_classes = the number of detected classes - we have in the demo 3 classes 
#Class names - list of the classes

# this is our winning model from our precious coding
segment_image.load_model("c:/models/eval/mask_rcnn_model.051-0.252276.h5") 

#lets test the first image 

segment_image.segmentImage("C:/Python-Code/ObjectDetection/PixelLib/AppleTestImage.jpg", show_bboxes=True,output_image_name="C:/Python-Code/ObjectDetection/PixelLib/AppleTestImageOut.jpg")

outImage1 = cv2.imread("C:/Python-Code/ObjectDetection/PixelLib/AppleTestImageOut.jpg")
cv2.imshow('outImage1',outImage1)


segment_image.segmentImage("C:/Python-Code/ObjectDetection/PixelLib/bananaTestImage.jpg", show_bboxes=True,output_image_name="C:/Python-Code/ObjectDetection/PixelLib/bananaTestImageOut.jpg")

outImage2 = cv2.imread("C:/Python-Code/ObjectDetection/PixelLib/bananaTestImageOut.jpg")
cv2.imshow('outImage2',outImage2)




cv2.waitKey(0)




