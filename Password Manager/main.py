from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.extend([choice(letters) for char in range(randint(8, 10))])
    password_list.extend([choice(symbols) for symb in range(randint(2, 4))])
    password_list.extend([choice(numbers) for num in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_e.delete(0, END)
    password_e.insert(END, password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_e.get()
    website = website.lower()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

            password = data[website]["password"]
            email = data[website]["email"]

    except FileNotFoundError:
        messagebox.showinfo(message="Sorry, you have not saved any passwords yet.")
    except KeyError:
        messagebox.showinfo(message="Sorry, there are no passwords/emails saved under this website")

    else:
        messagebox.showinfo(message=f"Email: {email},\nPassword: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_e.get()
    website = website.lower()
    email = email_us_e.get()
    password = password_e.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(message="Sorry you cant leave any spaces blank. Please fill everything")

    else:
        try:
            # first let's try reading from the json file
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                # Now let's update it
                data.update(new_data)

        except FileNotFoundError:
            # If the json file doesn't already exist
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # If our try block works
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_e.delete(0, END)
            password_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window configuration
window = Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")

# Canvas config
canvas = Canvas(width=200, height=200, bg="white", highlightbackground="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels config
website_l = Label(text="Website:", font=("Arial", 15, "normal"), fg="black", bg="white")
website_l.grid(row=1, column=0)

email_us_l = Label(text="Email/Username:", font=("Arial", 15, "normal"), fg="black", bg="white")
email_us_l.grid(row=2, column=0)

password_l = Label(text="Password:", font=("Arial", 15, "normal"), fg="black", bg="white")
password_l.grid(row=3, column=0)

# Entry config
website_e = Entry(width=21, bg="white", fg="black", highlightbackground="white")
website_e.focus()
website_e.grid(row=1, column=1)

email_us_e = Entry(width=38, bg="white", fg="black", highlightbackground="white")
email_us_e.insert(END, "padijnmm@gmail.com")
email_us_e.grid(row=2, column=1, columnspan=2)

password_e = Entry(width=21, bg="white", fg="black", highlightbackground="white")
password_e.grid(row=3, column=1)

# Button config
gen_pass_b = Button(text="Generate Password", bg="white", fg="black", highlightbackground="white", command=generate)
gen_pass_b.grid(row=3, column=2)

add_b = Button(text="Add", bg="white", fg="black", highlightbackground="white", width=36, command=save)
add_b.grid(row=4, column=1, columnspan=2)

search_b = Button(text="Search", bg="white", fg="black", highlightbackground="white", width=13, command=find_password)
search_b.grid(row=1, column=2)

window.mainloop()
