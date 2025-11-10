def print_even_odd(start, end):
    if start>end:
        return
    if start%2==0:
        print(f"Even:{start}")
    else:
        print(f"Odd:{start}")
    print_even_odd(start+1, end)

n=int(input("Enetr a limit: "))

print_even_odd(1,n)
