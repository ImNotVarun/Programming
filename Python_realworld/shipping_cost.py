'''Shipping Cost Calculator: Write a program that calculates the shipping cost for an online order based on the total weight of the order. The program should take the weight as input and apply the following rules:
If the weight is less than or equal to 2 Kg, the shipping cost is $4.99.
If the weight is greater than 2 kg but less than or equal to 8 kg, the shipping cost is $8.99.
If the weight is greater than 8 kg but less than or equal to 15 kg, the shipping cost is $12.99.
If the weight is greater than 15 kg, the shipping cost is $19.99.'''

weight = float(input("Enter the total weight of the shipping :"))

if weight <= 2:
    cost = 4.99
elif weight <= 8:
    cost = 8.99
elif (weight <= 15):
    cost = 12.99
else:
    cost = 19.99
print("The cost will be $", cost)
