#!/usr/bin/env bash

clear
echo " The Top 3 prices: "
res=$(cut -d',' -f2 data.csv | tr -d ' ' | sort -n | tail -3)
i=1
for r in $res
do
   echo "price $i is $r"
   i=$((i+1))
done
exit
