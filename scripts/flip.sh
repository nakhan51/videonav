#!/bin/bash

val=`cat night_video/rectime.csv| awk -F ',' 'NR>1 {print $2}'`
echo $val
 python detector/frametimestamp.py $val "night_video/video_night.mp4" "night_video/output_night.avi" "night_video/frametimestamp.csv"
