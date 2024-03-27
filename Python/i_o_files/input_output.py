# this is the learning code

f = open("Programming\Python\Basics\AddNumber.py", "+r")
print(f.read())
f.close()

# # create a file practice.txt and then append or write the lines

with open('practice.txt', 'r+') as f:
    f.write("Hello \n I don't Know why i am learing coding \n because after the Announcement of Devin i am scared")
    Data = f.read()

# Replace A word with another word

with open('practice.txt', 'r+') as f:
    Data = f.read()
new_data = Data.replace("Devin", "Devin (idiot)")
print(new_data)

# find a word in the file

with open('practice.txt', 'r+') as f:
    Data = f.read()
word = Data.find("scared")
if (word != -1):
    print("Found")
else:
    print("Not Found")

# # Find the word in a file and print the line ( Wrong one)
with open("practice.txt", 'r') as f:
    Data = f.read()
    wor = "scared"
    if (Data.readline(wor) == True):
        print("It is present at ", Data.readline(wor))

    else:
        print("-1 the word not found")

# iam a god dam idiot i mean i dont know why i created it whats i am thinking here.......


def cheack():
    for i in Data:
        print(i)
        if (i == "Devin"):
            print(f.append("Fuck you devin"))
        elif (Data.find("Annoucement")):
            print("Yes there is a word called Annoucement")
        else:
            print("Ther is no word name Devin")


cheack()
