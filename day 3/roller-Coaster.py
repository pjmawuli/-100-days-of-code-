print("Welcome to the Roller Coaster Ride 😋");
height = int(input("So tell me 😏 how tall are you? "));

bill = 0;

if height < 120:
    print("Sorry kid 😣 you're too short.");
    print("You'll die if you take this ride.");
    
else:
    age = int(input("How old are you 🤔? "));
    if age <= 12:
        bill = 7;
        print("You're still a kid");
        print("Your ticket costs $7.");
    elif age <= 18:
        bill = 43;
        print("You're a teen huh, your tickets costs $43.");
    elif age >= 45 and age <= 55:
        bill = 0;
        print("We know you're going through a lot. Fighting!!!✌️ ✌️ 🤗");
    else:
        bill = 400;
        print("You my good Sir/Madam will have to pay $400 for your tickets.");

    wants_photo = input("Do you want a photo taken? Y or N? ");
    if wants_photo == "Y":
        if age >= 45 and age <= 55:
            print("Your photo is free.");

            bill = 0;

        else:
            print("The cost of taking a photo is $5.");
            bill += 5;
            print(f"Your total bill is ${bill}");
    