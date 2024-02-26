#!/bin/bash
# print directory content if directory or print content of the file if file
for i in *; do
    if [ -d $i ]; then
        ls "$i"
        break
    else
        cat $i
    fi
done
