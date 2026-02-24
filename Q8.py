value=float(input("Enter temperature value:"))

unit=input("Enter unit(C for Celcius,F for Fahrenheit):").upper()

if unit=='C':
    fahrenheit=(value*9/5)+32
    print(f"{value}C={fahrenheit}F")
elif unit=='F':
    celcius=(value-32)*5/9
    print(f"{value}F={celcius}C")
else:
    print("Invalid unit")
