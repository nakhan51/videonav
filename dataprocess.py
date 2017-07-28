import numpy as np
import cv2
import json

annote_dic={}
notcrop_dic={}


def checkbound(boxes,red_pos,green_pos,red_count,green_count,color):
    no_box=len(boxes)
    
    if (no_box > 0 and (red_count==0 and green_count==0)):
        return False
    if (color == 0 and green_count > 0):
        return False
    if (color ==1 and red_count > 0):
        return False

    
    if red_count > 0:
        count=0
        for cir in red_pos:
            xc,yc=cir   
            for box in boxes:
                [x1,y1],[x2,y2]=box
                if xc > x1 and xc < x2 and yc > y1 and yc < y2:
                    count +=1
        if count == 0:
            return False

    if green_count > 0:
        count=0
        for cir in green_pos:
            xc,yc=cir   
            for box in boxes:
                [x1,y1],[x2,y2]=box
                if xc > x1 and xc < x2 and yc > y1 and yc < y2:
                    count +=1
        if count == 0:
            return False
        
    return True
    
    
with open('data/annotation.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frameno, circle_count, boxes, color=int(cols[0]), int(cols[1]), cols[2], int(cols[3])
    boxes=json.loads(boxes.decode('string-escape').strip('"'))
    annote_dic[frameno]=(circle_count, boxes, color)


#for k in annote_dic.keys():
#    print k, annote_dic[k]

with open('data/notcrop.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frame_no, red_count,green_count,red_pos,green_pos=int(cols[0]), int(cols[2]), int(cols[3]), (cols[4]), (cols[5])
    red_pos=json.loads(red_pos.decode('string-escape').strip('"'))
    green_pos=json.loads(green_pos.decode('string-escape').strip('"'))
    notcrop_dic[frame_no]=(red_count,green_count,red_pos,green_pos)

for k in notcrop_dic.keys():
    (red_count,green_count,red_pos,green_pos)=notcrop_dic[k]
    (circle_count, boxes, color)=annote_dic[k]
    
    if not k in annote_dic or len(boxes)==0:
        continue
    
    

    ret=checkbound(boxes,red_pos,green_pos,red_count,green_count,color)

    print k, ret 
    

    
