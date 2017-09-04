#!/bin/bash

#cat data/annotation.csv | awk -F, '{rects=$3; for (i=4; i<=NF-1; i++) {rects=rects","$i}} {print $1";"$2";"rects";"$NF}' | sed 's/(/[/g; s/)/]/g' > processeddata/annotation.txt

#cat data/sensor_nocrp_nofil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/sensor_nocrp_nofil.txt
#cat data/sensor_nocrp_recfil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/sensor_nocrp_fil.txt
#cat data/sensor_crp_nofil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/sensor_crp_nofil.txt
#cat data/sensor_crp_recfil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/sensor_crp_fil.txt

#cat data/cloudy_nocrp_nofil_12.txt | sed 's/(/[/g; s/)/]/g' > processeddata/cloudy_nocrp_nofil_12.txt
#cat data/cloudy_nocrp_recfil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/cloudy_nocrp_fil.txt
#cat data/cloudy_crp_nofil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/cloudy_crp_nofil.txt
#cat data/cloudy_crp_recfil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/cloudy_crp_fil.txt
#cat data/annotation_cloudy.txt | sed 's/(/[/g; s/)/]/g' > processeddata/cloudy_annotation.txt

cat data/walk_nocrp_nofil_12.txt | sed 's/(/[/g; s/)/]/g' > processeddata/walk_nocrp_nofil.txt
cat data/walk_nocrp_recfil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/walk_nocrp_fil.txt
cat data/walk_crp_nofil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/walk_crp_nofil.txt
cat data/walk_crp_recfil.txt | sed 's/(/[/g; s/)/]/g' > processeddata/walk_crp_fil.txt
cat data/annotation_walk.txt | sed 's/(/[/g; s/)/]/g' > processeddata/walk_annotation.txt



