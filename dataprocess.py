import numpy as np
import cv2
import json

annote_dic={}
notcrop_dic={}
crop_dic={}
nocrp_nofil_dic={}

def checkbound(boxes,cir_pos,ann_clr,det_clr,ann_cir_cnt):
    no_box=len(boxes)
    no_cir=len(cir_pos)
    FN=0
    
    if (no_box > 0 and no_cir == 0):
        FN +=1

    
    if no_cir > 0:
        truecount=0
        notinbox=0
        for cir in cir_pos:
            xc,yc=cir   
            for box in boxes:
                [x1,y1],[x2,y2]=box
                if xc > x1 and xc < x2 and yc > y1 and yc < y2:
                    truecount +=1
            if truecount==0:
                notinbox +=1
        TP=truecount
        FP=notinbox
        
        FN +=(no_cir-TP-FP)
        
    return TP,FP,FN
    
    
with open('data/annotation.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frameno, circle_count, boxes, color=int(cols[0]), int(cols[1]), cols[2], int(cols[3])
    boxes=json.loads(boxes.decode('string-escape').strip('"'))
    annote_dic[frameno]=(circle_count, boxes, color)


with open('data/notcrop.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frame_no, red_count,green_count,red_pos,green_pos=int(cols[0]), int(cols[2]), int(cols[3]), (cols[4]), (cols[5])
    red_pos=json.loads(red_pos.decode('string-escape').strip('"'))
    green_pos=json.loads(green_pos.decode('string-escape').strip('"'))
    notcrop_dic[frame_no]=(red_count,green_count,red_pos,green_pos)


with open('data/cropdata.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    crp_frameno, crp_cir_pos,crp_cir_color=int(cols[0]), (cols[2]), (cols[3])
    crp_cir_pos=json.loads(crp_cir_pos.decode('string-escape').strip('"'))
    crp_cir_color=json.loads(crp_cir_color.decode('string-escape').strip('"'))
    crop_dic[crp_frameno]=(crp_cir_pos,crp_cir_color)

    
for k in crop_dic.keys():
    (crp_cir_pos,crp_cir_color)=crop_dic[k]
    if not k in annote_dic:
        continue
    (circle_count, boxes, color)=annote_dic[k]
    
    if len(boxes)==0:
        continue
    
    TP,FP,FN=checkbound(boxes,crp_cir_pos,color,crp_cir_color,circle_count)

    print circle_count, k, TP, FP, FN
    

    
