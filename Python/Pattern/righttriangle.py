# right triangle
'''n=int(input("Enter the number"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
# triangle
n=int(input("enter N "))

for i in range(n+1):
    print(" "*(n-i),end='')
    for j in range(1,2*i):
        print(j,end='')
    print()'''
#right triangle rotate
for i in range(4):
    for j in range(4-i):
        print("#",end='')
    print()
