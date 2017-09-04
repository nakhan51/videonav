import cv2
import numpy as np

vidcap = cv2.VideoCapture('videos/sensor_nocrp_nofil.avi')
if (vidcap.isOpened()== False): 
	print("Error opening video stream or file")

success,image = vidcap.read()
count = 0

success = True
while success:
  success,image = vidcap.read()
  if count >950:
          cv2.imwrite("videos/frame%d.jpg" %count, image)  
  count += 1#
  if count == 1200:
          break

  
