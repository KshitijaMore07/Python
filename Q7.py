import re

msg=input("Enter chat message")

hashtags=re.findall(r'#\w+',msg)

mentions=re.findall(r'@\w+',msg)

print("Hashtags:",hashtags)
print("Mentions:",mentions)
