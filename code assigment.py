number = int(input("Hello, type in a number: "))
sum = 0

for x in range(1, number + 1):
    factor_count = 0
    for c in range(1, x + 1):
        if x % c == 0:
            factor_count += 1
    if factor_count == 2:
        sum += c
        print(x)

print(f"The sum of the prime numbers below {number} is {sum}.")

