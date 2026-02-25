import re
date=input("Enter date (dd-mm-yyyy):")
pattern=r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-[0-9]{4}$'

if re.match(pattern, date):
    print("Valid Date")
else:
    print("Invalid Date")
