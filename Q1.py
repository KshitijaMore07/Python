import re
email=input("Enter student email:")
pattern=r'^[a-zA-Z0-9._%+-]+@college\.edu$'

if re.match(pattern, email):
    print("Valid Student Email")
else:
    print("Invalid Student Email")
