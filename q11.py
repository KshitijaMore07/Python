s=input("Enter a string:")
lowercase=uppercase=digits=symbols=0
for char in s:
    if char.islower():
        lowercase+=1
    elif char.isupper():
       uppercase+=1
    elif char.isdigits():
       digits+=1
    else:
        symbols+=1
print("Lowercase:",lowercase)
print("Uppercase:",uppercase)
print("Digits:",digits)
print("Symbols:",symbols)
