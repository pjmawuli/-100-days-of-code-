fruits = ["apple", "banana", "orange"]

# Catch the exception and make sure the code runs without crashing

# My solution to the problem
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
#
# try:
#     make_pie(2)
# except IndexError:
#     print("Fruits pie")


# Angela's solution

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruits pie")
    else:
        print(f"{fruit} pie")

make_pie(9)