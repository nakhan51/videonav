import cv2
import numpy as np

vidcap = cv2.VideoCapture('taylor1.MOV')
frame_rate=vidcap.get(cv2.cv.CV_CAP_PROP_FPS)
print frame_rate
