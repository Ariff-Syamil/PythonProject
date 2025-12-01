from tkinter import *
from tkinter import messagebox
import random, pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_join = password_letters + password_symbols + password_numbers
    random.shuffle(password_join)
    password_create = "".join(password_join)

    pyperclip.copy(password_create)

    password_entry.delete(0, END)
    password_entry.insert(0, password_create)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_data = website_entry.get().title()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops",
                                    message="Please dont leave the field empty!")

    else:
        asked = messagebox.askokcancel(title="Do you wanna save this password?",
                            message= f"Are you sure you want\n"
                                     f" to save your data as: \n\n"
                                       f"Website: {website_data}\n"
                                     f"Email/Username: {email_data}\n"
                                     f"Password: {password_data}\n")
        if asked:
            new_data = {
                website_data:{
                    "email":email_data,
                    "password":password_data,
                }
            }
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search_website():
    website_search = website_entry.get().title()
    if len(website_search) > 0:
        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)
                website_found = data[website_search]
        except FileNotFoundError:
            messagebox.showinfo(title="Error",
                                message="No data found for this website, "
                                        "please create one.")
        except KeyError:
            messagebox.showinfo(title="Error",
                                message="Password not found for this website, "
                                        "please create one.")
        else:
            email_found = website_found["email"]
            password_found = website_found["password"]

            messagebox.showinfo(title=f"{website_search}",
                                message=f"Email: {email_found}\n"
                                        f"Password: {password_found}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
locker = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=locker)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"mohdsyamil95@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

search_button = Button(width=14, text="Search", command=search_website)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
save_button = Button(width=44, text="Add", command=save_password)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()