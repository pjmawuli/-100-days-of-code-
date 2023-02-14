# Learning about python's unlimited function arguments

# *args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#
#
# add(5, 3, 7, 3, 8, 8)

# **Kwargs
def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
    # print(key, value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=4, multiply=4)


# Using **kwargs with classes and objects

class Wizard:
    def __init__(self, name, **kwargs):
        self.name = name
        self.house = kwargs.get("house")
        self.fav_subject = kwargs.get("fav_subject")
        self.pet_name = kwargs.get("pet_name")


harry = Wizard(name="harry")
print(harry.name, harry.pet_name)
