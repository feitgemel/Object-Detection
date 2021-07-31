import cv2
import pixellib
from pixellib.tune_bg import alter_bg

# download the model from this link

#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5

# copy the file to c:\modes directory

# load our image

img = cv2.imread('Object-Detection/PixelLib/friends2b.jpg')
change_bg = alter_bg()

change_bg.load_pascalvoc_model('c:/models/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')


# green backgroudr
output = change_bg.color_bg('Object-Detection/PixelLib/friends2b.jpg', colors = (0,128,0))

# white background
outputWhite = change_bg.color_bg('Object-Detection/PixelLib/friends2b.jpg', colors = (255,255,255))


cv2.imshow('img original',img)
cv2.imshow('output',output)
cv2.imshow('output2',outputWhite)



cv2.waitKey(0)
cv2.destroyAllWindows()

