
class Student:
    def __init__(self, Name, python, java, javascript):
        self.Name = Name
        self.python = python
        self.java = java
        self.javascript = javascript

    @staticmethod
    def hello():
        print("Hello world")

    def avg(self):
        avg = (self.python+self.java+self.javascript)/3
        return avg


s1 = Student("varun", 12, 23, 34)
print(s1.avg())
s1.hello()
