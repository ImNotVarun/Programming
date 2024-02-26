#!/bin/bash
# to print file that have the read , write and excute permission in the current directory
for i in *; do
    if [ -r $i -a -w $i -a -x $i ]; then
        echo $i " - Has the all permission of read write and execute"
    fi
done
