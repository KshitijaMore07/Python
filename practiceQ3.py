dictionary={}
dictionary.update({"math":78})
dictionary.update({"science":88})
dictionary.update({"english":90})
print(dictionary)


#or

marks={}

x=int(input("enter math: "))
marks.update({"math" :x})


y=int(input("enter science: "))
marks.update({"science" :y})

z=int(input("enter english: "))
marks.update({"english" :z})

print(marks)
