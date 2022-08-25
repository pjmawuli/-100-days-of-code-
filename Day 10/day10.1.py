# Python Functions with outputs
first_name = input("Hello what's your first name?: ")
last_name = input("And your last name?: ")


def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name


print(format_name(first_name, last_name))