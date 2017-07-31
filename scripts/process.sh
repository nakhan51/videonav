#!/bin/bash

# # generate plotdata for computation time for all frames
# cat finaldata.txt | awk -F\; '{print $1, $2*1000}' > plotdata/frame_time_cropped.txt
# cat data_no_crop_black_filter.txt | awk -F\; '{print $1, $2*1000}' > plotdata/frame_time_notcropped.txt


# cat finaldata.txt | awk -F\; '{print $2*1000}' | sort -n | scripts/cdf.sh > plotdata/cdf_time_cropped.txt
# cat data_no_crop_black_filter.txt | awk -F\; '{print $2*1000}' | sort -n | scripts/cdf.sh > plotdata/cdf_time_notcropped.txt

# plotdata for walkvideos
cat walk_video/finaldata.txt | awk -F\; 'NR>1 && NR<4230 {print $1, $2*1000}' > plotdata/walk_frame_time_cropped.txt
cat walk_video/nocrop_nofilter.txt | awk -F\; 'NR>1 && NR<4230 {print $1, $2*1000}' > plotdata/walk_frame_time_notcropped.txt

cat walk_video/finaldata.txt | awk -F\; 'NR>1 && NR<4230 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/walk_cdf_time_cropped.txt
cat walk_video/nocrop_nofilter.txt | awk -F\; 'NR>1 && NR<4230 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/walk_cdf_time_notcropped.txt
