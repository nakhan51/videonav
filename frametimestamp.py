import numpy as np
import cv2
import csv
import sys

initialtime=int(sys.argv[1])
inputfile= sys.argv[2]
outputfile=sys.argv[3]
filename=sys.argv[4]

cap = cv2.VideoCapture(inputfile)

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=(cap.get(5))


fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter(outputfile,fourcc, round(frame_rate), (frame_width,frame_height))

new_file= filename 

f = open(new_file, "wt")
writer=csv.writer(f)
writer.writerow( ('frame_no','timestamp') )
count=0
timestamp= initialtime
print timestamp

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==False:
        break
    frame=cv2.flip(frame,-1)
    writer.writerow( (count,timestamp) )
    count +=1
    timestamp +=(1000/frame_rate)

    out.write(frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
f.close()
out.release
cv2.destroyAllWindows()
