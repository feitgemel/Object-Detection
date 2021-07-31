#In this tutorial we will learn how to detect object in an image as a semantic segmentation ( 150 classes )

# download the model and copy it to c:/models
#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.3/deeplabv3_xception65_ade20k.h5

import cv2
import pixellib
from pixellib.semantic import semantic_segmentation

pathForImage = 'Object-Detection/PixelLib/girl-dog.jpg'

img = cv2.imread(pathForImage)

 
# run the model
segmant_image = semantic_segmentation()
segmant_image.load_ade20k_model('c:/models/deeplabv3_xception65_ade20k.h5')

segmask, output = segmant_image.segmentAsAde20k(pathForImage)

# add overlay 
segmask, output2 = segmant_image.segmentAsAde20k(pathForImage, overlay = True)


cv2.imshow('Original Image', img)
cv2.imshow('img2', output)
cv2.imshow('img3', output2)

cv2.imwrite('Object-Detection/PixelLib/girl-dogSegmant.jpg',output)
cv2.imwrite('Object-Detection/PixelLib/girl-dogSegmantOverlay.jpg',output2)

cv2.waitKey(0)
cv2.destroyAllWindows()