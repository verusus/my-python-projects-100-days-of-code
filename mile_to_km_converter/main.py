from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=100, height=50)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)


def convert():
    miles_value = float(entry.get())
    km_value = round(miles_value * 1.609, 2)
    label3.config(text=str(km_value))


# calls action() when pressed
button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)


window.mainloop()
