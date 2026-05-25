height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))
BMI = weight / (height/100)**2
print("your BMI is",BMI)
if BMI <= 18.4:
 print("print you are under weight")
elif BMI <= 24.9:
 print("print you are healthy")
elif BMI <= 24.9:
 print("print you are overweight")
elif BMI <= 34.9:
 print("print you are sevearly over weight")
elif BMI <= 34.9:
 print("print you are obese")
else :
 print("you are sevearly obese")