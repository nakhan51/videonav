#!/bin/bash

cat > /tmp/data
linestotal=`cat /tmp/data | wc -l`

counter=1
for line in `cat /tmp/data`; do
	echo $counter $linestotal $line | awk '{printf "%f %f\n", $1/$2, $3}' 
	counter=$(($counter+1))
done
