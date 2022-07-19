height = int(input("Enter your height in m: "));
weight = int(input("Enter your weight in kg: "));

#print(type(height));
#print(type(weight));

bmi = weight / (height ** 2);

int(bmi);

print("Your BMI is: " + str(bmi));