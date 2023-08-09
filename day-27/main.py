from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

# my_label["text"] = "new text"


def click():
    phrase = input.get()
    my_label.config(text=phrase)

# button
button = Button(text="Click me", command=click)
button.pack()

input = Entry(width=20)
input.pack()


window.mainloop()
