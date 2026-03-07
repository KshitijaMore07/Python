with open("Myfile.txt","r")as f1, open("Newfile.txt","w")as f2:
    content=f1.read()
    f2.write(content)

with open("Newfile.txt","r")as f2:
    print(f2.read())
