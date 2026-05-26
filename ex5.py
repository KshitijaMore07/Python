user_input=int(input("ENter a number"))
sum_result=0
for i in range(0, user_input +1):
    sum_result += i
print(f'Sum of numbers from 0 to{user_input} is: {sum_result}')