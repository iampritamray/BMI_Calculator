# (BMI calculator)


height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))

bmi = round(weight / height ** 2)
print(f"Your BMI is {bmi}")


if bmi < 18.5:
  print("You are Underweight!")

elif bmi < 25:
  print("You have a normal weight!")

elif bmi < 30:
  print("You are over weight!")

elif bmi < 35:
  print("You are Obese")

else:
  print("DANGER!!! You are clinically Obese!")







