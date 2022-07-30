for x in range(1, 101):
    if x % 3 == 0 and x % 15 == 0:
        print("fizz-buzz");
    elif x % 3 == 0:
        print("fizz");
    elif x % 5 == 0:
        print("buzz");
    else:
        print(x);