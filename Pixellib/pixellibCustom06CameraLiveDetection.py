# in this lesson we will use our pre trained model and detect out trained objects in live camera
# We copy some of the code from our previous lesson
import pixellib
import cv2
import numpy as np
from pixellib.instance import custom_segmentation


segment_image = custom_segmentation()
segment_image.inferConfig(network_backbone="resnet101",num_classes=3,class_names=["BG","Banana","Apple","Tomato"])
segment_image.load_model("c:/models/eval/mask_rcnn_model.032-0.200773.h5") 

# lets load the camera

capture = cv2.VideoCapture(0)

while True:
    ret , frame = capture.read() # read the frame

    # analyse the frame using our model
    segmask , out = segment_image.segmentFrame(frame, show_bboxes=True , extract_segmented_objects=True,save_extracted_objects=True,text_thickness=1,text_size=0.6, box_thickness=2,verbose=None)

    cv2.imshow("frame", frame)

    if cv2.waitKey(25) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()   


