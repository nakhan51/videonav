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
   circles=cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, image.shape[0]/6,np.array([]),200, 15,5,8)
   #print circles
   return circles




#img = cv2.imread('extra/pitch_frame/frame15.jpg')
#filenames = [i for i in glob.glob("sensor_video/frame/*.jpg")]
#filenames.sort() # ADD THIS LINE








cap = cv2.VideoCapture("sensor_video/text_with_sensor.avi")

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(cap.get(cv2.cv.CV_CAP_PROP_FPS ))
#print frame_rate

fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter("sensor_video/rectangle.avi",fourcc, 10, (frame_width,frame_height))

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
#print pitch,roll,azimuth

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
         draw=True

   if detect == True and draw == True:
      x1=x1-50
      y1=y1-50
      x2=x2+50
      y2=y2+50
      cv2.rectangle(org_image,(x1,y1), (x2,y2),(255,255,255),3)
      out.write(org_image)
      count +=1
      draw=False

   if draw == False:
      diff_pitch=pitch[count]-pitch[count-1]
      diff_azimuth=azimuth[count]-azimuth[count-1]
      if diff_pitch > 0 and diff_azimuth > 0:
         x1=x1-diff_azimuth*30
         y1=y1-diff_pitch*21
         x2=x2-diff_azimuth*30
         y2=y2-diff_pitch*21
         cv2.rectangle(org_image,(int(x1),int(y1)), (int(x2),int(y2)),(255,255,255),3)
      elif diff_pitch > 0 and diff_azimuth < 0:
         x1=x1+diff_azimuth*30
         y1=y1-diff_pitch*21
         x2=x2+diff_azimuth*30
         y2=y2-diff_pitch*21
         cv2.rectangle(org_image,(int(x1),int(y1)), (int(x2),int(y2)),(255,255,255),3)
      elif diff_pitch < 0 and diff_azimuth < 0:
         x1=x1+diff_azimuth*30
         y1=y1+diff_pitch*21
         x2=x2+diff_azimuth*30
         y2=y2+diff_pitch*21
         cv2.rectangle(org_image,(int(x1),int(y1)), (int(x2),int(y2)),(255,255,255),3)
      elif diff_pitch < 0 and diff_azimuth > 0:
         x1=x1-diff_azimuth*30
         y1=y1+diff_pitch*21
         x2=x2-diff_azimuth*30
         y2=y2+diff_pitch*21
         cv2.rectangle(org_image,(int(x1),int(y1)), (int(x2),int(y2)),(255,255,255),3)
      out.write(org_image)
      count +=1
         
   if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
      break

cap.release()
f.close()
out.release()
cv2.destroyAllWindows()






