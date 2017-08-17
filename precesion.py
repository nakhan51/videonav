import numpy as np
import cv2

with open('data/pos_neg_crop.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

redfp=0
redtp=0
greentp=0
greenfp=0
redfn=0
greenfn=0
totalframe=1
posframe=0
i=1
for row in lines[1:]:
    cols= row.split(';')    
    
    redtp += float(cols[2])
    greentp += float(cols[3])

    redfp += float(cols[4])
    greenfp += float(cols[5])

    redfn +=float(cols[6])
    greenfn +=float(cols[7])
    
    
    i +=1
    totalframe = i

print redtp,greentp,redfp,greenfp,redfn,greenfn
    
