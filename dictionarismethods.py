# dictionaries methods

student={
"name" : "kshitija",
"score" : {
"chem": 98
    }
    }
print(student)
print(student.keys())
print(len(list(student.keys())))
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"city" : "mumbai"})
print(student)
