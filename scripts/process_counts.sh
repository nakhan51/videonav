#!/bin/bash
##nocrop_nofil

types="sensor"
sens="nocrp crp"
filter="nofil"

for type in $types; do
	for i in $sens; do
		for j in $filter; do

			total=`cat data/${type}_pos_neg_${i}_${j}.txt |awk -F\; 'NR>1 {print}'| wc -l`
			total_ann=`cat data/${type}_pos_neg_${i}_${j}.txt |awk -F\; 'NR>1 {sum +=$1} END {print sum}'`
			total_r=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 {print}' |wc -l`
			red_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 {sum +=$1} END {print sum}'`
			total_g=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 {print}' | wc -l`
			green_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 {sum +=$1} END {print sum}'`
			
			rfp_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {print}' | wc -l`
			rfp_no=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {sum +=$1} END {print sum}'`
			
			gfp_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {print}' | wc -l`
			gfp_no=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {sum +=$1} END {print sum}'`
			
			rtp_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {print}' | wc -l`
			rtp_no=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {sum +=$1} END {print sum}'`
			
			gtp_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {print}' | wc -l`
			gtp_no=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {sum +=$1} END {print sum}'`
			
			rfn_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {print}' | wc -l`
			rfn_no=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {sum +=$1} END {print sum}'`
			
			gfn_count=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {print}' | wc -l`
			gfn_no=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {sum +=$1} END {print sum}'`
			
			frame_pos=`cat data/${type}_pos_neg_${i}_${j}.txt | awk -F\; 'NR>1 && $9=="True" {print}' | wc -l`

			rtp_percent=`echo $rtp_count $total_r | awk '{print ($1/$2)*100}'`
			rfp_percent=`echo $rfp_count $total_r | awk '{print ($1/$2)*100}'`
			rfn_percent=`echo $rfn_count $total_r | awk '{print ($1/$2)*100}'`
			gtp_percent=`echo $gtp_count $total_g | awk '{print ($1/$2)*100}'`
			gfp_percent=`echo $gfp_count $total_g | awk '{print ($1/$2)*100}'`
			gfn_percent=`echo $gfn_count $total_g | awk '{print ($1/$2)*100}'`
			acc_percent=`echo $frame_pos $total | awk '{print ($1/$2)*100}'`

			echo "Redfp_${i}_${j}" $rfp_percent $rfp_no
			echo "Greenfp_${i}_${j}" $gfp_percent $gfp_no			
			echo "Redtp_${i}_${j}" $rtp_percent $rtp_no			
			echo "Greentp_${i}_${j}" $gtp_percent $gtp_no			
			echo "Redfn_${i}_${j}" $rfn_percent $rfn_no			
			echo "Greenfn_${i}_${j}" $gfn_percent $gfn_no			
			echo "Acc_${i}_${j}" $acc_percent			
			echo "ann_${i}_${j}" $total_ann $red_count $green_count			
		done
	done
done



# ##crp nofil

# total_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | wc -l`
# total_rcrp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==0 {print}' | wc -l`
# total_gcrp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==1 {print}' | wc -l`

# rfp_count_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {print}' | wc -l`
# gfp_count_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {print}' | wc -l`
# rtp_count_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {print}' | wc -l`
# gtp_count_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {print}' | wc -l`
# rfn_count_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {print}' | wc -l`
# gfn_count_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {print}' | wc -l`
# frame_pos_crp_nofil=`cat data/sensor_pos_neg_crp_nofil.txt | awk -F\; 'NR>1 && $9=="True" {print}' | wc -l`

