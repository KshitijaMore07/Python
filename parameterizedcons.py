#A constructor having parameter rather than self this constructor called as parameterized constructor

class Student():
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("example of parameterized constructor...")

s1=Student("kshitija", 90)
print(s1.name, s1.marks)
    
