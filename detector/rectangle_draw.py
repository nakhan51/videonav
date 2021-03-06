import cv2
import numpy as np
import glob
import math

### Laplacian Gaussian Filter

# kernel_size = 3
# scale = 1
# delta = 0
# ddepth = cv2.CV_16S


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
   #print circles
   return circles


def drawrectangle(x1,y1,refp,minip,maxip,diffp,refa,minia,maxia,diffa,w,h):
   if diffp > 0:
      y1n= y1+((0-y1)/(maxip-refp))*diffp
   else:
      y1n=y1+((y1-1080)/(refp-minip))*diffp

   if diffa <= 0:
      x1n=x1+((x1-0)/(refa-maxia))*diffa
   else:   
      x1n=x1+((x1-1920)/(refa-minia))*diffa

   x2n=x1n+w
   y2n=y1n+h
   x1n=int(max(0,x1n))
   x2n=int(min(x2n,1920))
   y1n=int(max(0,y1n))
   y2n=int(min(y2n,1080))

   if x2n-x1n<100:
      if x1n==0:
         x2n=x2n+100
      if x2n==1920:
         x1n=x1n-100
   if y2n-y1n<100:
      if y1n==0:
         y2n=y2n+100
      if y2n==1080:
         y1n=y1n-100
    
   return x1n,x2n,y1n,y2n

cap = cv2.VideoCapture("cloudy_video/text_with_sensor.avi")

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(cap.get(cv2.cv.CV_CAP_PROP_FPS ))
#print frame_rate

fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter("videos/rectangle_cl.avi",fourcc, frame_rate, (frame_width,frame_height))

new_file= "cloudy_video/sync.txt" 
f = open(new_file, "r")
lines=f.readlines()
lines=[x.strip('\n')for x in lines]
pitch=[]
roll=[]
azimuth=[]

for row in lines:
    columns= row.split(' ')
    pitch.append(float(columns[2]))
    roll.append(float(columns[3]))
    azimuth.append(float(columns[4]))
pitch_min=min(pitch)
pitch_max=max(pitch)
azimuth_min=min(azimuth)
azimuth_max=max(azimuth)

count=0
detect=False
while(cap.isOpened()):
   ret, org_image = cap.read()
   if ret==False:
      break

   while(not detect):
      image=cv2.medianBlur(org_image,3)
      hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV
        
      red_hue_image=colordetection(hsvimage,0)
      circles_red=detectcircle(red_hue_image)
      #print circles_red        
        
      if circles_red is not None:
         x=[]
         y=[]
         for circles in circles_red[0]:
            [x_c,y_c,r]=circles
            cv2.circle(org_image, (x_c,y_c),r, (255, 0, 0), 3)
            cv2.circle(org_image, (x_c, y_c), 0, (255, 0, 0), 3)
            x.append(x_c)
            y.append(y_c)

         x.sort()
         y.sort()
         x1= int(round(x[0]))
         y1= int(round(y[0]))
         x2= int(round(x[len(x)-1]))
         y2= int(round(y[len(y)-1]))
         detect=True
         firstdraw=True

   if detect == True and firstdraw == True:
      x1=x1-120
      y1=y1-120
      x2=x2+120
      y2=y2+120
      h=y2-y1
      w=x2-x1
      cv2.rectangle(org_image,(x1,y1), (x2,y2),(255,255,255),3)
      out.write(org_image)
      ref_pitch=pitch[count]
      ref_azimuth=azimuth[count]


   if firstdraw == False:
      diff_pitch=pitch[count]-ref_pitch
      diff_azimuth=azimuth[count]-ref_azimuth
      x1_n,x2_n,y1_n,y2_n=drawrectangle(x1,y1,ref_pitch,pitch_min,pitch_max,diff_pitch,ref_azimuth,azimuth_min,azimuth_max,diff_azimuth,w,h)
      #print count,diff_pitch,diff_azimuth,x1_n,y1_n,x2_n,y2_n

      cv2.rectangle(org_image,(int(x1_n),int(y1_n)), (int(x2_n),int(y2_n)),(255,255,255),3)
      out.write(org_image)
   firstdraw=False
   count +=1
         
   if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
      break

cap.release()
f.close()
out.release()
cv2.destroyAllWindows()






