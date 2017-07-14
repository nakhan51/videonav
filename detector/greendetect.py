import cv2
import numpy as np

#vidcap = cv2.VideoCapture('taylor1.MOV')
#success,image = vidcap.read()
#count = 0
#success = True
#while success:
  #success,image = vidcap.read()
  #print 'Read a new frame: ', success
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  #count += 1#

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('taylor1.MOV')

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))



# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter('output.avi',fourcc, 10, (frame_width,frame_height))

# Read until video is completed
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, org_image = cap.read()
	if ret == False:
		break
        image=cv2.medianBlur(org_image,3)
        hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV);# Convert input image to HSV
        
        
        #Threshold the HSV image, keep only the red pixels
        green_hue_image=cv2.inRange(hsvimage, np.array((50, 100, 100),dtype = "uint8"), np.array((95, 255, 255),dtype = "uint8"));
        #upper_red_hue_range=cv2.inRange(hsvimage, np.array((160, 100, 100),dtype = "uint8"), np.array((179, 255, 255),dtype = "uint8"));
        
        #Combine the above two images
        #red_hue_image=cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0);
        green_hue_image=cv2.GaussianBlur(green_hue_image, (9, 9), 2, 2);

        # Use the Hough transform to detect circles in the combined threshold image
        circles=cv2.HoughCircles(green_hue_image, cv2.cv.CV_HOUGH_GRADIENT, 1, green_hue_image.shape[0]/4,np.array([]),200, 12,2,5)
        
        
        if circles is not None:
                a, b, c = circles.shape
                for i in range(b):
                        cv2.circle(org_image, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (255, 0, 0), 3)
                        cv2.circle(org_image, (circles[0][i][0], circles[0][i][1]), 2, (255, 0, 0), 3)  

        # Write the frame into the file 'output.avi'
        out.write(org_image)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):# Press Q on keyboard to  exit
                break

        # out.write(image)
        # Display the resulting frame
        #cv2.imshow('Frame',image)

# Press Q on keyboard to  exit
#if cv2.waitKey(25) & 0xFF == ord('q'):
       # break 

# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

