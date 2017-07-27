import cv2
import numpy as np
import glob
import math

SCAN_INCREMENT=150

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
   circles=cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[0]/6,np.array([]),200, 15,5,8)
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

def scanarea(x1_n,x2_n,y1_n,y2_n,org_image):
   img=org_image[y1_n:y2_n,x1_n:x2_n]

   image=cv2.medianBlur(img,3)
   hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV
        
   red_hue_image=colordetection(hsvimage,0)
   circles_red=detectcircle(red_hue_image)

   green_hue_image=colordetection(hsvimage,1)
   circles_green=detectcircle(green_hue_image)
   
   return circles_red,circles_green



   
cap = cv2.VideoCapture("sensor_video/text_with_sensor.avi")

# Check if camera opened successfully
if (cap.isOpened()== False): 
   print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(round(cap.get(cv2.cv.CV_CAP_PROP_FPS )))

fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter("sensor_video/cropanddetect2.avi",fourcc, frame_rate, (frame_width,frame_height))

new_file= "sensor_video/sync.txt" 
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
            cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)
            x.append(x_c)
            y.append(y_c)

         x.sort()
         y.sort()
         x1= int(round(x[0]))
         y1= int(round(y[0]))
         x2= int(round(x[len(x)-1]))
         y2= int(round(y[len(y)-1]))
          
      green_hue_image=colordetection(hsvimage,1)
      circles_green=detectcircle(green_hue_image)

      if circles_green is not None:
         x=[]
         y=[]
         for circles in circles_green[0]:
            [x_c,y_c,r]=circles
            cv2.circle(org_image, (x_c,y_c),r, (255, 0, 0), 3)
            cv2.circle(org_image, (x_c, y_c), 0, (255, 0, 0), 3)
            cv2.putText(org_image,"green  go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)
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
      x1=x1-100
      y1=y1-100
      x2=x2+100
      y2=y2+100
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

      print x1_n,y1_n,x2_n,y2_n

      i=0
      while True:
         i +=1
         circles_red,_=scanarea(x1_n,x2_n,y1_n,y2_n,org_image)
                  
         print circles_red
         if circles_red is None:

            x1_n = max(0,x1_n-SCAN_INCREMENT)
            y1_n = max(0,y1_n-SCAN_INCREMENT)
            x2_n = min(1920,x2_n+SCAN_INCREMENT)
            y2_n = min(1080,y2_n+SCAN_INCREMENT)
            
         else:
            cv2.rectangle(org_image,(x1_n,y1_n), (x2_n,y2_n),(255,255,255),3)        
            break
         
         if i==2:
            break
         
      if circles_red is not None:
         for circles in circles_red[0]:
            [x_c,y_c,r]=circles
            x_c=int(x_c+x1_n)
            y_c=int(y_c+y1_n)
            cv2.circle(org_image, (x_c,y_c),r, (255, 0, 0), 3)
            cv2.circle(org_image, (x_c, y_c), 0, (255, 0, 0), 3)
            cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)

         cv2.rectangle(org_image,(x1_n,y1_n), (x2_n,y2_n),(255,255,255),3)        
            
      _,circles_green=scanarea(x1_n,x2_n,y1_n,y2_n,org_image)
         

      if circles_green is not None:
         for circles in circles_green[0]:
            [x_c,y_c,r]=circles
            x_c=int(x_c+x1_n)
            y_c=int(y_c+y1_n)
            cv2.circle(org_image, (x_c,y_c),r, (255, 0, 0), 3)
            cv2.circle(org_image, (x_c, y_c), 0, (255, 0, 0), 3)
            cv2.putText(org_image,"green  go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)

   out.write(org_image)
   firstdraw=False
   count +=1
         
   if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
      break

cap.release()
f.close()
out.release()
cv2.destroyAllWindows()

