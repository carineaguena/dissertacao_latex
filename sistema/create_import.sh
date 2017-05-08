#!/bin/bash

while read LINE; do

	echo "{arq_name:$(echo $LINE | awk '{print $1}'),op:$(echo $LINE | awk '{print $2}'),type:$(echo $LINE | awk '{print $3}'),line:$(echo $LINE | awk '{ s = ""; for (i = 4; i <= NF; i++) s = s $i " "; print s }')}"

done < querys
