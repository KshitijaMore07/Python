num1=float(input("Enter First number:"))

num2=float(input("Enter Second number:"))





operator=input("Enter operator(+,-,*,/,%,**,//):")

if operator=='+':
    print("Result:",num1+num2)
elif operator=='-':
    print("Result:",num1-num2)
elif operator=='*':
    print("Result:",num1*num2)
elif operator=='/':
    print("Result:",num1/num2)
elif operator=='%':
    print("Result:",num1%num2)
elif operator=='**':
    print("Result:",num1**num2)
elif operator=='//':
    print("Result:",num1//num2)
else:
    print("Invalid operator")
