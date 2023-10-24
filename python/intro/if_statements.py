height = 2.1
weight = 77
bmi = weight/height**2

print(f"BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal Weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

if(10 == 10.00):
    print("Equal")
else:
    print("Not Equal")

sentence = "Kenya, Uganda, Tanzania"

if "kenya" in sentence.lower():
    print("Yes, it exists")
else:
    print("Does not exists")