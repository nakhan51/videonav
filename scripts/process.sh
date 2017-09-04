#!/bin/bash

# # generate plotdata for computation time for Lisa 
#cat data/night2.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/night2_cdf.txt
#cat data/lisanight1_crop.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/lisanight1_crop_cdf.txt

# plotdata for walkvideos

# cat data/walk_crop_black.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/walk_cdf_crop_black.txt
# cat data/walk_crop_nofilter.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/walk_cdf_crop_nofil.txt
# cat data/walk_datanocrop_black.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/walk_cdf_nocrop_black.txt
# cat data/walk_nocrop_nofilter.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/walk_cdf_nocrop_nofil.txt
#cat data/walk_crop_nofilter.txt | awk -F\; 'NR>1 {print$2*1000, $3}' |sed 's/"/;/g'|awk -F\; '{print $1, $2}' |sort -n > plotdata/walk_recarea.txt

# sunny data
#cat data/sunny_nocrop_nofilter.txt | awk -F\; 'NR>1 {print $3*1000}'| sort -n |scripts/cdf.sh > plotdata/sunny_cdf_clrfil.txt
#cat data/sunny_nocrop_nofilter.txt | awk -F\; 'NR>1 {print $4*1000}'| sort -n |scripts/cdf.sh > plotdata/sunny_cdf_cirdet.txt

#cat data/sunny_nocrop_black.txt | awk -F\; 'NR>1 && $3!=-1 {print $3*1000}'| sort -n |scripts/cdf.sh > plotdata/sunny_cdf_filter.txt

#cat data/sunny_crop_nofilter2.txt | awk -F\; 'NR>1 {print$2*1000, $3}' |sed 's/"/;/g'|awk -F\; '{print $1, $2}' |sort -n > plotdata/sunny_recarea.txt

#cat data/sunny_crop_nofilter2.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sunny_cdf_crop_nofil.txt
#cat data/sunny_nocrop_black.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sunny_cdf_nocrop_black.txt
#cat data/sunny_nocrop_nofilter.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sunny_cdf_nocrop_nofil.txt

### sensor dataset
#cat data/sensor_nocrp_nofil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sensor_cdf_nocrp_nofil.txt
#cat data/sensor_nocrp_recfil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sensor_cdf_nocrp_recfil.txt
#cat data/sensor_crp_nofil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sensor_cdf_crp_nofil.txt
#cat data/sensor_crp_recfil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/sensor_cdf_crp_recfil.txt

## cloudy
cat data/cloudy_nocrp_nofil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/cloudy_cdf_nocrp_nofil.txt
cat data/cloudy_nocrp_recfil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/cloudy_cdf_nocrp_recfil.txt
cat data/cloudy_crp_nofil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/cloudy_cdf_crp_nofil.txt
cat data/cloudy_crp_recfil.txt | awk -F\; 'NR>1 {print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/cloudy_cdf_crp_recfil.txt


### color filter time
# cat noclrfil.txt | awk -F' ' '{print $1*1000}'| sort -n |scripts/cdf.sh > plotdata/cdf_noclrfil_full.txt
# cat clrfil.txt | awk -F' ' '{print $1*1000}'| sort -n |scripts/cdf.sh > plotdata/cdf_clrfil_full.txt
# cat noclrfil.txt | awk -F' ' '{print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/cdf_noclrfil_cir.txt
# cat clrfil.txt | awk -F' ' '{print $2*1000}'| sort -n |scripts/cdf.sh > plotdata/cdf_clrfil_cir.txt



