# 48. Simple Class and Object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} scored {self.marks} marks")

s1 = Student("Asha", 88)
s1.display()