# rtp_percent_crp_nofil=`echo $rtp_count_crp_nofil $total_rcrp_nofil | awk '{print ($1/$2)*100}'`
# rfp_percent_crp_nofil=`echo $rfp_count_crp_nofil $total_rcrp_nofil | awk '{print ($1/$2)*100}'`
# rfn_percent_crp_nofil=`echo $rfn_count_crp_nofil $total_rcrp_nofil | awk '{print ($1/$2)*100}'`
# gtp_percent_crp_nofil=`echo $gtp_count_crp_nofil $total_gcrp_nofil | awk '{print ($1/$2)*100}'`
# gfp_percent_crp_nofil=`echo $gfp_count_crp_nofil $total_gcrp_nofil | awk '{print ($1/$2)*100}'`
# gfn_percent_crp_nofil=`echo $gfn_count_crp_nofil $total_gcrp_nofil | awk '{print ($1/$2)*100}'`
# acc_percent_crp_nofil=`echo $frame_pos_crp_nofil $total_crp_nofil | awk '{print ($1/$2)*100}'`

# ##nocrp fil

# total_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | wc -l`
# total_rnocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==0 {print}' | wc -l`
# total_gnocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==1 {print}' | wc -l`

# rfp_count_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {print}' | wc -l`
# gfp_count_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {print}' | wc -l`
# rtp_count_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {print}' | wc -l`
# gtp_count_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {print}' | wc -l`
# rfn_count_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {print}' | wc -l`
# gfn_count_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {print}' | wc -l`
# frame_pos_nocrp_fil=`cat data/sensor_pos_neg_nocrp_fil.txt | awk -F\; 'NR>1 && $9=="True" {print}' | wc -l`

# rtp_percent_nocrp_fil=`echo $rtp_count_nocrp_fil $total_rnocrp_fil | awk '{print ($1/$2)*100}'`
# rfp_percent_nocrp_fil=`echo $rfp_count_nocrp_fil $total_rnocrp_fil | awk '{print ($1/$2)*100}'`
# rfn_percent_nocrp_fil=`echo $rfn_count_nocrp_fil $total_rnocrp_fil | awk '{print ($1/$2)*100}'`
# gtp_percent_nocrp_fil=`echo $gtp_count_nocrp_fil $total_gnocrp_fil | awk '{print ($1/$2)*100}'`
# gfp_percent_nocrp_fil=`echo $gfp_count_nocrp_fil $total_gnocrp_fil | awk '{print ($1/$2)*100}'`
# gfn_percent_nocrp_fil=`echo $gfn_count_nocrp_fil $total_gnocrp_fil | awk '{print ($1/$2)*100}'`
# acc_percent_nocrp_fil=`echo $frame_pos_nocrp_fil $total_nocrp_fil | awk '{print ($1/$2)*100}'`

# ##crop fil

# total_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | wc -l`
# total_rcrp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==0 {print}' | wc -l`
# total_gcrp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==1 {print}' | wc -l`

# rfp_count_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {print}' | wc -l`
# gfp_count_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {print}' | wc -l`
# rtp_count_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {print}' | wc -l`
# gtp_count_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {print}' | wc -l`
# rfn_count_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {print}' | wc -l`
# gfn_count_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {print}' | wc -l`
# frame_pos_crp_fil=`cat data/sensor_pos_neg_crp_fil.txt | awk -F\; 'NR>1 && $9=="True" {print}' | wc -l`

# rtp_percent_crp_fil=`echo $rtp_count_crp_fil $total_rcrp_fil | awk '{print ($1/$2)*100}'`
# rfp_percent_crp_fil=`echo $rfp_count_crp_fil $total_rcrp_fil | awk '{print ($1/$2)*100}'`
# rfn_percent_crp_fil=`echo $rfn_count_crp_fil $total_rcrp_fil | awk '{print ($1/$2)*100}'`
# gtp_percent_crp_fil=`echo $gtp_count_crp_fil $total_gcrp_fil | awk '{print ($1/$2)*100}'`
# gfp_percent_crp_fil=`echo $gfp_count_crp_fil $total_gcrp_fil | awk '{print ($1/$2)*100}'`
# gfn_percent_crp_fil=`echo $gfn_count_crp_fil $total_gcrp_fil | awk '{print ($1/$2)*100}'`
# acc_percent_crp_fil=`echo $frame_pos_crp_fil $total_crp_fil | awk '{print ($1/$2)*100}'`


