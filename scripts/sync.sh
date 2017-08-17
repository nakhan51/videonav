#!/bin/bash

python detector/sync.py "night_video/frametimestamp.csv" "night_video/sensortimestamp.csv" > night_video/sync.txt
