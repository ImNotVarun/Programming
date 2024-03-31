class Account:
    def __init__(self, balance, account_no):
        self.balance = int(balance)
        self.account_no = account_no

    def debit(self):
        user = int(input("Enter the amount you wanna debit :"))
        if self.balance < user:
            print("Insufficent Balance")
        else:
            self.balance = self.balance-user
            print("Remanning Balance :", self.balance)

    def credit(self):
        user = int(input("Enter the amount you wanna credit in the account :"))
        self.balance = self.balance+user
        print("Updated Balance :", self.balance)

    def info(self):
        print("Balance :", self.balance, 'Account NO :', self.account_no)


A1 = Account(2000, 122)

while True:
    User_Input = int(input(
        "What do you wanna do \n1.Debit from account \n2.Credit from account \n3.Show account info \n4.Quit\n"))
    match (User_Input):
        case (1):
            A1.debit()
        case (2):
            A1.credit()
        case 3:
            A1.info()
        case 4:
            print("Exiting...")
            break
