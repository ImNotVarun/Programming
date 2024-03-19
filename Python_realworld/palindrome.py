# program to cheak if the list is a palindrome or not
# it is a palindrome list
list = [1, 2, 3, 2, 1]
lis2 = list.copy()
lis2.reverse()
print(list, lis2)
if (list == lis2):
    print("It is a palindrome list")
else:
    print("Its not a palindrome list")

    # it is not a palindrome list
list = [1, 2, 3, 2, 2]
lis2 = list.copy()
lis2.reverse()
print(list, lis2)
if (list == lis2):
    print("It is a palindrome list")
else:
    print("Its not a palindrome list")
