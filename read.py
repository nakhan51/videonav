import numpy as np
import cv2


new_file= "log/annotation.csv" 
f = open(new_file, "r")
lines=f.readlines()
lines=[x.strip('\n')for x in lines]
pitch=[]
roll=[]
azimuth=[]

for row in lines[1:]:
    columns= row.split(',')
    pitch.append(float(columns[0]))
    roll.append(float(columns[1]))
    azimuth.append((columns[2]))
print azimuth[0]
