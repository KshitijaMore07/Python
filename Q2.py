with open("Myfile.txt","r")as f:
    text=f.read()
    words=text.split()
    print("Total words:",len(words))
    
  
