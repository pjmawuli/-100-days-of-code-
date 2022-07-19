height = float(input("How tall are you in cm? "));
weight = float(input("How heavy are you in kg? "));

bmi = weight / (height ** 2);
bmi = round(bmi, 2);

print(f"Your BMI is {bmi}.");

if bmi <= 18.5:
    print("You really have to take better care of yourself. You are underweight 😔.");
elif bmi <= 25:
    print("Looks like someone has been taking good care of themselves. Your BMI is pretty normal.");
elif bmi <= 30:
    print("Careful your BMI says you are overweight.");
elif bmi <= 35:
    print("Yikes! 😬 take better care of yourself. Your BMI says you are obese. Maybe you should see a doctor or a trainer?");
elif bmi > 35:
    print("Okay Hun, I'm calling a doctor you need help. You are clinically obese.");