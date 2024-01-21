# find greator number from 3 number
num1=int(input("enter first number"))
num2=int(input("enter first number"))
num3=int(input("enter first number"))

if num1>num2 and num1>num3:
    print("Greater Number is -",num1)
elif num2>num1 and num2>num3:
    print("Greater Number is -",num2)
else :
    print("Greater Number is -",num3)