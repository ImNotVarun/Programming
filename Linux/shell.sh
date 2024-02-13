#!sh
                        #adding of two numbers in bash
# echo Enter first number
# read num1
# echo "Enter second number"
# read num2
# sum=$(($num1+$num2))
# echo "Sum is $sum"

                       #arthmatic oprationsion in bash
# read num1
# read num2
# sum=$(($num1+$num2))
# sub=$(($num1-$num2))
# mul=$(($num1*$num2))
# div=$(($num1/$num2))
# echo "Sum is $sum"
# echo "Sub is $sub"
# echo "Mul is $mul"
# echo "Div is $div"

                      # if else statements for even odd numbers
# echo enter first number
# read num1

# if (($num1%2==0 ))
# then echo this is a even number
# else echo this is a odd number
# fi

              #asks the user to input a number and checks if it's divisible by both 3 and 5.
# echo num
# read num
# if (($num%3==0 && $num%5==0))
# then echo it is devisible by both 3 and 5
# else echo it can not be divisivle by 3 and 5
# fi

#the user for two numbers and then determine and print the larger of the two numbers.
echo enter the number
read num
echo enter the second number
read num2
if (($num>$num2))
then echo The largest numbers is $num
else echo The largest numbers is $num2
fi