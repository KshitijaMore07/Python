class Person:
    name="annonymous"

    def changeName(self, name):
        self.name=name

p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)
