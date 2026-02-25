import re

mobile=input("Enter mobile number:")
pattern=r'^[6-9]\d{9}$'

if re.match(pattern, mobile):
    print("Valid Indian Mobile Number")
else:
    print("Inavlid Mobile Number")
