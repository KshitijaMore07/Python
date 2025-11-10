#search if the word "learning" exists in the file or not
word="learning"
with open("practice.txt","r")as f:
    data=f.read()
   
    if(data.find("word")!=-1):
        print("FOUND")
    else:
        print("not FOUND")
        
