# first we have to label the Banana / Apple / Tomato in the images
# we will use lables me

# pip install pyqt5
# pip install labelme

# after labeling the images. lets test it.
#Each image has a json file 

import pixellib
from pixellib.custom_train import instance_custom_training

vis_img = instance_custom_training()
vis_img.load_dataset("Object-Detection\Pixellib\customModel")

vis_img.visualize_sample()