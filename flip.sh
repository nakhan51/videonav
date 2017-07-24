#!/bin/bash

val=`cat sensor_video/rectime.csv| awk -F ',' 'NR>1 {print $2}'`
echo $val
 python frametimestamp.py $val "sensor_video/video_sensor.mp4" "sensor_video/output_sensor.avi" "sensor_video/frametimestamp.csv"
