''' Write a Python function that takes a password string as input and validates it according to the following rules:
The password must be at least 8 characters long
The password must contain at least one uppercase letter
The password must contain at least one lowercase letter
The password must contain at least one digit
The password must contain at least one special character (@, #, $, %, etc.)'''

Password = input("Enter the Password")
if (Password<len(8)):
    print("The Password Must containes at least 8 characters")
elif (Password.upper()):
    print("The password must container a upper letter")
else:
    print("i dont know")