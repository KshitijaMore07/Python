import re
text=input("Enter string with delimiters(,;space):")

result=re.split(r'[;,\s]\s*',text)

print("Split Result:",result)
