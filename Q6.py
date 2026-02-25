import re
text=input("Enter text with numbers: ")

numbers=re.findall(r'\d+',text)

print("External Numbers:", numbers)
