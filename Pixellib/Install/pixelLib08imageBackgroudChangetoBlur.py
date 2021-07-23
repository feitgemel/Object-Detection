# this tutorial elaborates how to change a background of an image to blur

# Download the model
# #https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5
# copy the file to c:/models

import cv2
import pixellib
from pixellib.tune_bg import alter_bg

img = cv2.imread('Object-Detection/PixelLib/friends2b.jpg')
change_bg = alter_bg()

change_bg.load_pascalvoc_model('c:/models/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')

# use the model for blur the image
img2 = change_bg.blur_bg('Object-Detection/PixelLib/friends2b.jpg', moderate = True)

# show the image
cv2.imshow('Original image',img)

# show the Blur image
cv2.imshow('img2',img2)

# write the new image
cv2.imwrite('Object-Detection/PixelLib/friends2bBlur.jpg',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
