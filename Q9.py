import os

def operations():
    os.rename("demo1.txt","demo2.txt")
    os.remove("hi.txt")
    j=open("Myfile.txt","r+")
    o=open("1st.txt","w")
    k=j.read()
    print(k)
    if k:
        new="o"+k[1:]
        j.seek(0)
        j.write(new)
        j.truncate()


operations()
