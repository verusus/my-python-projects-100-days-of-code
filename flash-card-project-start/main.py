from tkinter import *
import pandas as pd
import random
from pathlib import Path


# ----------------- Handling Data -----------------
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    pdf = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    pdf = pd.read_csv("data/french_words.csv")
finally:
    record_list_of_words_to_learn = pdf.to_dict(orient="records")


def update_data(record_to_delete_from_record_list):
    global record_list_of_words_to_learn
    record_list_of_words_to_learn.remove(record_to_delete_from_record_list)
    words_to_learn_df = pd.DataFrame(record_list_of_words_to_learn)
    filepath = Path('data/words_to_learn.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    words_to_learn_df.to_csv(filepath, index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)   # invalidate the last timer after a click
    # setting the image each time clicked
    canvas.itemconfig(card, image=card_front_img)
    # generate rand record
    current_card = random.choice(record_list_of_words_to_learn)
    rand_french_word = current_card["French"]    # record it's a dict raw
    canvas.itemconfig(title_item, text="French", fill="black")
    canvas.itemconfig(word_item, text=rand_french_word, fill="black")
    flip_timer = window.after(3000, flip_card)     # renew the timer


def i_know():
    global current_card
    update_data(current_card)
    next_card()


def flip_card():
    global current_card
    rand_english_word = current_card["English"]
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title_item, text="English", fill="white")
    canvas.itemconfig(word_item, text=rand_english_word, fill="white")
    window.after_cancel(flip_card)


# ----------------------- UI ------------------------------
window = Tk()
flip_timer = window.after(3000, flip_card)
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# creating the card as canvas
canvas = Canvas(height=526, width=800)   # canvas allow us to overlap thing on top of each others
card_front_img = PhotoImage(file="images/card_front.png")   # highlightthickness=0
card = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")

title_item = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_item = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, command=i_know)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
