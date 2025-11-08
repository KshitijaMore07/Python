i=1
while i<=5:
    print(i)
    if(i ==3):
        break
    i +=1
print("enf of loop")


nums=(1,4,9,16,25,36,49,64,81,100)

x=36

i=0 #initialization

while i<len(nums):
    if(nums[i] == x):
        print("found at idx",i)
        break
    else:
        print("finding...")
    i+=1
