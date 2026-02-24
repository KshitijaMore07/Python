weight=float(input("Enter your weight in your kg:"))

height=float(input("Enter your height in meters:"))

bmi=weight/(height**2)
print(f"Your BMI is:{bmi:2f}")
if bmi<18.5:
     print("Category:Underweight")
elif 18.5<=bmi<25:
     print("Category:Normal weight")
elif 25<=bmi<30:
     print("Category:Overweight")
else:
    print("Category:Obese")
