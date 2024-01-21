num1=int(input("enter the first number "))
num2=int(input("enter the second number"))

opreator=input("enter the oprator")

match opreator:
    case "+":
        print("Sum of Numers is",num1+num2)
    case "-":
        print("Sub of numbers is ",num1-num2)
    case "/":
        print("div of number is ",num1/num2)
    case "*":
        print("mul of the numbers is ",num1*num2)
    case _ :
        print("oprator is invalid")