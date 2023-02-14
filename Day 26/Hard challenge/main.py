with open("file1.txt") as data_1:
    first_list = [num.strip() for num in data_1]
    print(first_list)
with open("file2.txt") as data_2:
    second_list = [num.strip() for num in data_2]
    print(second_list)

result = [int(num) for num in first_list if num in second_list]
print(result)

# Write your code above 👆

# print(result)


