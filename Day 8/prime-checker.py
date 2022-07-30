def prime_checker(number):
    factor_count = 0
    for x in range(1, number + 1):
        if number % x == 0:
            factor_count += 1
    if factor_count == 2:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number = n)