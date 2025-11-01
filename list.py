marks=[12,23,34,34,5,6,7,8,9,0,1,2,3,4,56,89]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
student=["riya",95.4,17,"pune"]
print(student)
student[0]="Arjun"
print(student)


#Slicing

marks=[12,23,34,34,5,6]
#print(marks[1:4])
print(marks[-3:-1])

#list methods

#list.append()-add at the last
list=[2,1,3]
list.append(4)
print(list)

#list.sort()

list=["banana","litchi","mango"]
print(list.sort(reverse=True))
print(list)

#list.reverse()

list=["PRIYA","NEFA","RADHA"]
list.reverse()
print(list)

#list.insert()

list=[2,1,3]
list.insert(1,5)
print(list)

#list.pop()

list=[2,1,3]
list.pop(2)
print(list)

