#!/bin/bash

#scatter plot and cdf of time w/ and w/o sensor data

gnuplot<<EOF

set terminal pdf font "Helvetica,12" lw 2
set key above

#set xlabel "Area"
#set ylabel "Time (ms)"

# scatter plot
#set output "plots/cloudy_recarea.pdf"
#plot [:1200000][] \
#'plotdata/cloudy_recarea.txt' u 2:1 lw 0.001 ti "" 


# cdf
set xlabel "Time (ms)"
set ylabel "CDF"
 

#set style line 3 lt 3
#set style line 4 lt 4

set output "plots/lisacdf.pdf"
plot [:][:] \
'plotdata/lisaday1_cdf.txt' u 2:1 w lines ti "w/o cropping (day)",\
'plotdata/lisaday1_crop_cdf.txt' u 2:1 w lines ti "w/ cropping (day)",\
'plotdata/lisanight1_cdf.txt' u 2:1 w lines dt 5 ti "w/o cropping (night)",\
'plotdata/lisanight1_crop_cdf.txt' u 2:1 w lines dt 5 ti "w/ cropping (night)"

#'plotdata/walk_cdf_nocrop_nofil.txt' u 2:1 w lines ti "w/o sensor w/o filter",\
#'plotdata/walk_cdf_nocrop_black.txt' u 2:1 w lines ti "w/o sensor w/ filter",\
#'plotdata/walk_cdf_crop_nofil.txt' u 2:1 w lines ti "w/ sensor w/o filter",\
#'plotdata/walk_cdf_crop_black.txt' u 2:1 w lines ti "w/ sensor w/ filter"




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
