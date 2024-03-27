# A company wants to automate the process of sending out invoices to customers. They have a list of customer data stored in a CSV file. Write a Python function that takes the CSV file as input and generates a PDF invoice for each customer.

import csv

with open('D:\Compiling_Coding\Programming\Python_realworld\Invoices\customers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

f = open('C:\Comipling_Codes\Compiling_Coding\Programming\Python_realworld\Invoices\customers.csv', "+r")
print(f.read())
