user_input=int(input("Entyer input:"))
print("Reverse table of {user_input} is as follows")
for i in range(10,0,-1):
    reverse=user_input *i
    print(f'{user_input} * {i}={reverse}')
    