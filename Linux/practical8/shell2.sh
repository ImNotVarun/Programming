#!/bin/bash
total=500
for((i=0;i<5;i++)); do
    echo "Enter the Marks in the subjects"
    read -r marks
    sum=$((sum+marks))
    per=$((sum*100/total))
done

echo "Total Marks ""$sum"
echo "Percentage ""$per""%"


