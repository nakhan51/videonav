import numpy as np
import cv2

cap = cv2.VideoCapture("walk_video/text_with_sensor.avi")

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

while(cap.isOpened()):
   ret, org_image = cap.read()
   if ret==False:
      break

   #org_image.release()
cap.release()
cv2.destroyAllWindows()
