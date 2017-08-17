import numpy as np
import cv2
import csv
import time

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
      green_hue_range=cv2.inRange(hsvimage, np.array((50, 100, 100),dtype = "uint8"), np.array((95, 255, 255),dtype = "uint8"));
        
      green_hue_image=cv2.GaussianBlur(green_hue_range, (9, 9), 2, 2);

      return green_hue_image

def detectcircle(image):
   circles=cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[0]/6,np.array([]),200, 15,5,10)
   return circles

def finaldata(circles_red,circles_green):
   color=[]
   cir_pos=[]
   radious=[]

   len_red=len_green=0
   if circles_red is not None:
      for circles in circles_red[0]:
         c=0
         [x_c,y_c,r]=circles
         cir_pos.append((x_c,y_c))
         color.append(c)
         radious.append(r)

   if circles_green is not None:
      for circles in circles_green[0]:
         c=1
         [x_c,y_c,r]=circles
         radious.append(r)
         cir_pos.append((x_c,y_c))
         color.append(c)

   return cir_pos,color,radious

def process_frame(org_image):
   image=cv2.medianBlur(org_image,3)
   hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV

   start_clrfil=time.time()
   red_hue_image=colordetection(hsvimage,0)
   green_hue_image=colordetection(hsvimage,1)
   clrfil_time=time.time()-start_clrfil

   start_cirdet=time.time()
   circles_red=detectcircle(red_hue_image)               
   circles_green=detectcircle(green_hue_image)
   cirdet_time=time.time()-start_cirdet


   return circles_red, circles_green,clrfil_time,cirdet_time

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


write_file=('data/night_nocrop_nofilter.txt')
g = open(write_file, "wt")
header="frameno"+";"+"frametime"+";"+"colorfiltertime"+";"+"circledettime"+";"+"radious"+";"+"cir_pos"+";"+"color\n"
g.write(header)


# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('night_video/output_night.avi')

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

#The default resolutions are system dependent. We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(round(cap.get(cv2.cv.CV_CAP_PROP_FPS)))


# Define the codec and create VideoWriter object.
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter('videos/night_nocrop_nofilter.avi',fourcc, frame_rate, (frame_width,frame_height))


frame_no=0
# Read until video is completed
while(cap.isOpened()):
   # Capture frame-by-frame
   ret, org_image = cap.read()
   if ret == False:
      break

   start_frame=time.time()
   circles_red,circles_green,clrfil_time,cirdet_time=process_frame(org_image)  
   org_image=draw_circles(circles_red,circles_green,org_image,0,0)

   cir_pos,color,radious=finaldata(circles_red,circles_green)
   
   frame_time=time.time()-start_frame
   out_str=str(frame_no)+";"+str(frame_time)+";"+str(clrfil_time)+";"+str(cirdet_time)+";\""+str(radious)+"\";\""+str(cir_pos)+"\";\""+str(color)+"\"\n"
   g.write(out_str)
   
   out.write(org_image)
   frame_no +=1
   
   if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
      break 

# When everything done, release the video capture object
cap.release()
out.release()
g.close()
 
# Closes all the frames
cv2.destroyAllWindows()
