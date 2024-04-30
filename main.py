from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for x in range(nr_letters)]
    password_numbers = [random.choice(numbers) for x in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for x in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_file():
    web = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if not web or not password:
        if not web:
            messagebox.showerror(title="Missing Website", message="You didnt enter a website")
        if not password:
            messagebox.showerror(title="missing Password", message="You didnt enter a password")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} "
                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            file = open("pw.txt", "a")
            file.write(f"{web} | {email} | {password}\n")
            file.close()
            web_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("The Vault")
window.config(padx=50, pady=50, bg='#695E93')


canvas = Canvas(width=200, height=200, bg='#695E93', highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels, Website, username, password
web_label = Label(bg='#695E93', fg='#003366', text="Website:")
user_label = Label(bg='#695E93', fg='#003366', text="Username/E-Mail:")
pass_label = Label(bg='#695E93', fg='#003366', text="Password:")
web_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)
# entry for three labels

web_entry = Entry(bg="#ffaa00", width=35)
user_entry = Entry(bg="#ffaa00", width=35)
user_entry.insert(0,"foo@e.mail")
pass_entry = Entry(bg="#ffaa00", width=21)
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")
user_entry.grid(row=2, column=1, columnspan=2, sticky="w")
pass_entry.grid(row=3, column=1, sticky="w")
#buttons, generate password, add
gen_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=add_to_file)
gen_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
