with open("demo1.txt","r")as f1, open("demo2.txt","w")as f2:
    lines=f1.readlines()
    for i in range(len(lines)):
        if i !=2:
            f2.write(lines[i])

print("New file created after skipping line 3.")
