# Calculates the sum of all even numbers from 1 to 100 inclusive

total = 0;
for x in range(0, 101, 2):
    total = total + x;

print(total);