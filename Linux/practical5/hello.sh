#!/bin/bash
read a
if [ $a -lt 0 ]; then
    echo A is a negative number
else
    echo A is a positive number
fi
