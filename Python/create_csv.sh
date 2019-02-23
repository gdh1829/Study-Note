#!/bin/bash
START_TIME=$SECONDS
echo "Start! $START_TIME"
for var in 1 2 3 4 5 6 7 8 9 10; do 
    echo "$var"
    sleep 1s
    echo "$LINENO"
done

echo "ELAPSED_TIME: $(($SECONDS - $START_TIME))"

pwd=`pwd`
