print("Welcome to the Leap Year determiner.")
year = int(input("What year do you want to check? "))

while True:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Ho Ho It's a leap year.")
                break
            print("Its not a leap year")
            break
        print("its a leap year")
        break
