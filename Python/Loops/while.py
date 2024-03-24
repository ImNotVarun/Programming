# n = 0
# while (n <= 100):
#     print(n)
#     n += 1

# n = 100
# while (n >= 0):
#     print(n)
#     n -= 1

# no = int(input("enter a number"))
# i = 1
# while i <= 10:
#     print(no*i)
#     i += 1

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # while idx < len(list):
# #     print(list[idx])
# #     idx += 1
# x = 36
# idx = 0
# for i in list:
#     if (i == x):
#         print("Found the number at", idx)
#     idx += 1


# for i in range(101):
#     print(i)

# for i in range(101, 0, -1):
#     print(i)

# no = int(input("enter a number"))
# for i in range(1, 11):
#     print(no*i)

no = int(input("enter a number"))
# i = 0
# sum = 0
# while i <= no:
#     sum = i+sum
#     i += 1
# print("Sum of the natural number is :", sum)

# sum = 0
# for i in range(0, no+1):
#     sum = i+sum
# print("Sum of the natural number is :", sum)
fac = 1
for i in range(1, no+1):
    fac = fac*i
    print(fac)
