# import the necessary packages
import numpy as np
import sys
import cv2

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

def drawcircle(org_image,image,flag):
   if flag==1:
      text="red don't go"
   else:
      text="green go"
   circles=cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[0]/6,np.array([]),200, 15,5,8)
   print circles


   if circles is not None:
      a, b, c = circles.shape
      for i in range(b):
         cv2.circle(org_image, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 2)
         print (circles[0][i][0], circles[0][i][1])
         cv2.circle(org_image, (circles[0][i][0], circles[0][i][1]), 1, (0, 255, 0), 1)
         cv2.putText(org_image,text,(circles[0][i][0], circles[0][i][1]),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  
   return org_image

kernel_size = 3
scale = 2
delta = 0
ddepth = cv2.CV_16S

# load the image
org_image = cv2.imread('/home/nishat/opencv_test/sensor_video/frame/frame1500.jpg')
image=cv2.medianBlur(org_image,3)

# Convert input image to HSV
hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);

red_hue_image=colordetection(hsvimage,0)

# red circle draw
org_image=drawcircle(org_image,red_hue_image,1)  

green_hue_image=colordetection(hsvimage,1)

# green circle draw
org_image=drawcircle(org_image,green_hue_image,0)
      
# show the images
cv2.imshow("Detected red circles on the input image", org_image)
cv2.waitKey(0)

