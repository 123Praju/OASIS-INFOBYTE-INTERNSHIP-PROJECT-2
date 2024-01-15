print("Hello! This calculator is use to calculate your BMI")
name = input("Please Enter your name : ")
weight = float(input("Please Enter your weight in kg : "))
height = float(input("Please Enter your height in m : "))

bmi=weight/(height**2)

if (bmi < 18.5) :
    print(f"{name} you are underweight according to BMI where your BMI is {bmi}")
elif (bmi>18.5 and bmi<=24.9):
    print(f"{name} you are healthy according to BMI where your BMI is {bmi}")
else:
    print(f"{name} you are overweight according to bmi where your BMI is {bmi}")