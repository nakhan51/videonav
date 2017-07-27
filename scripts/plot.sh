#!/bin/bash

#scatter plot and cdf of time w/ and w/o sensor data

gnuplot<<EOF

set terminal pdf font "Helvetica,12" lw 2

set xlabel "Frame"
set ylabel "Time (ms)"

# scatter plot
set output "plots/frame_time.pdf"
plot \
'plotdata/frame_time_cropped.txt' u 1:2 ti "w/ sensor", \
'plotdata/frame_time_notcropped.txt' u 1:2 ti "w/o sensor"

# cdf
set xlabel "Time (ms)"
set ylabel "CDF"
 
set output "plots/cdf_time.pdf"
plot [:300][:] \
'plotdata/cdf_time_cropped.txt' u 2:1 w lines ti "w/ sensor", \
'plotdata/cdf_time_notcropped.txt' u 2:1 w lines ti "w/o sensor"


EOF
