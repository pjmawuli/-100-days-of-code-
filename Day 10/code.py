sum = 0

while True:
    number = int(input("Enter a number: "))

    if number < 0:
        break

    sum += number

print(sum)
