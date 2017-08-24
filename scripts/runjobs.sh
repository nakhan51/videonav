#!/bin/bash

#types="night walk cloudy sunny sensor"
types="walk cloudy sunny sensor"

for type in $types; do
 	python detector/crop_nofilter.py ${type}_video/output_${type}.avi videos/${type}_crp_nofil.avi data/${type}_crp_nofil.txt ${type}_video/sync.txt
done

# for type in $types; do
# 	python detector/detectwithrecfilter.py ${type}_video/output_${type}.avi videos/${type}_nocrp_recfil.avi data/${type}_nocrp_recfil.txt
# done

#python detector/detectwithrecfilter.py cloudy_video/output_cloudy.avi videos/cloudy_nocrp_recfil.avi data/cloudy_nocrp_recfil.txt
