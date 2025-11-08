#WAP to find the sum of first n numbers(using while)

n=7
sum=0
i=1
while i<=n:
    sum +=i
    i +=1
print("total sum=",sum)







#or(using for)


n=5
sum=0
for i in range(1, n+1):
    sum +=i
print("total sum=",sum)
