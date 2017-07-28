import numpy as np
import cv2
import json

annote_dic={}

with open('data/annotation.txt') as f:
    lines=f.readlines()
lines=[x.strip('\n\r')for x in lines]

for row in lines[1:]:
    cols= row.split(';')
    frameno, circle_count, boxes, color=int(cols[0]), int(cols[1]), cols[2], int(cols[3])
    boxes_l=json.loads(boxes)
    #print boxes_l
    annote_dic[frameno]=(circle_count, boxes_l, color)


for k in annote_dic.keys():
    print k, annote_dic[k]
