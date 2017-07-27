#!/bin/bash

# generate plotdata for computation time for all frames
cat finaldata.txt | awk -F\; '{print $1, $2*1000}' > plotdata/frame_time_cropped.txt
cat data_no_crop_black_filter.txt | awk -F\; '{print $1, $2*1000}' > plotdata/frame_time_notcropped.txt


cat finaldata.txt | awk -F\; '{print $2*1000}' | sort -n | scripts/cdf.sh > plotdata/cdf_time_cropped.txt
cat data_no_crop_black_filter.txt | awk -F\; '{print $2*1000}' | sort -n | scripts/cdf.sh > plotdata/cdf_time_notcropped.txt

