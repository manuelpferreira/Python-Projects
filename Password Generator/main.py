from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    auto_pass = "".join(password_list)
    password.delete(0, END)
    password.insert(0, auto_pass)
    pyperclip.copy(auto_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website.get()
    email_username_input = email_username.get()
    password_input = password.get()

    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: \nEmail: "
                                                                    f"{email_username_input} \nPassword: {password_input} "
                                                                    f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_input} | {email_username_input} | {password_input}\n")
                website.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)
label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)
label3 = Label(text="Password:")
label3.grid(column=0, row=3)

website = Entry(width=38)
website.grid(column=1, row=1, columnspan=2)
website.focus()

email_username = Entry(width=38)
email_username.grid(column=1, row=2, columnspan=2)
email_username.insert(0, "manuelpiresferreira@gmail.com")

password = Entry(width=21)
password.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
