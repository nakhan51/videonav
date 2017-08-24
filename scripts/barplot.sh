#!/bin/bash

gnuplot<<EOF

set terminal pdf font "Helvetica,12" lw 2
#set terminal pngcairo nocrop enhanced font "verdana,8" size 640,300


set boxwidth 1
set style fill solid 1.00 
set key above
 
set ylabel "Value"
set xlabel "Hue"

set xtics nomirror rotate by -45
set style data histograms
set output "plots/stat_light.pdf"

set xtics (0,20,40,60,80,100,120,140,160,180) 

plot [][]"plotdata/red_stat.txt" using 2 title "red" with histograms,\
"plotdata/green_stat.txt" using 2 title "green" with histograms
EOF
