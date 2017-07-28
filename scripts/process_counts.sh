#!/bin/bash

total=`cat pos_neg_cnt_data.txt | wc`

tp_count=`cat pos_neg_cnt_data.txt | awk '$3>0 {print}' | wc -l`
fp_count=`cat pos_neg_cnt_data.txt | awk '$4!=0 {print}' | wc -l`
fn_count=`cat pos_neg_cnt_data.txt | awk '$5!=0 {print}' | wc -l`

tp_percent=`echo $tp_count $total | awk '{print ($1/$2)*100}'`
fp_percent=`echo $fp_count $total | awk '{print ($1/$2)*100}'`
fn_percent=`echo $fn_count $total | awk '{print ($1/$2)*100}'`

echo "True Positive" $tp_percent 
echo "False Positive" $fp_percent 
echo "False Negative" $fn_percent