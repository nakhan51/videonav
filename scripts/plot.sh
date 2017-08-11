#!/bin/bash

#scatter plot and cdf of time w/ and w/o sensor data

gnuplot<<EOF

set terminal pdf font "Helvetica,12" lw 2
set key above

#set xlabel "Area"
#set ylabel "Time (ms)"

# scatter plot
#set output "plots/sunny_recarea.pdf"
#plot [:1200000][] \
#'plotdata/sunny_recarea.txt' u 2:1 lw 0.001 ti "" 
#'plotdata/walk_frame_time_notcropped.txt' u 1:2 lw 1 ti "w/o sensor"

# cdf
#set xlabel "Time (ms)"
#set ylabel "CDF"
 
#set output "plots/sunny_cdf_time.pdf"
#plot [:200][:] \
#'plotdata/sunny_cdf_nocrop_nofil.txt' u 2:1 w lines ti "w/o sensor w/o filter", \
#'plotdata/sunny_cdf_nocrop_black.txt' u 2:1 w lines ti "w/o sensor w/filter",\
#'plotdata/sunny_cdf_crop_nofil.txt' u 2:1 w lines ti "w/ sensor w/o filter"
#'plotdata/walk_cdf_crop_black.txt' u 2:1 w lines ti "w/ sensor w/filter"

## rec-time
#set xlabel "Area(pixel)"
#set ylabel "Time(ms)"

#set output "plots/recarea_time.pdf"
#plot \
#'plotdata/recarea.txt' u 2:1 ti "rec area vs frametime"


# cdf for color filter
set xlabel "Time (ms)"
set ylabel "CDF"
 
# set output "plots/sunny_cdf_clrfil.pdf"
# plot [:100][:] \
# 'plotdata/sunny_cdf_clrfil.txt' u 2:1 w lines ti "processing time for color filtering"

# set output "plots/sunny_cdf_cirdet.pdf"
# plot [:][:] \
# 'plotdata/sunny_cdf_cirdet.txt' u 2:1 w lines ti "processing time for circle detection"

#set output "plots/sunny_cdf_filter.pdf"
#plot [:10][:] \
#'plotdata/sunny_cdf_filter.txt' u 2:1 w lines ti ""

#set output "plots/cdf_clrfil_full.pdf"
#plot [:3000][:] \
#'plotdata/cdf_noclrfil_full.txt' u 2:1 w lines ti "w/o color filtering",\
#'plotdata/cdf_clrfil_full.txt' u 2:1 w lines ti "w/ color filtering"

set output "plots/red.pdf"
plot \
'red.txt' u 1:2 



EOF
