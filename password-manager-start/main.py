from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for char in range(nr_letters)]
    password_list += [choice(symbols) for char in range(nr_symbols)]
    password_list += [choice(numbers) for char in range(nr_numbers)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# empty_file = open("password_manager.txt", mode="x")


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if not website:
        messagebox.showerror(title="Error", message="the website field is empty!")
    elif not email:
        messagebox.showerror(title="Error", message="the email field is empty!")
    elif not password:
        messagebox.showerror(title="Error", message="the password field is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you entered:\nWebsite: {website}\nemail:"
                                               f" {email}\npassword: {password}\nAre you sure you want to save?")

        if is_ok:
            format_data = f"{website} |{email} |{password}"
            with open("password_manager.txt", mode="a") as password_file:
                password_file.write(f"{format_data}\n")
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "essalhi12345@gmail.com")
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
# embed the image into the canvas
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# using a label to display image
# label = Label()
# image = PhotoImage(file='logo.png')
# label['image'] = image
# label.pack()

# row1
web_label = Label(text="website:")
web_entry = Entry(width=35)
web_entry.focus()
# web_entry.insert(END, "insert your website here")
web_label.grid(row=1, column=0)
web_entry.grid(row=1, column=1, columnspan=2)
# row2
email_label = Label(text="Email/Username:")
email_entry = Entry(width=35)
email_entry.insert(0, "essalhi12345@gmail.com")
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
# row3
pass_label = Label(text="Password:")
pass_entry = Entry(width=21)
# pass_entry.config(show="*")
generate_pass_button = Button(text="Generate Password", command=generate_password)
pass_label.grid(row=3, column=0)
pass_entry.grid(row=3, column=1)
generate_pass_button.grid(row=3, column=2)
# row4
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
