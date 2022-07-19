age = input("what is your age? ");

age = int(age);
total_years = 90;

years_left = total_years - age;


num_days = years_left * 365;
num_weeks = years_left * 52;
num_months = years_left * 12;


print(f"You have {num_days} days, {num_weeks} weeks, and {num_months} months left to live.");