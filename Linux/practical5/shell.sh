#!/bin/bash
# print 1 to 10 number using while loop
n=1
while [ $n -lt 11 ]; do
  echo $n
  let "n+=1"
done
