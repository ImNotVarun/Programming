
def INR_to_USD():
    INR = int(input("Enter Rupees"))
    USD = INR/83
    print("Rupees in Dollar :", float(USD), "$")


def USD_to_INR():
    USD = int(input("Enter in DOllar"))
    INR = USD*83
    print("DOllar in Rupees :", float(INR), "₹")

    print("What you wanna do")


IN = int(input("1. INR to USD\n" "2. USD to INR\n"))

match (IN):
    case (1):
        INR_to_USD()

    case (2):
        USD_to_INR()
