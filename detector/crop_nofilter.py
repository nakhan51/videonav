import cv2
import numpy as np
import csv
import math
import time

RECTANGLE_INIT_SIZE=120
SCAN_INCREMENT_WIDTH=100
SCAN_INCREMENT_HEIGHT=120
REC_INC_WIDTH=5
REC_INC_HEIGHT=5
MAX_HEIGHT=100
MAX_WIDTH=100
HISTORY_SIZE=10
FACTOR=2
REC_AREA=1920*1080
SINGLE_LGT_RIGHT=300
SINGLE_LGT_LEFT=200

def readfile(new_file):
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

   return pitch,roll,azimuth

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
   return circles


def drawrectangle(x1,y1,pitch_data,azimuth_data,w,h):
   refp,minip,maxip,diffp=pitch_data
   refa,minia,maxia,diffa=azimuth_data
   dena= refa-minia
   numa=refa-maxia
   denp=refp-minip
   nump=maxip-refp
   if dena  == 0:
      dena =1
   if numa == 0:
      numa=1
   if denp  == 0:
      dena =1
   if nump == 0:
      numa=1
      
   if diffp > 0:
      y1n= y1+((0-y1)/(nump))*diffp
   else:
      y1n=y1+((y1-frame_height)/(denp))*diffp

   if diffa <= 0:
      x1n=x1+((x1-0)/(numa))*diffa
   else:   
      x1n=x1+((x1-frame_width)/(dena))*diffa

   x1n=int(max(0,x1n))
   y1n=int(max(0,y1n))
   x2n=x1n+w
   y2n=y1n+h
   x2n=int(min(x2n,frame_width))
   y2n=int(min(y2n,frame_height))

   if x2n-x1n < MAX_WIDTH:
      if x1n == 0:
         x2n = x2n+MAX_WIDTH
      if x2n == frame_width:
         x1n = x1n-MAX_WIDTH
   if y2n-y1n < MAX_HEIGHT:
      if y1n == 0:
         y2n = y2n+MAX_HEIGHT
      if y2n == frame_height:
         y1n = y1n-MAX_HEIGHT
         
   return x1n,x2n,y1n,y2n


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

def update_reference(circles_red, circles_green, frame_no):
   circles_x=[]
   circles_y=[]

   # TODO: is this a valid logic? if both red and green are detected then the bounding box will
   # take all of them together
   if circles_red is not None:
      for circles in circles_red[0]:
         [x_c,y_c,r]=circles
         circles_x.append(x_c)
         circles_y.append(y_c)

   if circles_green is not None:
      for circles in circles_green[0]:
         [x_c,y_c,r]=circles
         circles_x.append(x_c)
         circles_y.append(y_c)
         
   circles_x.sort()
   circles_y.sort()
   x1= int(round(circles_x[0]))
   y1= int(round(circles_y[0]))
   x2= int(round(circles_x[len(circles_x)-1]))
   y2= int(round(circles_y[len(circles_y)-1]))

   
   x1=x1-RECTANGLE_INIT_SIZE
   y1=y1-RECTANGLE_INIT_SIZE
   x2=x2+RECTANGLE_INIT_SIZE
   y2=y2+RECTANGLE_INIT_SIZE
   h=y2-y1
   w=x2-x1
   if (circles_red is not None or circles_green is not None):
      len_red=len_green=0
      if circles_red is not None:
         len_red=len(circles_red[0])
      if circles_green is not None:
         len_green=len(circles_green[0])
      if len_red == 1 or len_green == 1:
         if x1<=400:
            x1=max(50,x1-SINGLE_LGT_LEFT)
            x2=min(x2+SINGLE_LGT_RIGHT,1900)
         if x1>400:
            x1=max(50,x1-SINGLE_LGT_RIGHT)
            x2=min(x2+SINGLE_LGT_LEFT,1900)
         w=x2-x1

   ref_pitch=pitch[frame_no]
   ref_azimuth=azimuth[frame_no]
   
   return x1, y1, x2, y2, h, w, ref_pitch, ref_azimuth


def process_frame(org_image):
   #print org_image.shape
   image=cv2.medianBlur(org_image,3)
   hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV
   
   red_hue_image=colordetection(hsvimage,0)
   circles_red=detectcircle(red_hue_image)            
   
   green_hue_image=colordetection(hsvimage,1)
   circles_green=detectcircle(green_hue_image)


   return circles_red, circles_green

