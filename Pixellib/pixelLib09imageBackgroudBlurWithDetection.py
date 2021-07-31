# In the tutorial we will learn how to detect an object in an image , and blur all the rest as a background

# download the model
#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/xception_pascalvoc.pb
# copy the model file to c:/models

import cv2
import pixellib
from pixellib.tune_bg import alter_bg

img = cv2.imread('Object-Detection/PixelLib/man-car.jpg')

#load the model
change_bg = alter_bg(model_type="pb")
change_bg.load_pascalvoc_model('c:/models/xception_pascalvoc.pb')

# step 1 : extract the person in the image
output = change_bg.blur_bg('Object-Detection/PixelLib/man-car.jpg',extreme = True, detect = "person")

# step 2 : change the background color to green 
output2 = change_bg.color_bg('Object-Detection/PixelLib/man-car.jpg',colors = (0,128,0), detect = "person")


# show the image
cv2.imshow('original image',img)

# show the image after the model
cv2.imshow('img2',output)

# show the third image after the model
cv2.imshow('img3',output2)

cv2.imwrite('Object-Detection/PixelLib/man-carBlur.jpg',output)
cv2.imwrite('Object-Detection/PixelLib/man-cargreen.jpg',output2)

cv2.waitKey(0)

cv2.destroyAllWindows()