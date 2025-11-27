#Attribute means any data


class Student():
    college_name="Fergusson College"
    name="anonymous" #Class.attr

    def __init__(self, fullname):
        self.name=fullname #obj.attr > Class.attr
        

s1=Student("Kshitija", 89)
print(s1.name)
