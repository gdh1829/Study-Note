#!/bin/bash

file_path="/home/aggregate/hrbc-system-report/logs/daily-report/resource-count/hrbc-daily-resource-count-report_Db5.csv"

for line in `cat $file_path| cut -d',' -f4`; do
    echo $line
    length=${#test[@]}
    test[$length]=$line
done

echo ${test[@]}
