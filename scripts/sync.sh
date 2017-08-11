#!/bin/bash

python detector/sync.py "sunny_video/frametimestamp.csv" "sunny_video/sensortimestamp.csv" > sunny_video/sync.txt
