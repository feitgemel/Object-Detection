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

# The model directory has several files in this format : mask_rcnn_model.*
# It is saved with the epoch number

# we would like to evaluate each model and find the best one

# lets test a specific model :

#train_maskRcnn.evaluate_model("c:/models/mask_rcnn_model.051-0.252276.h5")

# The evaluation for this epoch is :  0.636364 

# we would like to evaluate all the models.
# since the direcroty is not empty , I will just copy all the models to a new directory .

# lets test the result of all models

train_maskRcnn.evaluate_model("c:/models/eval")

# These are the results :
# c:/models/eval\mask_rcnn_model.001-1.361029.h5 evaluation using iou_threshold 0.5 is 0.000000 

# c:/models/eval\mask_rcnn_model.002-0.597196.h5 evaluation using iou_threshold 0.5 is 0.000000 

# c:/models/eval\mask_rcnn_model.004-0.463875.h5 evaluation using iou_threshold 0.5 is 0.272727 

# c:/models/eval\mask_rcnn_model.006-0.376810.h5 evaluation using iou_threshold 0.5 is 0.272727 

# c:/models/eval\mask_rcnn_model.008-0.342451.h5 evaluation using iou_threshold 0.5 is 0.363636 

# c:/models/eval\mask_rcnn_model.010-0.301472.h5 evaluation using iou_threshold 0.5 is 0.454545 

# c:/models/eval\mask_rcnn_model.015-0.267621.h5 evaluation using iou_threshold 0.5 is 0.590909 

# # this is the best model - since it has the high evaluate number : 0.636
# c:/models/eval\mask_rcnn_model.051-0.252276.h5 evaluation using iou_threshold 0.5 is 0.636364 

# mask_rcnn_model.051-0.252276.h5 #

