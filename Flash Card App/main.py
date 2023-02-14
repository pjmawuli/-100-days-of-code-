from tkinter import *
from pandas import *
from random import *
from tkinter import messagebox


# ---------------------------- THE SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = None
data = None
words = None
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
    words = data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

window = Tk()


# ---------------------------- THE LEARNING MECHANISM ------------------------------- #

# When the right button is pressed
def correct_btn_pressed():
    global words
    # removing the current card from the list that will be shown
    try:
        words.remove(current_card)
    except ValueError:
        messagebox.showinfo(message="You have run out of cards")
    else:
        # Creating a csv file from the new list
        words_to_learn = DataFrame(words)
        words_to_learn.to_csv("data/words_to_learn.csv")

        next_card()


# ---------------------------- RANDOM WORD MECHANISM ------------------------------- #


def next_card():
    global current_card
    try:
        current_card = choice(words)
    except IndexError:
        messagebox.showinfo(message="You've run out of cards to learn")
    else:
        title = "French"
        word = current_card['French']
        canvas.itemconfig(card_set, image=card_f_png)
        canvas.itemconfig(title_text, text=title, fill="black")
        canvas.itemconfig(word_text, text=word, fill="black")
        show_answer()


def flip_card(translation):
    canvas.itemconfig(card_set, image=card_b_png)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=translation, fill="white")
    window.after_cancel(timer)


# ---------------------------- THE TIME MECHANISM ------------------------------- #

def show_answer():
    global timer
    global current_card
    translation = current_card["English"]
    timer = window.after(3000, flip_card, translation)


# ---------------------------- UI SETUP ------------------------------- #
window.config(height=500, width=500, bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Flashy")

# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# canvas photo
card_f_png = PhotoImage(file="images/card_front.png")
card_b_png = PhotoImage(file="images/card_back.png")
card_set = canvas.create_image(400, 266, image=card_f_png)
# canvas text
title_text = canvas.create_text(400, 180, text="", fill="black", font=("Arial", 35, "normal"))
word_text = canvas.create_text(400, 260, text="", fill="black", font=("Arial", 50, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                   command=correct_btn_pressed)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1, column=1)

# Functions to run before mainloop is called
next_card()

window.mainloop()
