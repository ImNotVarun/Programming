#!/bin/bash
                # using until loop for printing the number 1 to 5 
# a=0
# until [ $a -gt 5 ]; do
#     a=$((a+1))
#     echo $a
# done

# write an array that takes input from user to add in the array
arr=()

# Prompt the user for input
echo "Enter elements to add to the array (press q to quit):"
read input
until [ true ]; do
if [ "$input" = "q" ]; then
break
else
    arr+=("$input")
fi

    
done
# Print the array elements
echo "The array elements are: ${arr[@]}"


# while true; do
#     read input
#     if [ "$input" = "q" ]; then
#         break
#     fi
#     arr+=("$input")  # Add the input to the array
# done