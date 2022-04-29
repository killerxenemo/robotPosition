import cv2
from PIL import Image
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    np3D=np.array(frame)
    print(np3D.shape)
    key = cv2.waitKey(500) # espera a una tecla n milisegons
    if key == 27: # exit on ESC
        break
vc.release()
cv2.destroyWindow("preview")