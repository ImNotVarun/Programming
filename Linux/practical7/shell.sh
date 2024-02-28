#!/bin/bash
# print directory content if directory or print content of the file if file
echo "Enter the path or file name"
read input
if [ -f "$input" ]; then
    echo "The file content is : "
    cat $input
else
    echo "The directory content is : "
    ls "$input"
fi
