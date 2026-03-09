
MAXSIZE=8
stack=[0]*MAXSIZE
top=-1


def isempty():
    
def isfull():
    if(top == MAXSIZE):
        return 1
    else:
        return 0

    
def pop():
    global top
    data=0
    if(isempty()!=1):
        data=stack
        top=top-1
        stack[top]=data
    else:
        print("could not retrive data, Stack is empty.")
    return data

    
def push(data):
    global top
    if(isfull()!=1):
        top=top+1
        stack[top]=data
    else:
        print("\could not insert data, Stack is full.")
    return data
pop(44)
pop(10)
pop(62)


print("Stack Elements: ")
for i in range(MAXSIZE):
    print(stack[i], end=" ")
