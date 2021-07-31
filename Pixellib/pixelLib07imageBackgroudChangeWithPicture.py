# this tutorial elaborates how to change a background of an image with another image

# Download the model
# #https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5
# copy the file to c:/models

import cv2
import pixellib
from pixellib.tune_bg import alter_bg

img = cv2.imread('Object-Detection/PixelLib/friends2b.jpg')
change_bg = alter_bg()

change_bg.load_pascalvoc_model('c:/models/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')


# lets see the image that would be the background :
#img2 = cv2.imread('Object-Detection/PixelLib/snowBackground.jpg')
img2 = change_bg.change_bg_img(f_image_path = 'Object-Detection/PixelLib/friends2b.jpg', b_image_path = 'Object-Detection/PixelLib/snowBackground.jpg')

# show the image
cv2.imshow('Original image',img)
cv2.imshow('img2',img2)
cv2.imwrite('Object-Detection/PixelLib/friends2bPic.jpg',img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
