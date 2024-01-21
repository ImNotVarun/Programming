# AND and OR using

eng = int(input("enter the marks obtained in english"))

maths = int(input("enter the marks obtained in maths"))

if eng > 80 and maths > 80 :
    print("You got an A")
elif eng > 80 or maths > 80 :
    print("You got an B")
else:
    print("You got a C")
