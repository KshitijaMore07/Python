import re

password=input("Enetr password:")
pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
