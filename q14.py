string=input("Enter a string:")
for ch in set(string):
    print(f"{ch}:{string.count(ch)}",end=",")
