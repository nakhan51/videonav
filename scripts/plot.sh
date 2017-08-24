#!/bin/bash

#scatter plot and cdf of time w/ and w/o sensor data

gnuplot<<EOF

set terminal pdf font "Helvetica,12" lw 2
set key above

set xlabel "Area"
set ylabel "Time (ms)"

# scatter plot
set output "plots/cloudy_recarea.pdf"
plot [:1200000][] \
'plotdata/cloudy_recarea.txt' u 2:1 lw 0.001 ti "" 
#'plotdata/walk_frame_time_notcropped.txt' u 1:2 lw 1 ti "w/o sensor"

# cdf
#set xlabel "Time (ms)"
#set ylabel "CDF"
 
#set output "plots/lisanight1_cdf.pdf"
#plot [:][:] \
#'plotdata/lisanight1_cdf.txt' u 2:1 w lines ti "w/o cropping",\
#'plotdata/lisanight1_crop_cdf.txt' u 2:1 w lines ti "w/ cropping"


## rec-time
#set xlabel "Area(pixel)"
#set ylabel "Time(ms)"

#set output "plots/recarea_time.pdf"
#plot \
#'plotdata/recarea.txt' u 2:1 ti "rec area vs frametime"
 

#set output "plots/sunny_cdf_filter.pdf"
#plot [:10][:] \
#'plotdata/sunny_cdf_filter.txt' u 2:1 w lines ti ""


#set output "plots/red.pdf"
#plot \
#'plotdata/red.txt' u 1:2,\
#'plotdata/green.txt' u 1:2 



EOF
