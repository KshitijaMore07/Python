#Conditionalstatements

#if-elif-else

age=25

if(age>= 18):
    print("can vote and apply for license")


light="green"
if(light =="red"):
    print("stop")
elif(light =="yellow"):
    print("look")
elif(light =="green"):
     print("go")
else:
    print("end of code")



#Nesting

age=98
if(age>= 18):
    if(age>= 80):
        print("cannot drive")
    else:
        print("can drive")
    
