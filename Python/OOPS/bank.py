class BankAccount:

    # TODO: Implement the __init__ method
    def constr(self, Name, account_no, Phone_no, balance):
        self.Name = Name
        self.account_no = account_no
        self.Phone_no = Phone_no
        self.balance = balance
    # TODO: Implement the deposit method

    def deposite(self, amount):
        userinput = input("enter the name of the account holder")
        for i in accounts:
            if userinput == accounts.Name:
                updated = int(input("enter the ammount :"))
                accounts.balance.append(updated)
                print(accounts.balance)

    # TODO: Implement the withdraw method
    pass

    # TODO: Implement the get_balance method
    def get_balance():
        userinput = input("enter the name of the account holder")
        for i in accounts:
            if userinput == accounts.Name:
                print(accounts.balance)
            else:
                print("The customer did not exist")

    # TODO: Implement the display_account_info method
    def display_account_info():
        userinput = input("Please enter the name ")
        if (userinput == account1.Name):
            print(account1.__dict__.items())
        else:
            print(account2.__dict__.items())


# TODO: Create an instance of the BankAccount class with appropriate initial values
account1 = BankAccount("Samay", 12345678, 9876543210, 2000)

# TODO: Create another instance of the BankAccount class with different initial values
account2 = BankAccount("Varun", 87654321, 1234567890, 1000)
accounts = [account1, account2]
# TODO: Deposit some amount into account1
# Example: account1.deposit(500)

# TODO: Withdraw some amount from account2
# Example: account2.withdraw(200)

# TODO: Display the account information for account1
# Example: account1.display_account_info()

# TODO: Display the account information for account2
# Example: account2.display_account_info()

# TODO: Get the balance of account1
# Example: balance = account1.get_balance()
# print(f"Balance of account1: {balance}")

# TODO: Try withdrawing an amount greater than the balance from account2
# Example: account2.withdraw(10000)
