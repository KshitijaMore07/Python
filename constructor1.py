class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in database..")
s1=Student("kshitija", 97)
print(s1.name, s1.marks)
