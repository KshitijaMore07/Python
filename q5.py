for num in range(20,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is Non-Prime")
                break
            else:
                print(num,"is Prime")
