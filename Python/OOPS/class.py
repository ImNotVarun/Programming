
# ? creating a class for student

class Students:
    name = None
    age = None
    roll_no = None
    father_name = None
    mother_name = None
    address = None
    phone_no = None
    email_id = None


si = Students()
si.name = "Varun"
si.age = 20
si.roll_no = 1
si.father_name = "Mr. Virender Singh"
si.mother_name = "Mrs. Babli Singh"
si.address = "123 Main Street, Anytown, CA 12345"
si.phone_no = "123-456-7890"
si.email_id = "varun@example.com"

for i, j in si.__dict__.items():
    print(i, j)


#! Same as the first one but with the constructor

class MyClass:
    def __init__(self, Name, age, roll_no, father_name, mother_name, address, phone_no, email_id):
        self.Name = Name
        self.age = age
        self.roll_no = roll_no
        self.father_name = father_name
        self.mother_name = mother_name
        self.address = address
        self.phone_no = phone_no
        self.email_id = email_id

    def Welcome(self):
        print("Welcome to the class", self.Name)


# ? adding value to the constructor and printing it

Varun = MyClass("Varun",
                20,
                1,
                "Mr. Virender Singh",
                "Mrs. Babli Singh",
                "123 Main Street, Anytown, CA 12345",
                "123-456-7890",
                "varun@example.com")
for i, j in Varun.__dict__.items():
    print(i, j)


#! adding value to the constructor and printing it

Samay = MyClass("Samay", 201, 2, "Mr. Darmendra Singh", "Mrs. Lovely Singh",
                "123 Main Street, Anytown, CA 12345", "123-456-7890", "samay@example.com")
for i, j in Samay.__dict__.items():
    print(i, j)


# ? calling the welcome fuction
Varun.Welcome()
Samay.Welcome()
