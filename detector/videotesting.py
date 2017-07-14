import numpy as np
import cv2


cap = cv2.VideoCapture('taylor1.MOV')

frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
#out = cv2.VideoWriter('output.avi',fourcc,10, (640,380))
out = cv2.VideoWriter('output.avi',fourcc,10, (frame_width,frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
