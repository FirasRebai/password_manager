import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import os


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().lower()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                "email": email,
                "password": password
            }
    }

    if len(website) == 0 or len(password) == 0:
        alert = messagebox.showwarning(title="oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- Find Password ------------------------------- #

def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            # print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            website_email = data[website]["email"]
            website_password = data[website]["password"]
            alert = messagebox.showwarning(title=website,
                                           message=f"Email: {website_email} \n Password: {website_password} ")
        else:
            alert = messagebox.showwarning(title="Error",
                                           message=f"No Data for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    # print(nr_letters)
    # print(nr_symbols)
    # print(nr_numbers)
    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # password_list = []

    # for n in range(1, nr_letters + 1):
    #     rcl = random.choice(letters)
    #     password_list.append(rcl)
    password_list_letters = [random.choice(letters) for letter in range(nr_letters)]
    # print(password_list_letters)
    # for n in range(1, nr_numbers + 1):
    #     rcn = random.choice(numbers)
    #     password_list.append(rcn)

    password_list_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    # for n in range(1, nr_symbols + 1):
    #     rcs = random.choice(symbols)
    #     password_list.append(rcs)

    password_list_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list = password_list_letters + password_list_numbers + password_list_symbols
    random.shuffle(password_list)
    pass_w = "".join(password_list)
    # for char in password_list:
    #     pass_w += char
    password_entry.insert(0, pass_w)
    pyperclip.copy(pass_w)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

generate_password_button = Button(text="Search", width=14, command=find_password)
generate_password_button.grid(column=2, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=51)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "random@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
