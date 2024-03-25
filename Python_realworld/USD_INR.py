
def INR_to_USD():
    INR = int(input("Enter Rupees :"))
    USD = INR/83
    print("Rupees in Dollar :", int(USD), "$")


def USD_to_INR():
    USD = int(input("Enter in Dollar :"))
    INR = USD*83
    print("Dollar in Rupees :", int(INR), "₹")


print("What you wanna do")

while True:
    IN = int(input("1. INR to USD\n" "2. USD to INR\n"))

    match (IN):
        case (1):
            INR_to_USD()

        case (2):
            USD_to_INR()
    INPUT = input("Do you want to continue Y/N :").capitalize()
    if (INPUT == "Y"):
        continue

    else:
        print("Thanks for using our service")
        break
