
import numpy as np
import cv2
import csv

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

def midpointcircledraw(x_c,y_c,r):
    point=[]
    x=0;
    y=r;
    
    point.append((x_c+x,y_c+y))
    point.append((x_c+x,y_c-y))
    point.append((x_c-x,y_c+y))
    point.append((x_c-x,y_c-y))
    point.append((x_c+y,y_c+x))
    point.append((x_c+y,y_c-x))
    point.append((x_c-y,y_c+x))
    point.append((x_c-y,y_c-x))
     
    #Initialising the value of D
    d = 5/4 - r
    while x < y:
        # Mid-point is inside or on the perimeter
        if (d < 0):
            d=d+2*x+1
        #Mid-point is outside the perimeter
        else:
            d=d+2*x-2*y+1
            y -=1
        x+=1
         
        #All the perimeter points have already been printed
         
        point.append((x_c+x,y_c+y))
        point.append((x_c+x,y_c-y))
        point.append((x_c-x,y_c+y))
        point.append((x_c-x,y_c-y))
        point.append((x_c+y,y_c+x))
        point.append((x_c+y,y_c-x))
        point.append((x_c-y,y_c+x))
        point.append((x_c-y,y_c-x))

    return point



# blackrange=50
# percentile=80
# # load the image


# # Create a VideoCapture object and read from input file
# cap = cv2.VideoCapture('sensor_video/output_sensor.avi')

# # Check if camera opened successfully
# if (cap.isOpened()== False): 
# 	print("Error opening video stream or file")

# #The default resolutions are system dependent. We convert the resolutions from float to integer.
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# frame_rate=int(round(cap.get(cv2.cv.CV_CAP_PROP_FPS)))


# # Define the codec and create VideoWriter object.
# fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
# out = cv2.VideoWriter('sensor_video/detection_sensor.avi',fourcc, 10, (frame_width,frame_height))
# #org_image = cv2.imread('sensor_video/frame/frame650.jpg')

# # Read until video is completed
# while(cap.isOpened()):
#     	# Capture frame-by-frame
# 	ret, org_image = cap.read()
# 	if ret == False:
# 		break
#         image=cv2.medianBlur(org_image,3)

#         # Convert input image to HSV
#         hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);

#         red_hue_image=colordetection(hsvimage,0)

#         # red circle draw
#         circles_red=detectcircle(red_hue_image)
#         print circles_red
#         if circles_red is not None:
#             for circles in circles_red[0]:
#                 [x_c,y_c,r]=circles    
#                 point= midpointcircledraw(x_c,y_c,(r+1.2))
#                 count=0
#                 for i in range(0,len(point)):
#                     x,y = point[i]
#                     color=(hsvimage[int(y),int(x)])
#                     if color[2]<= blackrange:
#                         count+=1
#                 print(count/float(len(point)))*100,color[2]        
#                 if (count/float(len(point)))*100 <= percentile:
        
#                     cv2.circle(org_image, (x_c, y_c), r, (0, 0, 255), 2)
#                     cv2.circle(org_image, (x_c, y_c), 1, (0, 255, 0), 1)
#                     cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  

#         green_hue_image=colordetection(hsvimage,0)

#         # green circle draw
#         circles_green=detectcircle(green_hue_image)
#         print circles_green
#         if circles_green is not None:
#             for circles in circles_green[0]:
#                 [x_c,y_c,r]=circles    
#                 point= midpointcircledraw(x_c,y_c,(r+1))
#                 print point
#                 count=0
#                 for i in range(0,len(point)):
#                     x,y = point[i]
#                     print x,y
#                     color=(hsvimage[int(y),int(x)])
#                     if color[2]<= blackrange:
#                         count+=1
#                 print(count/float(len(point)))*100,color
#                 if (count/float(len(point)))*100 >= percentile:
#                     cv2.circle(org_image, (x_c, y_c), r, (0, 0, 255), 2)
#                     cv2.circle(org_image, (x_c, y_c), 1, (0, 255, 0), 1)
#                     cv2.putText(org_image,"green go",(int(x_c+10),int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  


#         out.write(org_image)
        
#         if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
#                 break

 

# # When everything done, release the video capture object
# cap.release()
# out.release()
 
# # Closes all the frames
# cv2.destroyAllWindows()
# # show the images
# #cv2.imshow("Detected red circles on the input image", org_image)
# #cv2.waitKey(0)



# new_file=('redcirclefileter.csv')

