import numpy as np
import cv2
import sys

def interpolator(upper,lower,sensortime,presensortime,frametime):
    slope=(upper-lower)/(sensortime-presensortime)
    sensor_new= lower+slope*(frametime-presensortime)
    return sensor_new 

datafile1=sys.argv[1]
datafile2=sys.argv[2]

with open(datafile1) as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

frameno=[]
frametimestamp=[]
sensortimestamp=[]
pitch=[]
roll=[]
yaw=[]

for row in lines[1:]:
    columns= row.split(',')
    #columns=[int(columns[0]),int(columns[1])]
    frameno.append(int(columns[0]))
    frametimestamp.append(float(columns[1]))
    

with open(datafile2) as g:
    lines=g.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    columns= row.split(',')
    
    sensortimestamp.append(int(columns[5]))
    pitch.append(float(columns[13]))
    roll.append(float(columns[14]))
    yaw.append(float(columns[15]))

#print pitch[1]-pitch[2]


for i in range(0,len(frametimestamp)):
    frametime=frametimestamp[i]
    j=0
    flag=True
    while(flag):
        sensortime=sensortimestamp[j]
        #print sensortime,frametime
        if sensortime > frametime:
            if (j-1)<0:
                pitch_new=pitch[j]
                roll_new=roll[j]
                azimuth_new=yaw[j]
                flag=False
            else:
                u_pitch=pitch[j]
                l_pitch=pitch[j-1]
                u_roll=roll[j]
                l_roll=roll[j-1]
                u_yaw=yaw[j]
                l_yaw=yaw[j-1]
                presensortime=sensortimestamp[j-1]
                pitch_new=interpolator(u_pitch,l_pitch,sensortime,presensortime,frametime)
                roll_new=interpolator(u_roll,l_roll,sensortime,presensortime,frametime)
                azimuth_new=interpolator(u_yaw,l_yaw,sensortime,presensortime,frametime)
                flag=False
        
        j+=1
    
    print frameno[i],frametimestamp[i],pitch_new,roll_new,azimuth_new,frametime
    
    i+=1
            
f.close()
g.close()


