with open("Myfile.txt","r")as f:
    lines=f.readlines()
    if len(lines)>=5:
        print("Line 5:",lines[4].strip())
    else:
        print("File has less than 5 lines.")
