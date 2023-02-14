from tkinter import *

window = Tk()
window.minsize(height=300, width=500)
window.title("My first GUI program")
window.config(padx=60, pady=60)

# Label
my_label = Label(text="Label", pady=20, padx=20)
my_label.grid(row=0, column=0)
# Buttons
button1 = Button(text="Button1", pady=20)
button1.grid(row=1, column=1)

button2 = Button(text="Button2", padx=20, pady=20)
button2.grid(row=0, column=2)
# Entry
my_entry = Entry(width=15)
my_entry.insert(END, "Starting text")
my_entry.grid(row=3, column=3)

window.mainloop()
