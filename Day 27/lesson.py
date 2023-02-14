# We are learning about tkinter a gui class for python

from tkinter import *

window = Tk()
window.title("My first Gui Program")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="Hola", font=("Arial", 24, "normal"))
my_label.pack()
my_label.pack(expand=0)
# my_label.config(text="Hello World")


# what happens when the button is clicked
def button_clicked():
    my_label.config(text=my_entry.get())


# Buttons
my_button = Button(text="Button", command=button_clicked)
my_button.pack()


# Entry
my_entry = Entry(width=10)
# add some text to begin with
my_entry.insert(END, string="type here")
my_entry.pack()


# TextBox
my_textbox = Text(width=50, height=25)
# puts cursor in textbox
my_textbox.focus()
# some text to begin with
my_textbox.insert(END, "Starting text")
# we're getting the text in the textbox
text_box_in = my_textbox.get("1.0", END)
print(text_box_in)
my_textbox.pack()


# Spinbox

# function to return the values from the spinbox
def get_spin():
    print(my_spinbox.get())


my_spinbox = Spinbox(from_=0, to=10, width=5, command=get_spin)
my_spinbox.pack()


# Scale

# function to return the value on the current scale

def get_scale(value):
    print(value)


my_scale = Scale(from_=0, to=50, command=get_scale)
my_scale.pack()


# CheckButton

def get_check_button():
    # Prints 1 if On_button checked else 0
    print(checked_state.get())


checked_state = IntVar()
my_checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=get_check_button)
checked_state.get()
my_checkbutton.pack()


# RadioButton

# returns the current state of the radio
def get_radio():
    print(radio_state.get())


radio_state = IntVar()
my_radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=get_radio)
my_radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=get_radio)
radio_state.get()
my_radiobutton1.pack()
my_radiobutton2.pack()


# ListBox

# a function to get the selected item in the list
def get_listbox(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Orange", "Banapple"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)
my_listbox.bind("<<ListboxSelect>>", get_listbox)
my_listbox.pack()

window.mainloop()

