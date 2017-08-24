#!/bin/bash

#cat data/annotation.csv | awk -F, '{rects=$3; for (i=4; i<=NF-1; i++) {rects=rects","$i}} {print $1";"$2";"rects";"$NF}' | sed 's/(/[/g; s/)/]/g' > processeddata/annotation.txt

#cat data/finaldata.txt | sed 's/(/[/g; s/)/]/g' > processeddata/cropdata.txt

#cat data/datanocrop_black.txt | sed 's/(/[/g; s/)/]/g' > processeddata/notcrop.txt

#cat data/nocrop_nofilter.txt | sed 's/(/[/g; s/)/]/g' > processeddata/notcropandfilter.txt
#cat data/walk_crop_nofilter.txt | sed 's/(/[/g; s/)/]/g' > processeddata/walkcropnofil.txt





