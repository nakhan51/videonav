#!/bin/bash

gnuplot<<EOF

set terminal pdf font "Helvetica,12" lw 2
#set terminal pngcairo nocrop enhanced font "verdana,8" size 640,300


set boxwidth 0.9
set style fill solid 1.00 
set key above
 
set ylabel "Percentage"
#set xlabel "Hue"

set xtics nomirror rotate by 0
set style data histograms
set output "plots/bar_fn.pdf"

#set xtics (0,20,40,60,80,100,120,140,160,180) 

#plot [][]"plotdata/red_stat.txt" using 2 title "red" with histograms,\
#"plotdata/green_stat.txt" using 2 title "green" with histograms

plot [:][-1:]"fn.txt" using 2:xticlabel(1) title "w/o sensor w/o filter" with histograms,\
"" using 4 title "w/o sensor w/ filter" with histograms,\
"" using 3 title "w/ sensor w/o filter" with histograms,\
"" using 5 title "w/ sensor w/ filter" with histograms

EOF
