#!/bin/bash

for i in 0 1 2; do
    echo $i
done

for i in {0..2}; do
    echo $i
done

#unavailable loop
length=2
for i in {0..$length}; do
    echo $i #output is just literally like {0..2}
done

#wildcard
for i in hello 1 * 2 goodbye; do
  echo "Looping ... i is set to $i"
done
#output
# Looping ... i is set to hello
# Looping ... i is set to 1
# Looping ... i is set to (name of first file in current directory)
#     ... etc ...
# Looping ... i is set to (name of last file in current directory)
# Looping ... i is set to 2
# Looping ... i is set to goodbye

# c language style loop
for (( i=0; i<10; i++)); do
    echo $i
done