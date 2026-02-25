def multiply(a,*args):
    product=a
    for num in args:
        product*=num
    return product
print(multiply(2,3,4))
print(multiply(5))
