import cv2
import numpy as np
import time

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('output_crop.avi')

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(round(cap.get(cv2.cv.CV_CAP_PROP_FPS)))


# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter('output_crop_detect.avi',fourcc, 20, (frame_width,frame_height))

# Read until video is completed
while(cap.isOpened()):
        start_frame= time.time()
	# Capture frame-by-frame
	ret, org_image = cap.read()
	if ret == False:
		break

        start_madian=time.time()
        image=cv2.medianBlur(org_image,3)
        time_median=time.time()-start_madian

        start_hsv=time.time()
        hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV
        time_hsv=time.time()-start_hsv
        
        
        #Threshold the HSV image, keep only the red pixels
        start_range=time.time()
        lower_red_hue_range=cv2.inRange(hsvimage, np.array((0, 100, 100),dtype = "uint8"), np.array((10, 255, 255),dtype = "uint8"));
        time_range_red=time.time()-start_range
        
        upper_red_hue_range=cv2.inRange(hsvimage, np.array((160, 100, 100),dtype = "uint8"), np.array((179, 255, 255),dtype = "uint8"));
        
        #Combine the above two images
        start_weighted=time.time()
        red_hue_image=cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0);
        time_weighted_red=time.time()-start_weighted
        
        red_hue_image=cv2.GaussianBlur(red_hue_image, (9, 9), 2, 2);

        # Use the Hough transform to detect circles in the combined threshold image
        start_circle=time.time()
        circles_red=cv2.HoughCircles(red_hue_image, cv2.cv.CV_HOUGH_GRADIENT, 1, red_hue_image.shape[0]/4,np.array([]),200, 12,2,4)
        time_circle_red=time.time()-start_circle
        
        
        if circles_red is not None:
                a, b, c = circles_red.shape
                for i in range(b):
                        cv2.circle(org_image, (circles_red[0][i][0], circles_red[0][i][1]), circles_red[0][i][2], (0, 0, 255), 1)
                        cv2.circle(org_image, (circles_red[0][i][0], circles_red[0][i][1]), 2, (0, 255, 0), 1)

        #Threshold the HSV image, keep only the green pixels
        green_hue_image=cv2.inRange(hsvimage, np.array((50, 100, 100),dtype = "uint8"), np.array((95, 255, 255),dtype = "uint8"));
        
        #Combine the above two images
        green_hue_image=cv2.GaussianBlur(green_hue_image, (9, 9), 2, 2);

        # Use the Hough transform to detect circles in the combined threshold image
        circles_green=cv2.HoughCircles(green_hue_image, cv2.cv.CV_HOUGH_GRADIENT, 1, green_hue_image.shape[0]/4,np.array([]),200, 12,2,5)
        
        
        if circles_green is not None:
                a, b, c = circles_green.shape
                for i in range(b):
                        cv2.circle(org_image, (circles_green[0][i][0], circles_green[0][i][1]), circles_green[0][i][2], (255, 0, 0), 2)
                        cv2.circle(org_image, (circles_green[0][i][0], circles_green[0][i][1]), 1, (255, 0, 0), 1)
        time_frame=time.time()-start_frame
                        
        print time_frame,time_median,time_hsv,time_range_red,time_weighted_red,time_circle_red
        # Write the frame into the file 'output.avi'
        out.write(org_image)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
                break

 

# When everything done, release the video capture object
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()

