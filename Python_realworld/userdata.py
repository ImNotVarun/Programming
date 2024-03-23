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

print("Welcome to the Database \n enter waht you wanna do \n Here is What you can do \n 1.Add in the database \n 2.Delete from the database \n 3.See details of a customer from the database")

entered = input("Enter your choice")
match entered:
    case "3":  # See details of a customer from the database
        print("Enter the name of the customer")
        name = input().lower()
        if name == User_One["name"]:
            print(User_One)
        elif name == User_two["name"]:
            print(User_two)
        elif name == User_three["name"]:
            print(User_three)
        elif name == User_four["name"]:
            print(User_four)
        elif name == User_five["name"]:
            print(User_five)
        else:
            print("No such customer")
    case "2":
        print("Enter the name of the customer you want to delete")
        name = input().lower()
        if name == User_One["name"]:
            print(User_One)
            print("What you want to Delete \n 1.Name \n 2.Age \n 3.City")
            choice = input()
            if choice == "1":
                User_One["name"] = input("Enter the new name")
                print(User_One)
            elif choice == "2":
                User_One["age"] = int(input("Enter the new age"))
                print(User_One)
            elif choice == "3":
                User_One["city"] = input("Enter the new city")
                print(User_One)
            else:
                print("Invalid choice")
        elif (name == User_two["name"]):
            print(User_two)
