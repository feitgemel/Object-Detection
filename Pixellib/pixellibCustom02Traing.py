# first we have to label the Banana / Apple / Tomato in the images
# we will use lables me

# pip install pyqt5
# pip install labelme

# after labeling the images. lets test it.
#Each image has a json file 

import pixellib
from pixellib.custom_train import instance_custom_training

train_maskRcnn = instance_custom_training()

# num_classes=3 since we have 3 classes : Banana , Apple , Tomato
train_maskRcnn.modelConfig(network_backbone="resnet101",num_classes=3, batch_size=1)

#https://github.com/matterport/Mask_RCNN/releases
# you can download here the 2.0 version for the model 
train_maskRcnn.load_pretrained_model("c:/models/mask_rcnn_coco.h5") 
train_maskRcnn.load_dataset("Object-Detection/Pixellib/customModel")


#Note: The batch_sizes given are samples used for google colab. 
# If you are using a less powerful GPU, reduce your batch size, 
# for example a PC with a 4G RAM GPU you should use a batch size of 1 for both resnet50 or resnet101. 
# I used a batch size of 1 to train my model on my PC’s GPU, 
# train for less than 100 epochs and it produced a validation loss of 0.263. 
# This is favourable because my dataset is not large. 
# A PC with a more powerful GPU you can use a batch size of 2. 
# If you have a large dataset with more classes and much more images use 
# google colab where you have free access to a single 12GB NVIDIA Tesla K80 GPU 
# that can be used up to 12 hours continuously. 
# Most importantly try and use a more powerful GPU and train for 
# more epochs to produce a custom model that will perform efficiently 
# across multiple classes. 

# Achieve better results by training with much more images. 
# 300 images for each each class is recommended to be the minimum required for 
# training.


# path_trained_models -> where will be stored the trained model
train_maskRcnn.train_model(num_epochs=100 , augmentation=True, path_trained_models="c:/models")

# these are the results model
# now , We have to find the best one





