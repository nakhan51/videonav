#!/bin/bash

total=`cat data/pos_neg_nocrop.txt |wc -l`
total_r=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==0 {print}' |wc -l`
total_g=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==1 {print}' | wc -l`

rfp_count=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {print}' | wc -l`
gfp_count=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {print}' | wc -l`
rtp_count=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {print}' | wc -l`
gtp_count=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {print}' | wc -l`
rfn_count=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {print}' | wc -l`
gfn_count=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {print}' | wc -l`
frame_pos=`cat data/pos_neg_nocrop.txt | awk -F\; 'NR>1 && $9=="True" {print}' | wc -l`

rtp_percent=`echo $rtp_count $total_r | awk '{print ($1/$2)*100}'`
rfp_percent=`echo $rfp_count $total_r | awk '{print ($1/$2)*100}'`
rfn_percent=`echo $rfn_count $total_r | awk '{print ($1/$2)*100}'`
gtp_percent=`echo $gtp_count $total_g | awk '{print ($1/$2)*100}'`
gfp_percent=`echo $gfp_count $total_g | awk '{print ($1/$2)*100}'`
gfn_percent=`echo $gfn_count $total_g | awk '{print ($1/$2)*100}'`
acc_percent=`echo $frame_pos $total | awk '{print ($1/$2)*100}'`

total_crp=`cat data/pos_neg_nocrop.txt | wc -l`
total_rcrp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==0 {print}' | wc -l`
total_gcrp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==1 {print}' | wc -l`

rfp_count_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==0 && $5!=0 {print}' | wc -l`
gfp_count_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==1 && $6!=0 {print}' | wc -l`
rtp_count_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==0 && $3>0 {print}' | wc -l`
gtp_count_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==1 && $4>0 {print}' | wc -l`
rfn_count_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==0 && $7!=0 {print}' | wc -l`
gfn_count_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $12==1 && $8!=0 {print}' | wc -l`
frame_pos_crp=`cat data/pos_neg_crop.txt | awk -F\; 'NR>1 && $9=="True" {print}' | wc -l`

rtp_percent_crp=`echo $rtp_count_crp $total_rcrp | awk '{print ($1/$2)*100}'`
rfp_percent_crp=`echo $rfp_count_crp $total_rcrp | awk '{print ($1/$2)*100}'`
rfn_percent_crp=`echo $rfn_count_crp $total_rcrp | awk '{print ($1/$2)*100}'`
gtp_percent_crp=`echo $gtp_count_crp $total_gcrp | awk '{print ($1/$2)*100}'`
gfp_percent_crp=`echo $gfp_count_crp $total_gcrp | awk '{print ($1/$2)*100}'`
gfn_percent_crp=`echo $gfn_count_crp $total_gcrp | awk '{print ($1/$2)*100}'`
acc_percent_crp=`echo $frame_pos_crp $total_crp | awk '{print ($1/$2)*100}'`


#echo "Red" $rfp_percent $rfp_percent_crp
#echo "Green" $gfp_percent $gfp_percent_crp
#echo "Red" $rtp_percent $rtp_percent_crp
#echo "Green" $gtp_percent $gtp_percent_crp
#echo "Red" $rfn_percent $rfn_percent_crp
#echo "Green" $gfn_percent $gfn_percent_crp
echo "Acc" $acc_percent $acc_percent_crp
