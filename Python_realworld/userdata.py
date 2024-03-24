User_One = {
    "name": "john",
    "age": 30,
    "city": "New York"
}
User_two = {
    "name": "jane",
    "age": 20,
    "city": "New York"
}

User_three = {
    "name": "mary",
    "age": 10,
    "city": "New York"
}

User_four = {
    "name": "peter",
    "age": 40,
    "city": "New York"
}


User_five = {
    "name": "lisa",
    "age": 50,
    "city": "New York"
}
users = [User_One, User_two, User_three, User_four, User_five]

print("Welcome to the Database \n enter what you wanna do \n Here is What you can do \n 1.Add a new cutomer in the database \n 2.Delete or add customer in  the database \n 3.See details of a customer from the database")

entered = input("Enter your choice")
match entered:
    case "3":  # See details of a customer from the database
        print("Enter the name of the customer")
        name = input().lower()
        for user in users:
            if name == user["name"]:
                print(user)
                break  # break the loop if the customer is found
        else:
            print("Customer not found")

    case "2":
        print("Enter the name of the customer you want to delete")
        name = input().lower()
        for user in users:
            if name == user["name"]:
                print(user)
                print(
                    "What you want to Delete \n 1.Name \n 2.Age \n 3.City \n 4.Delete the customer")
                choice = input()

                if choice == "1":
                    user["name"] = input("Enter the new name")
                    print(user)

                elif choice == "2":
                    # Check if the input is an integer
                    user["age"] = input("Enter the new age")
                    if (user["age"].isdigit()):
                        print("Done", user)
                    else:
                        print("Invalid age")

                elif choice == "3":
                    user["city"] = input("Enter the new city")
                    print(user)

                elif choice == "4":
                    print("Customer deleted")
                    users.remove(user)
                    print(users)

                else:
                    print("Invalid choice")
                break
        else:
            print("No such customer")
    case "1":
        print("Enter the name of the customer")
        name = input().lower()
        for user in users:
            if name == user["name"]:
                print("Customer already exists")
                break
        else:
            print("Customer not found")
