from audioop import add


print("Welcome to the Python Pizza Deliveries!");
size = input("What size of Pizza do you want? S, M or L? ");

add_peperoni = input("Do you want Peperoni? Y or N? ");
extra_cheese = input("Would you like extra cheese? Y or N? ");

bill = 0;

if size == "L":
    bill = 25;
    print("A large pizza costs $25.");
    if add_peperoni == "Y":
        bill += 3;

elif size == "M":
    bill = 15;
    print("A medium sized pizza costs $15.");
    if add_peperoni == "Y":
        bill += 3;

elif size == "S":
    bill = 5;
    print("A small pizza costs $5.");
    if add_peperoni == "Y":
        bill += 2;

if extra_cheese == "Y":
    bill += 1;

print(f"Your total bill is ${bill}.");
