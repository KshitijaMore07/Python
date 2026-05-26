user_input=int(input("Enter user input :"))
print("table of {user_input} is as follows")
for i in range(1,11,2):
    
    result=user_input * i
    print(f'{user_input}*{i}={result}')