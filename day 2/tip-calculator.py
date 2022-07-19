print("Welcome to the Tip Calculator😁");
bill = int(input("What was the total bill? $"));
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "));
num_people = int(input("How many people split the bill? "));

tip /= 100;
bill += tip;
pay = bill / num_people;
pay = round(pay, 2);

print(f"Each person should pay ${pay}.");
print("You're Welcome 😉.");