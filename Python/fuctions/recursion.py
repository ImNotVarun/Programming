# def sum(n):
#     if (n == 0):
#         return 1
#     return sum(n-1)*n


# print(sum(5))


string1 = ["hello", "how", "are", "you"]


def lis():
    if len(string1) == 0:
        return "empty string"
    return list(string1)


print(lis())
