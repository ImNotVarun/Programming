# if cost and selling price of an item is input by user , write a program to deetermine whether the seller made a profit or loss or no profit or no loss , also determine how much profit or loss he occure

Cost = int(input("Enter The cost of the product"))
selling_price = int(input("Enter the selling price of the product"))
sum=selling_price-Cost
if selling_price > Cost:
    print("it is a profit \n""profit =",sum, "rs")
elif selling_price < Cost:
    print("It is a loss\n ""Loss =", sum)
else:
    print("Ther is no profit and loss")
