import numpy as np
import cv2
import json
import sys

annotationfile=sys.argv[1]
inputfile=sys.argv[2]
outputfile=sys.argv[3]
annote_dic={}
rec_dic={}


def checkbound(boxes,cir_pos,ann_clr,det_clr,ann_cir_cnt):
    no_box=len(boxes)
    no_cir=len(cir_pos)
    FN=0
    TP=0
    FP=0
    red_tp=0
    red_fp=0
    red_fn=0
    green_tp=0
    green_fp=0
    green_fn=0
    rfp_con=0
    gfp_con=0
    
    if (no_box > 0 and no_cir == 0):
        FN +=1
        Frame= False
        if ann_clr == 0:
            red_fn +=ann_cir_cnt
        if ann_clr == 1:
            green_fn +=ann_cir_cnt
            
    
    if no_cir > 0:
        truecount=0
        notinbox=0
        rcnt_tp=0
        gcnt_tp=0
        rcnt_fp=0
        gcnt_fp=0
        gcon_fp=0
        rcon_fp=0
        
        i=0
        for cir in cir_pos:
            xc,yc=cir   
            for box in boxes:
                [x1,y1],[x2,y2]=box
                if xc >= x1 and xc <= x2 and yc >= y1 and yc <= y2:
                    truecount +=1
                    if det_clr[i]==0:
                        if ann_clr == det_clr[i]:
                            rcnt_tp +=1
                        else:
                            gcon_fp +=1
                    if det_clr[i]==1:
                        if ann_clr == det_clr[i]:
                            gcnt_tp +=1
                        else:
                            rcon_fp +=1
            if truecount==0:
                notinbox +=1
                if det_clr[i]==0:
                    rcnt_fp +=1
                if det_clr[i]==1:
                    gcnt_fp +=1
            i +=1

        TP=truecount
        FP=notinbox
        red_tp=rcnt_tp
        red_fp=rcnt_fp
        green_tp=gcnt_tp
        green_fp=gcnt_fp
        rfp_con=rcon_fp
        gfp_con=gcon_fp
        if TP > 0:
            Frame= True
        else:
            Frame= False
        
        
    return red_tp, green_tp, red_fp, green_fp, red_fn, green_fn, Frame, rfp_con, gfp_con
    
## Annotation    
with open(annotationfile) as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frameno, circle_count, boxes, color=int(cols[0]), int(cols[1]), cols[2], int(cols[3])
    boxes=json.loads(boxes.decode('string-escape').strip('"'))
    annote_dic[frameno]=(circle_count, boxes, color)


    
## nocrop nofil
with open(inputfile) as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frame_no, rec_pos,rec_clr=int(cols[0]), (cols[3]), (cols[4])
    rec_pos=json.loads(rec_pos.decode('string-escape').strip('"'))
    rec_clr=json.loads(rec_clr.decode('string-escape').strip('"'))
    rec_dic[frame_no]=(rec_pos,rec_clr)


    
write_file=(outputfile)
g = open(write_file, "wt")
header="ann_cir"+";"+"frameno"+";"+"red_tp"+";"+"green_tp"+";"+"red_fp"+";"+"green_fp"+";"+"red_fn"+";"+"green_fn"+";"+"Frame"+";"+"rfp_con"+";"+"gfp_con"+";"+"color\n"
g.write(header)    

## main
for k in rec_dic.keys():
    (cir_pos,cir_color)=rec_dic[k]
    if not k in annote_dic:
        continue
    (circle_count, boxes, color)=annote_dic[k]
    
    if len(boxes)==0:
        continue
    
    red_tp, green_tp, red_fp, green_fp, red_fn, green_fn, Frame, rfp_con, gfp_con=checkbound(boxes,cir_pos,color,cir_color,circle_count)
    
    out_str=str(circle_count)+";"+str(k)+";"+str(red_tp)+";"+str(green_tp)+";"+str(red_fp)+";"+str(green_fp)+";"+str(red_fn)+";"+str(green_fn)+";"+str(Frame)+";"+str(rfp_con)+";"+str(gfp_con)+";"+str(color)+"\n"
    g.write(out_str)


g.close()
f.close()
# Closes all the frames
cv2.destroyAllWindows()
    

    
