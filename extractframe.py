import cv2
import numpy as np

vidcap = cv2.VideoCapture('sensor_video/output_sensor.avi')
if (vidcap.isOpened()== False): 
	print("Error opening video stream or file")

success,image = vidcap.read()
count = 0

success = True
while success:
  success,image = vidcap.read()
  if count >694:
          cv2.imwrite("sensor_video/green/frame%d.jpg" %count, image)  
  count += 1#
  if count == 895:
          break

  
