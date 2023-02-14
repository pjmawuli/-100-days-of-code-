from tkinter import *

window = Tk()
window.config(width=400, height=200, pady=40, padx=40)

# EntryWidget for miles
mile_entry = Entry(width=10)
mile_entry.grid(row=0, column=1)

# LabelWidget for miles entry
mile_label = Label(font=("Arial", 15, "normal"), text="miles")

# Label for second column of the grid
label_c1 = Label(text="Is equal to", font=("Arial", 15, "normal"))
label_c1.grid(row=1, column=0)

result_label = Label(text=0, font=("Arial", 15, "normal"))
result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 15, "normal"))
km_label.grid(row=1, column=2)


# The calculate function
def calculate():
    result_label.config(text=round(float(mile_entry.get()) * 1.6, 2))


# The calculate button to perform the calculation
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(row=2, column=1)


mile_label.grid(row=0, column=2)
window.mainloop()