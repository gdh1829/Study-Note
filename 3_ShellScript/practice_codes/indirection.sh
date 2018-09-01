#!/bin/bash

# indirection
min_1="777"
function getMin() {
    local tmp="";
    tmp="min_$1";

    echo ${!tmp};
}

a=1
bb=`getMin $a`

echo $bb
