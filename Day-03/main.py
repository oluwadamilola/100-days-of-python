print("BMI calculator")

height = float(input("whats your height"))
weight = float(input(" what your weight"))
bmi = weight/height*height
if bmi < 18.5:
    print(f"here is your {bmi} you are under weight" )
elif bmi > 30.6:
    print(f"here is your bmi {bmi} you are obese")