def finaldata(circles_red,circles_green,shiftx,shifty):
   color=[]
   cir_pos=[]

   if circles_red is not None:
      for circles in circles_red[0]:
         c=0
         [x_c,y_c,r]=circles
         x_c=int(x_c+shiftx)
         y_c=int(y_c+shifty)
         cir_pos.append((x_c,y_c))
         color.append(c)

   if circles_green is not None:
      for circles in circles_green[0]:
         c=1
         [x_c,y_c,r]=circles
         x_c=int(x_c+shiftx)
         y_c=int(y_c+shifty)
         cir_pos.append((x_c,y_c))
         color.append(c)

   return cir_pos,color


def recarea(x1,y1,x2,y2):
   width=x2-x1
   height=y2-y1
   area=width*height

   return area

cap = cv2.VideoCapture("sunny_video/output_sunny.avi")

if (cap.isOpened()== False): 
   print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(round(cap.get(cv2.cv.CV_CAP_PROP_FPS )))


fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter("videos/sunny_crop_nofilter2.avi",fourcc, frame_rate, (frame_width,frame_height))

new_file= "sunny_video/sync.txt" 

pitch,roll,azimuth=readfile(new_file)
pitch_min=min(pitch)
pitch_max=max(pitch)
azimuth_min=min(azimuth)
azimuth_max=max(azimuth)



write_file=('data/sunny_crop_nofilter2.txt')
g = open(write_file, "wt")
header="frameno"+";"+"frametime"+";"+"recarea"+";"+"cir_pos"+";"+"color\n"
g.write(header)


is_first_frame=True
frame_no=0
x1=y1=x2=y2=h=w=ref_pitch=ref_azimuth = None

circle_count_history=[]

