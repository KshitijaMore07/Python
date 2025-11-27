#constructor invoke(execute) automatically when object is created or at the time of object creation
#a constructor always taking a parameter which id called as self(which means new object is created)
class Student:
    name="kshitija"
    def __init__(self):
        print(self)
        print("adding new student in database..")
s1=Student()
        
