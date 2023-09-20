import tkinter as tk
from tkinter import messagebox
import random
import string

def password():
    length = int(l_entry.get())

    use_digits = d_var.get()
    use_special_chars = special_char_var.get()

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()' if use_special_chars else ''

    all_characters = lowercase_letters + uppercase_letters + digits + special_chars

    password = ''.join(random.choice(all_characters) for _ in range(length))
    pas_entry.delete(0, tk.END)
    pas_entry.insert(0, password)

def generate_password_button():
    try:
        password()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")
app = tk.Tk()
app.title("Password Generator")

l_label = tk.Label(app, text="Password Length:")
l_label.pack()
l_entry = tk.Entry(app)
l_entry.pack()

d_var = tk.IntVar()
d_checkbox = tk.Checkbutton(app, text="Include Digits", variable=d_var)
d_checkbox.pack()

special_char_var = tk.IntVar()
special_char_checkbox = tk.Checkbutton(app, text="Include Special Characters", variable=special_char_var)
special_char_checkbox.pack()


generate_button = tk.Button(app, text="Generate Password", command=generate_password_button)
generate_button.pack()


password_label = tk.Label(app, text="Generated Password:")
password_label.pack()
pas_entry = tk.Entry(app)
pas_entry.pack()


app.mainloop()
