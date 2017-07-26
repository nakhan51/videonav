#!/bin/bash

python detector/sync.py "sensor_video/frametimestamp.csv" "sensor_video/sensortimestamp.csv" > sensor_video/sync.txt
