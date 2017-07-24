import numpy as np
import cv2
import csv
import sys

inputvideo= sys.argv[1]
outputvideo=sys.argv[2]
datafile=sys.argv[3]

cap = cv2.VideoCapture(inputvideo)

# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate=int(cap.get(cv2.cv.CV_CAP_PROP_FPS ))
#print frame_rate

fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
out = cv2.VideoWriter(outputvideo,fourcc, frame_rate, (frame_width,frame_height))

new_file= datafile 
f = open(new_file, "r")
lines=f.readlines()
lines=[x.strip('\n')for x in lines]
pitch=[]
roll=[]
azimuth=[]

for row in lines:
    columns= row.split(' ')
    pitch.append(format(float(columns[2]),'.2f'))
    roll.append(format(float(columns[3]),'.2f'))
    azimuth.append(format(float(columns[4]),'.2f'))
#print pitch,roll,azimuth

count=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==False:
        break

    text1="Pitch: "+str(pitch[count])
    text2="Roll: "+str(roll[count])
    text3="Azimuth: "+str( azimuth[count])
    cv2.putText(frame,text1,(1600,800),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0), 5)
    cv2.putText(frame,text2,(1600,850),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0), 5)
    cv2.putText(frame,text3,(1600,900),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0), 5)

    out.write(frame)
    count +=1
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
f.close()
out.release
cv2.destroyAllWindows()
