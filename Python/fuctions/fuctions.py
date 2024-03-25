# fuction examples

def sum(a, b):  # fuctions parameters
    s = a+b
    print(s)


sum(2, 4)  # calling the function


# fuction for genrating the average of three numbers

def aveg(x, y, z):
    avg = (x+y+z)/3
    print(avg)
    return avg


aveg(98, 97, 95)


# fuction for multiplication of two numbers

def Mul(a, b, c):
    mul = a*b*c
    print(mul)
    return mul


Mul(1, 2, 3)

# fuction to print the length of the list

list = ["objectA", "objectB", "objectC"]


def abc():
    print(len(list))


abc()

# fuction to Print the element of the list in a single line

list1 = ["hello", "world", "mother", "brother"]


def ele():
    for ele in list1:
        print(ele, end=" ")
    print("\n")


ele()

# fuction to find a factorial of N


def fac(x):
    facc = 1
    for i in range(1, x+1):
        facc *= i
    print(facc)


fac(5)
