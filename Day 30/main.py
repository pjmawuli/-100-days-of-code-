# FileNotFound Error
# with open("hello.txt", mode="r") as file:
#     file.read()

# KeyError Error
# my_dict = {"key": "value"}
# print(my_dict["non_existent_key"])

# IndexError Error
# my_list = [1, 2, 3, 4, 5]
# print(my_list[9])

# Type Error
# name = "Julio"
# print("Julio" + 44)

# Learning about Try, Except, Else, and Finally
# try:
#     file = open("test_file.txt", mode="r")
#
# except FileNotFoundError as missing_file:
#     print(f"Sorry the file {missing_file.filename} wasn't found.")
#     print(f"so we made you a new one")
#     file = open("test_file.txt", mode="w")
#     file.write("Hello Kooonnnniichhiiiiwaaaaaaaa")
#
# else:
#     print("We are O.K")
#
# finally:
#     file.close()

# Learning about raising errors
# BMI CALCULATOR

# height = int(input("How tall are you? in meters\n"))
# weight = int(input("How heavy are you? in kilograms\n"))
#
# if height > 3:
#     raise ValueError(f"Really {height} meters?")
#
# bmi = weight/ height ** 2
# print(bmi)

