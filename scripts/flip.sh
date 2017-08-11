#!/bin/bash

val=`cat sunny_video/rectime.csv| awk -F ',' 'NR>1 {print $2}'`
echo $val
 python detector/frametimestamp.py $val "sunny_video/video_sunny.mp4" "sunny_video/output_sunny.avi" "sunny_video/frametimestamp.csv"
