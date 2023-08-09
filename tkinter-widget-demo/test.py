from tkinter import *

window = Tk()
window.title("test")
window.minsize(width=400, height=400)
window.config(padx=20, pady=40)

label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1, column=2)

# new button
button2 = Button(text="I'm button2", command=action)
button2.grid(row=0, column=3)

# entry
entry = Entry(width=50)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(row=3, column=4)

window.mainloop()