while(cap.isOpened()):
   
   ret, org_image = cap.read()
   if ret==False:
      break
   newrec= -1
   circ_pos=[]
   color=[]
   start_frame=time.time()
      
   if(is_first_frame):
      circles_red, circles_green = process_frame(org_image)
      #print circles_green, circles_red
      if(circles_red is not None or circles_green is not None):
         x1, y1, x2, y2, h, w, ref_pitch, ref_azimuth = update_reference(circles_red, circles_green, frame_no)
         org_image=draw_circles(circles_red,circles_green,org_image,0,0)
         cv2.rectangle(org_image,(x1,y1), (x2,y2),(255,255,255),3)
         circ_pos,color=finaldata(circles_red,circles_green,0,0)
         newrec=recarea(0,0,1920,1080)
         is_first_frame=False

   else:
      diff_pitch=pitch[frame_no]-ref_pitch
      diff_azimuth=azimuth[frame_no]-ref_azimuth
      pitch_data=[ref_pitch,pitch_min,pitch_max,diff_pitch]
      azimuth_data=[ref_azimuth,azimuth_min,azimuth_max,diff_azimuth]
      x1_n,x2_n,y1_n,y2_n=drawrectangle(x1,y1,pitch_data,azimuth_data,w,h)
   
      i=0
      rec=3
      while True:
         img=org_image[y1_n:y2_n,x1_n:x2_n]
         
         circles_red,circles_green=process_frame(img)
         

         if (circles_red is None and circles_green is None): # no cicles currently, so we need to search larger area
            #if (((x2r-x1r)*(y2r-y1r)>=0.9*REC_AREA) or i==3) : 
                  #break
            if (((x2_n-x1_n)*(y2_n-y1_n)>=0.9*REC_AREA) or i==2) : 
                  break
            if i>0:
               # x1_n=0
               # y1_n=0
               # x2_n=1920
               # y2_n=1080
               # x1_n=int(max(0,x1_n-SCAN_INCREMENT_WIDTH*FACTOR))
               # y1_n=int(max(0,y1_n-SCAN_INCREMENT_HEIGHT*FACTOR))
               # x2_n=int(min(frame_width, x2_n+SCAN_INCREMENT_WIDTH*FACTOR))
               # y2_n=int(min(frame_height, y2_n+SCAN_INCREMENT_HEIGHT*FACTOR))
               # newrec= newrec+ recarea(x1_n,y1_n,x2_n,y2_n)
               
               if rec==3:
                  x1_n=int(max(0,x1r-SCAN_INCREMENT_WIDTH*FACTOR))
                  y1_n=int(max(0,y1r-SCAN_INCREMENT_HEIGHT*FACTOR))
                  x2_n=int(min(frame_width, x2r+SCAN_INCREMENT_WIDTH*FACTOR))
                  y2_n=int(min(frame_height, y1r+REC_INC_HEIGHT*FACTOR))
                  newrec= newrec+ recarea(x1_n,y1_n,x2_n,y2_n)               
               if rec==2:
                  x1_n=int(max(0,x2r-REC_INC_WIDTH*FACTOR))
                  y1_n=int(max(0,y1r))
                  x2_n=int(min(frame_width, x2r+SCAN_INCREMENT_WIDTH*FACTOR))
                  y2_n=int(min(frame_height, y2r))
                  newrec= newrec+ recarea(x1_n,y1_n,x2_n,y2_n)
                                 
               if rec==1:
                  x1_n=int(max(0,x1r-SCAN_INCREMENT_WIDTH*FACTOR))
                  y1_n=int(max(0,y1r))
                  x2_n=int(min(frame_width, x1r+REC_INC_WIDTH*FACTOR))
                  y2_n=int(min(frame_height, y2r))
                  newrec= newrec+ recarea(x1_n,y1_n,x2_n,y2_n)
               if rec==0:
                  x1_n=int(max(0,x1r-SCAN_INCREMENT_WIDTH*FACTOR))
                  y1_n=int(max(0,y2r-REC_INC_HEIGHT*FACTOR))
                  x2_n=int(min(frame_width, x2r+SCAN_INCREMENT_WIDTH*FACTOR))
                  y2_n=int(min(frame_height, y2r+SCAN_INCREMENT_HEIGHT*FACTOR))
                  newrec= newrec+ recarea(x1_n,y1_n,x2_n,y2_n)
                  rec=4
                  i +=1
                  x1r=int(max(0,x1r-SCAN_INCREMENT_WIDTH*FACTOR))
                  y1r=int(max(0,y1r-SCAN_INCREMENT_HEIGHT*FACTOR))
                  x2r=int(min(frame_width, x2r+SCAN_INCREMENT_WIDTH*FACTOR))
                  y2r=int(min(frame_height, y2r+SCAN_INCREMENT_HEIGHT*FACTOR))
               rec-=1
               #print x1_n,y1_n,x2_n,y2_n
               #print i
            else:
               x1_n = max(0, x1_n-SCAN_INCREMENT_WIDTH)
               y1_n = max(0, y1_n-SCAN_INCREMENT_HEIGHT)
               x2_n = min(frame_width, x2_n+SCAN_INCREMENT_WIDTH)
               y2_n = min(frame_height, y2_n+SCAN_INCREMENT_HEIGHT)
               x1r=x1_n
               y1r=y1_n
               x2r=x2_n
               y2r=y2_n
               newrec=recarea(x1_n,y1_n,x2_n,y2_n)
               
               i +=1
               
         else: # either red or green is detected            
            cv2.rectangle(org_image,(x1_n,y1_n), (x2_n,y2_n),(255,255,255),3)
            newrec=recarea(x1_n,y1_n,x2_n,y2_n)
            break
         
         #if i==2:
            #break
        
      if (circles_red is not None or circles_green is not None):

         if(i>0): # rectangle was increased for search, so need to update reference.
            x1, y1, x2, y2, h, w, ref_pitch, ref_azimuth = update_reference(circles_red, circles_green, frame_no)
   
         org_image=draw_circles(circles_red,circles_green,org_image,x1_n,y1_n)
         circ_pos,color=finaldata(circles_red,circles_green,x1_n,y1_n)
         
   #print circ_pos
   frame_time=time.time()-start_frame
   out_str=str(frame_no)+";"+str(frame_time)+";\""+str(newrec)+"\";\""+str(circ_pos)+"\";\""+str(color)+"\"\n"
   g.write(out_str)

   out.write(org_image)
   frame_no +=1
   
   if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
      break


cap.release()
#f.close()
g.close()
out.release()
cv2.destroyAllWindows()
