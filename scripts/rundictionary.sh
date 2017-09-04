#!/bin/bash

types="walk"
sens="nocrp crp"
filter="nofil fil"

for type in $types; do
	for i in $sens; do
		for j in $filter; do
			python detector/dictionaryTF.py processeddata/${type}_annotation.txt processeddata/${type}_${i}_${j}.txt data/${type}_pos_neg_${i}_${j}.txt
		done
	done
done


#python detector/dictionaryTF.py processeddata/cloudy_annotation.txt processeddata/cloudy_nocrp_nofil_12.txt data/cloudy_pos_neg_nocrp_nofil_12.txt
