print("This is a test for dictionary")

Food = {
    "Main dish": "Roti",
    "sabji": "Allu ki sabji",
    "Desert": "Panni"
}

print(Food)


# nested dictionary

dic = {
    "name": "samay",
    "section": "A",
    "subjects": {
        "C": 20,
        "maths": 8,
        "python": 21
    }
}

print(dic)  # print entire dictionary
print(dic["subjects"])  # print the subjects name and marks
# it will print the marks in the python subject
print(dic["subjects"]["python"])
dic["section"] = "B"
print(dic)
dic["surname"] = "Panchal"
print(dic)
