# Image classification tutorial - step by step
# This tutorial is based on Tensorflow and does not need any new training
#It is based on pre trained models

# first , install TensorFlow and Numpy
# I also recommend to install OpenCV

#pip install tensorflow
#pip install numpy 

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# lets look at the images that will classify :

filename = 'C:/GitHub/Object-Detection/TensorFlowKeras-PreTrainedModels/dog2.jpg'

#resnet = tf.keras.applications.resnet50.ResNet50()
# lets try another nodel
mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()

from tensorflow.keras.preprocessing import image
img = image.load_img(filename, target_size=(224,224)) # the model works with 224X224 resolution

resizedImage = image.img_to_array(img)
print("Risized image shape")
print(resizedImage.shape)

# we need to add one more dimantion for the image before running the model
imageWithMoreDimantion = np.expand_dims(resizedImage,axis=0)
print("imageWithMoreDimantion image shape")
print(imageWithMoreDimantion.shape)

#finalImage = tf.keras.applications.resnet.preprocess_input(imageWithMoreDimantion)
finalImage = tf.keras.applications.mobilenet.preprocess_input(imageWithMoreDimantion)

#predictions = resnet.predict(finalImage)
predictions = mobile.predict(finalImage)



from tensorflow.keras.applications import imagenet_utils
results = imagenet_utils.decode_predictions(predictions)

print('Results :')
print(results)

#show the image
plt.imshow(img)
plt.show()




