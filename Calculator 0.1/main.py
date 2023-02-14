from tkinter import *

# The window of the calculator
window = Tk()
window.title("Calculator 0.1")
window.config(padx=20, pady=20)
text = ""
first_variable = None
second_variable = None
operation = None


# ------------------------------- OPERATION FUNCTIONALITY ----------------------------------#
def premature_operation():
    global first_variable
    global second_variable
    global text
    global operation

    first_variable = perform_operation(first_variable, second_variable, operation)
    second_variable = None
    text = str(first_variable)
    result_l.config(text=text)


def perform_operation(num1, num2, operand):
    if operand == "add":
        answer = num1 + num2
    if operand == "sub":
        answer = num1 - num2
    if operand == "div":
        answer = num1 / num2
    if operand == "prod":
        answer = num1 * num2

    return answer


# ------------------------------- STORING FUNCTIONALITY ----------------------------------#

def variable_check(var):
    global first_variable
    global second_variable
    global text

    if first_variable is None:
        first_variable = var
        text += var
        result_l.config(text=text)
        first_variable = int(first_variable)

    elif operation is None:
        first_variable = str(first_variable)
        first_variable += var
        text += var
        result_l.config(text=text)
        first_variable = int(first_variable)

    elif second_variable is None:
        second_variable = var
        text += var
        result_l.config(text=text)
        second_variable = int(second_variable)

    elif second_variable is not None:
        second_variable = str(second_variable)
        second_variable += var
        text += var
        result_l.config(text=text)
        second_variable = int(second_variable)


# ------------------------------- BUTTON FUNCTIONALITY ----------------------------------#

# The numbers
def one_pressed():
    variable_check("1")


def two_pressed():
    variable_check("2")


def three_pressed():
    variable_check("3")


def four_pressed():
    variable_check("4")


def five_pressed():
    variable_check("5")


def six_pressed():
    variable_check("6")


def seven_pressed():
    variable_check("7")


def eight_pressed():
    variable_check("8")


def nine_pressed():
    variable_check("9")


def zero_pressed():
    variable_check("0")


# The operations
def del_pressed():
    global text
    global first_variable
    global second_variable
    global operation
    text = ""
    first_variable = None
    second_variable = None
    operation = None

    result_l.config(text=text)


def add_pressed():
    global text
    global operation

    if operation is None:
        text += "➕"
        operation = "add"
    else:
        premature_operation()
        operation = "add"
        text += "➕"

    result_l.config(text=text)


def sub_pressed():
    global text
    global operation

    if operation is None:
        text += "➖"
        operation = "sub"
    else:
        premature_operation()
        operation = "sub"
        text += "➖"

    result_l.config(text=text)


def prod_pressed():
    global text
    global operation

    if operation is None:
        text += "✖️"
        operation = "prod"
    else:
        premature_operation()
        operation = "prod"
        text += "✖️"

    result_l.config(text=text)


def div_pressed():
    global text
    global operation

    if operation is None:
        text += "➗️"
        operation = "div"
    else:
        premature_operation()
        operation = "div"
        text += "➗️"

    result_l.config(text=text)


def equal_pressed():
    global text
    global first_variable
    global second_variable
    global operation

    result = perform_operation(first_variable, second_variable, operation)

    result_l.config(text=result)


# ------------------------------- THE GUI ----------------------------------#

# Labels
result_l = Label(text=text, height=3, width=23, bg="white", fg="black", font=("Arial", 24, "normal"), )
result_l.grid(row=0, column=0, columnspan=4)

# Buttons

# The numbers
seven_btn = Button(text="7", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                   command=seven_pressed)
seven_btn.grid(row=1, column=0)
print(seven_btn)

eight_btn = Button(text="8", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                   command=eight_pressed)
eight_btn.grid(row=1, column=1)

nine_btn = Button(text="9", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                  command=nine_pressed)
nine_btn.grid(row=1, column=2)

four_btn = Button(text="4", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                  command=four_pressed)
four_btn.grid(row=2, column=0)

five_btn = Button(text="5", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                  command=five_pressed)
five_btn.grid(row=2, column=1)

six_btn = Button(text="6", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2, command=six_pressed)
six_btn.grid(row=2, column=2)

one_b = Button(text="1", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2, command=one_pressed)
one_b.grid(row=3, column=0)

two_btn = Button(text="2", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2, command=two_pressed)
two_btn.grid(row=3, column=1)

three_btn = Button(text="3", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                   command=three_pressed)
three_btn.grid(row=3, column=2)

zero_btn = Button(text="0", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                  command=zero_pressed)
zero_btn.grid(row=4, column=0)

# The operations
div_btn = Button(text="➗", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2, command=div_pressed)
div_btn.grid(row=4, column=3)

prod_btn = Button(text="✖️", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                  command=prod_pressed)
prod_btn.grid(row=3, column=3)

add_btn = Button(text="➕", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2, command=add_pressed)
add_btn.grid(row=4, column=1)

sub_btn = Button(text="➖", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2, command=sub_pressed)
sub_btn.grid(row=4, column=2)

equ_btn = Button(text="🟰", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                 command=equal_pressed)
equ_btn.grid(row=2, column=3)

del_btn = Button(text="DEL", bg="white", fg="black", width=4, font=("Arial", 20, "normal"), height=2,
                 command=del_pressed)
del_btn.grid(row=1, column=3)

window.mainloop()
