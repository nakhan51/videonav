# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
org_image = cv2.imread(args["image"])
image=cv2.medianBlur(org_image,3)

# Convert input image to HSV
hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);
#cv2.imshow("red_hue",hsvimage)
#cv2.waitKey(0)

#Threshold the HSV image, keep only the red pixels
lower_red_hue_range=cv2.inRange(hsvimage, np.array((0, 100, 100),dtype = "uint8"), np.array((10, 255, 255),dtype = "uint8"));
upper_red_hue_range=cv2.inRange(hsvimage, np.array((160, 100, 100),dtype = "uint8"), np.array((179, 255, 255),dtype = "uint8"));

#Combine the above two images
red_hue_image=cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0);
red_hue_image=cv2.GaussianBlur(red_hue_image, (9, 9), 2, 2);
cv2.imshow("red_hue",red_hue_image)
cv2.waitKey(0)

# Use the Hough transform to detect circles in the combined threshold image
circles=cv2.HoughCircles(red_hue_image, cv2.cv.CV_HOUGH_GRADIENT, 1, red_hue_image.shape[0]/4,np.array([]),200, 12,2,4)
print circles
#print red_hue_image.shape[0]/4

if circles is not None:
   a, b, c = circles.shape
   for i in range(b):
       cv2.circle(org_image, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 2)
       cv2.circle(org_image, (circles[0][i][0], circles[0][i][1]), 1, (0, 255, 0), 1)
       cv2.putText(org_image,"red don't go",(circles[0][i][0], circles[0][i][1]),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  

# show the images
   cv2.imshow("Detected red circles on the input image", org_image)
   cv2.waitKey(0)

