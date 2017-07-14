import cv2
import numpy as np

cap = cv2.VideoCapture('taylor1.MOV')

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
frame_rate=int(round(cap.get(cv2.cv.CV_CAP_PROP_FPS)))
print frame_rate, frame_height, frame_width

# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out=cv2.VideoWriter('output_crop.avi',fourcc, frame_rate , (frame_width/2,frame_height/2))

#Read until video is completed
while(cap.isOpened()):
    #Capture frame-by-frame
    ret, org_image = cap.read()
    if ret == False:
            break

    #(h,w)=org_image.shape[:2]
    crop_image=org_image[0:frame_height/2, 0:frame_width/2]
    #cv2.imshow("cropimage",crop_image)
    #cv2.waitKey(0)
    #Write the frame into the file 'output.avi'

    #out.write(org_image)
    out.write(crop_image)

    if cv2.waitKey(25) & 0xFF == ord('q'):#Press Q on keyboard to  exit
        break

#When everything done, release the video capture object
cap.release()
out.release() 
#Closes all the frames
cv2.destroyAllWindows()


# image=cv2.imread("frame181.jpg")
# cv2.imshow("org_image", image)
# cv2.waitKey(0)

# print image.shape
# (h,w)=image.shape[:2]
# print h, w 
# crop_image=image[0:h/2, 0:w/2]
# cv2.imshow("cropped",crop_image)
# cv2.waitKey(0)
# (h1,w1)=crop_image.shape[:2]
# print h1, w1 

