#BMI calculator
print("This is a program to calculte your BMI\n")
weight=int(input("Enter your weight\n"))
height=float(input("Enter your height\n"))
bmi=weight/height **2
bmi_round=round(bmi,2)
print(f"your bmi is {bmi_round}")

 