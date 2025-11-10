f1=open("file1.txt","r")
data=f1.read().split()
f1.close()

unique=[]
for i in data:
    if i not in unique:
        unique.append(i)

    f2=open("file2.txt","w")
    for i in unique:
        f2.write(i+" ")
    f2.close()

    print("Duplicates removed and saved to file2.txt")
