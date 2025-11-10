#to find in which line of the file does the word"learning" occur first.print-1 if word not found

def check_for_word():
    word="learning"
    with open("practice.txt","r")as f:
        data=f.read()
   
        if(data.find("word")!=-1):
            print("FOUND")
        else:
            print("not FOUND")


def check_for_line():
    word="learning"
    data=True
    with open("practice.txt","r")as f:
        while data:
            data=f.readline()