# f = open(new_file, "wt")
# writer=csv.writer(f)
# writer.writerow( ('circle_no','center_x','center_y','radious','point_r','point_r+1','point_r+2') )


def rectangle_per(hsvimage,x_c,y_c,r,flag):
   points=[]
   
   x_c=int(x_c)
   y_c=int(y_c)
   r=int(round(r))
   if flag==0:   
      ymin=y_c+r
      ymax=y_c+2*r+2
      xmin=x_c-r
      xmax=x_c+r
   if flag==1:
      ymin=y_c-r
      ymax=y_c+r
      xmin=x_c+r
      xmax=x_c+2*r
   if flag==2:
      ymin=y_c-2*r-2
      ymax=y_c-r
      xmin=x_c-r
      xmax=x_c+r
   if flag==3:
      ymin=y_c-r
      ymax=y_c+r
      xmin=x_c-2*r-2
      xmax=x_c-r
   for y in range(ymin, ymax+1):
      for x in range(xmin,xmax+1):
         points.append((x,y))
   color=[]
   count=0
   for i in range(0,len(points)):
      x,y=points[i]
      color=hsvimage[y,x]
      #if flag==2:
        # print x,y, color
      if color[2]<65:
         count +=1
   return (count/float(len(points)))*100

img = cv2.imread('sensor_video/frame/frame1505.jpg')
hsvimage=cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
red_hue_image=colordetection(hsvimage,0)
circles_red=detectcircle(red_hue_image)
if circles_red is not None:
   no_red_c=0
   for circles in circles_red[0]:
      no_red_c +=1
      [x_c,y_c,r]=circles
      bottom=rectangle_per(hsvimage,x_c,y_c,r,0)
      right=rectangle_per(hsvimage,x_c,y_c,r,1)
      upper=rectangle_per(hsvimage,x_c,y_c,r,2)
      left=rectangle_per(hsvimage,x_c,y_c,r,3)
      print bottom,right,upper,left
      if bottom > 70 or right > 70 or upper > 70 or left > 70:
         cv2.circle(img, (x_c, y_c), r, (0, 0, 255), 2)
         cv2.circle(img, (x_c, y_c), 1, (0, 255, 0), 1)

green_hue_image=colordetection(hsvimage,1)
circles_green=detectcircle(green_hue_image)

if circles_green is not None:
   for circles in circles_green[0]:
      [x_c,y_c,r]=circles
      bottom=rectangle_per(hsvimage,x_c,y_c,r,0)
      right=rectangle_per(hsvimage,x_c,y_c,r,1)
      upper=rectangle_per(hsvimage,x_c,y_c,r,2)
      left=rectangle_per(hsvimage,x_c,y_c,r,3)
      print bottom,right,upper,left
      if bottom > 70 or right > 70 or upper > 70 or left > 70:
         cv2.circle(img, (x_c, y_c), r, (0, 0, 255), 2)
         cv2.circle(img, (x_c, y_c), 1, (0, 255, 0), 1)

cv2.imshow("Detected red circles on the input image", img)
cv2.waitKey(0)







        # #for j in [1,1.5,2]:
#         point= midpointcircledraw(x_c,y_c,(r+1))
#         count=0
#         #color=[]
#         for i in range(0,len(point)):
#             x,y = point[i]
#             color=(hsvimage[int(y),int(x)])
#             #cv2.circle(img,(int(x),int(y)),0,(255,0,0),1)
#             writer.writerow( (no_red_c,x_c,y_c,r,color))        
#             # if color[2]<= blackrange:
#             #     count+=1
#             #     print(count/float(len(point)))*100,color[2]        
#             #     if (count/float(len(point)))*100 >= percentile:
        
#             #         cv2.circle(org_image, (x_c, y_c), r, (0, 0, 255), 2)
#             #         cv2.circle(org_image, (x_c, y_c), 1, (0, 255, 0), 1)
#             #         cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

  
# cv2.imshow('circles',img)
# cv2.waitKey(0)
# f.close()

# point= midpointcircledraw(825.5,325.5,5.5)
# for i in range(0,len(point)):
#    x,y = point[i]

#    #print x,y
#    color=(hsvimage[int(y),int(x)])

#    light=(hsl[int(y),int(x)])
#    print light
#    print color[2]
#    cv2.circle(img,(int(x),int(y)),1,(255,0,0),1)

  
# cv2.imshow('circles',img)
# cv2.waitKey(0)
