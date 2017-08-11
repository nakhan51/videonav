# import the necessary packages
import numpy as np
import sys
import cv2
import time

def colordetection(hsvimage,flag):
   if flag==0:
      #Threshold the HSV image, keep only the red pixels
      lower_red_hue_range=cv2.inRange(hsvimage, np.array((0, 100, 100),dtype = "uint8"), np.array((10, 255, 255),dtype = "uint8"));
      upper_red_hue_range=cv2.inRange(hsvimage, np.array((160, 100, 100),dtype = "uint8"), np.array((179, 255, 255),dtype = "uint8"));

      #Combine the above two images
      red_hue_image=cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0);
      red_hue_image=cv2.GaussianBlur(red_hue_image, (9, 9), 2, 2);
      
      # red_lap = cv2.Laplacian(red_hue_image,ddepth,ksize = kernel_size,scale = scale,delta = delta)
      # dst = cv2.convertScaleAbs(red_lap)
      # #dst=cv2.GaussianBlur(dst, (9, 9), 2, 2);
      # cv2.imshow('laplacian',dst)
      # cv2.waitKey(0)
      return red_hue_image

   else:
      #Threshold the HSV image, keep only the red pixels
      green_hue_range=cv2.inRange(hsvimage, np.array((50, 100, 100),dtype = "uint8"), np.array((95, 255, 255),dtype = "uint8"));
        
      green_hue_image=cv2.GaussianBlur(green_hue_range, (9, 9), 2, 2);

      #gray_lap = cv2.Laplacian(green_hue_image,ddepth,ksize = kernel_size,scale = scale,delta = delta)
      #dst_green = cv2.convertScaleAbs(gray_lap)
      #cv2.imshow('laplacian',dst)
      #cv2.waitKey(0)
      return green_hue_image

def detectcircle(image):
   circles=cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[0]/6,np.array([]),200, 15,5,10)
   return circles

def process_frame(org_image):
   image=cv2.medianBlur(org_image,3)
   hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV
   
   red_hue_image=colordetection(hsvimage,0)
   circles_red=detectcircle(red_hue_image)            
      
   green_hue_image=colordetection(hsvimage,1)
   circles_green=detectcircle(green_hue_image)


   return circles_red, circles_green


def draw_circles(circles_red,circles_green,org_image,shiftx,shifty):
   if circles_red is not None:
      for circles in circles_red[0]:
         [x_c,y_c,r]=circles
         x_c=int(x_c+shiftx)
         y_c=int(y_c+shifty)
         cv2.circle(org_image, (x_c,y_c),r, (255, 0, 0), 3)
         cv2.circle(org_image, (x_c, y_c), 0, (255, 0, 0), 3)
         cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)

   if circles_green is not None:
      for circles in circles_green[0]:
         [x_c,y_c,r]=circles
         x_c=int(x_c+shiftx)
         y_c=int(y_c+shifty)
         cv2.circle(org_image, (x_c,y_c),r, (255, 0, 0), 3)
         cv2.circle(org_image, (x_c, y_c), 0, (255, 0, 0), 3)
         cv2.putText(org_image,"green  go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)

   return org_image

# load the image

org_image = cv2.imread('plots/frame502.jpg')

circles_red, circles_green = process_frame(org_image)

if(circles_red is not None or circles_green is not None):
   org_image=draw_circles(circles_red,circles_green,org_image,0,0)

cv2.imshow("Detected red circles on the input image", org_image)
cv2.waitKey(0)

