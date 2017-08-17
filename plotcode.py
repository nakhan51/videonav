# import the necessary packages
import numpy as np
import sys
import cv2
import time
import argparse
import glob
import math

def colordetection(hsvimage,flag):
   if flag==0:
      #Threshold the HSV image, keep only the red pixels
      lower_red_hue_range=cv2.inRange(hsvimage, np.array((0, 100, 100),dtype = "uint8"), np.array((10, 255, 255),dtype = "uint8"));
      upper_red_hue_range=cv2.inRange(hsvimage, np.array((160, 100, 100),dtype = "uint8"), np.array((179, 255, 255),dtype = "uint8"));

      #Combine the above two images
      red_hue_image=cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0);
      red_hue_image=cv2.GaussianBlur(red_hue_image, (9, 9), 2, 2);
      
      return red_hue_image

   else:
      #Threshold the HSV image, keep only the red pixels
      green_hue_range=cv2.inRange(hsvimage, np.array((65, 100, 100),dtype = "uint8"), np.array((95, 255, 255),dtype = "uint8"));
        
      green_hue_image=cv2.GaussianBlur(green_hue_range, (9, 9), 2, 2);

      return green_hue_image


def drawcircle(org_image,image,flag,hsvimage):
   if flag==0:
      text="Red Circle"
   else:
      text="Green Circle"
   circles=cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[0]/6,np.array([]),200, 15,5,8)


   if circles is not None:
      a, b, c = circles.shape
      for i in range(b):
         x=int((circles[0][i][0]))
         y=int((circles[0][i][1]))
         r=int(round(circles[0][i][2]))
         cv2.circle(org_image, (x, y), (r+2), (255, 255, 255), 2)
         cv2.putText(org_image,text,(x-10, y-20),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,255,255), 2)  
   return org_image


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input dataset of images")
args = vars(ap.parse_args())
i=0 
# loop over the images
for imagePath in glob.glob(args["images"] + "/*.png"):
   org_image = cv2.imread(imagePath)

   image=cv2.medianBlur(org_image,3)

   # Convert input image to HSV
   hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);
   #huerange=cv2.inRange(hsvimage, np.array((0, 10, 10),dtype = "uint8"), np.array((179, 255, 255),dtype = "uint8"));

   red_hue_image=colordetection(hsvimage,1)
   #res_red=cv2.bitwise_and(org_image,org_image, mask= red_hue_image)

   #green_hue_image=colordetection(hsvimage,0)
   #res_green=cv2.bitwise_and(org_image,org_image, mask= green_hue_image)

   #red_green=cv2.addWeighted(red_hue_image, 1.0, green_hue_image, 1.0, 0.0);
   #res_red_green = cv2.bitwise_and(org_image,org_image, mask= red_green)

   
   # red circle draw
   #img=drawcircle(red_hue_image,red_hue_image,1)


   org_image=drawcircle(org_image,red_hue_image,1,hsvimage)

   i +=1

   #cv2.imshow("circle", org_image)
   #cv2.waitKey(0)


