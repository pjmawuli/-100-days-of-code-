print("Welcome to the Leap Year determiner.");
year = int(input("What year do you want to check? "));

if year % 4 == 0:
    if year % 100 != 0:
        print("Ya! It's a leap year.");
    elif year % 400 == 0:
        print("Ho Ho It's a leap year.");
else:
    print("Nope this isn't a Leap Year. My Brazza!");