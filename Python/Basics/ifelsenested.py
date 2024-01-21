# take positive input tell it is divisible by 5 and 3 but not 15

n1=int(input("Enter the Number "))

if n1%5==0:
    if n1%3==0:
        print("Entered Number is divisible by 5 and 3")
    else:
        print("Entered number is only dicvisible by 3")
else:
    print("Number is Not divisible By 15")