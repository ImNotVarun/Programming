num1=int(input("enter the first number "))
num2=int(input("enter the second number"))

Operator=input("enter the operator")

match Operator:
    case "+":
        print("Sum of Numbers is",num1+num2)
    case "-":
        print("Sub of numbers is ",num1-num2)
    case "/":
        print("div of number is ",num1/num2)
    case "*":
        print("mul of the numbers is ",num1*num2)
    case _ :
        print("operator is invalid")
while True:
    choice = input("Do you want to continue? (y/n): ")
    if choice == "y" or choice == "Y":
        continue
    elif choice == "n" or choice == "N":
        print("Thank you for using calculator")
        break
    else:
        print("Invalid choice")
#lolollolololo