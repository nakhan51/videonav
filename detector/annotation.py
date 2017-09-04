import cv2
import csv
import numpy as np

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
annotation = False


new_file=('annotation_sunny.txt')

f = open(new_file, "wt")
header="frameno"+";"+"no_of_circles"+";"+"bounding_box_position"+";"+"color\n"
f.write(header)


def click_and_annotate(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
	    refPt = [(x, y)]
	    annotation = True
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
	    # record the ending (x, y) coordinates and indicate that
	    # the cropping operation is finished
	    refPt.append((x, y))
	    annotation = False
                   
	    # draw a rectangle around the region of interest
	    cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
	    cv2.imshow("image", image)



#image = cv2.imread('sensor_video/frame/frame15.jpg')
cap = cv2.VideoCapture("sunny_video/output_sunny.avi")

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

count=0
while(cap.isOpened()):
        overall_rec=[]
        ret, image = cap.read()
        if ret==False:
                break

        if (count % 20) ==0:
                clone = image.copy()
                cv2.namedWindow("image")
                cv2.setMouseCallback("image", click_and_annotate)
 
                # keep looping until the 'q' key is pressed
                while True:
	                # display the image and wait for a keypress
	                cv2.imshow("image", image)
	                key = cv2.waitKey(1) & 0xFF
 
	                # if the 'r' key is pressed, make flag red
	                if key == ord("r"):
	                        flag=0
            
                        # if the 'g' key is pressed, make flag green
	                elif key == ord("g"):
	                        flag=1
            
                        # if the 's' key is pressed, reset the coordinate
	                elif key == ord("s"):
	                        image = clone.copy()
 
	                # if the 'c' key is pressed, break from the loop
	                elif key == ord("c"):
                                overall_rec.append(refPt)
                        elif key == ord("n"):
                                break
 
                # if there are two reference points, then crop the region of interest
                # from teh image and display it
                no_circle=len(overall_rec)
                out_str=str(count)+";"+str(no_circle)+";\""+str(overall_rec)+"\";"+str(flag)+"\n"
                f.write(out_str)
        count +=1
# close all open windows
cap.release()
f.close()
cv2.destroyAllWindows()
