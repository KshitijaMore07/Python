lst=[1,3,5,7,'hello','python']
search=input("enter number or string to search:")
if search.isdigit():
    search=int(search)
found=False
for item in lst:
    if item==search:
        found=True
        break
if found:
     print("Found:",search)
else:
     print("Not Found")
