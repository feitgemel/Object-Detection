# in This tutorial we will learn how to detect objects using semantic segmentation
# we will you two methods : ADE20K and Pascalovc models

# first , lets download both models :

# #https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.3/deeplabv3_xception65_ade20k.h5
#https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5

#lets copy the models to c:/models

import pixellib
from pixellib.semantic import semantic_segmentation

segment_video = semantic_segmentation()
segment_video.load_ade20k_model("c:/models/deeplabv3_xception65_ade20k.h5")

# This is our video :
imgPath = "c:/demo/football.mp4"

#use the model ade20k
segmask1 , output1 = segment_video.process_video_ade20k(imgPath,frames_per_second=15,output_video_name="c:/demo/footballade20k.mp4")

# use the the Pascalvoc model :
segment_video.load_pascalvoc_model("c:/models/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

segmask2 , output2 = segment_video.process_video_pascalvoc(imgPath,frames_per_second=15,output_video_name="c:/demo/footballPas.mp4",overlay=True)

print ('Finish')

