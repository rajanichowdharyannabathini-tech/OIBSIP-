import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if number_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        # Password Strength
        if length < 8:
            strength_label.config(text="Strength: Weak", fg="red")
        elif length < 12:
            strength_label.config(text="Strength: Medium", fg="orange")
        else:
            strength_label.config(text="Strength: Strong", fg="green")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")


# Copy Password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(root, text="PASSWORD GENERATOR", font=("Arial", 18, "bold"))
title.pack(pady=10)

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()

length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var).pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var).pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Numbers", variable=number_var).pack(anchor="w", padx=100)
tk.Checkbutton(root, text="Special Characters", variable=symbol_var).pack(anchor="w", padx=100)

tk.Button(root, text="Generate Password", command=generate_password,
          bg="green", fg="white", font=("Arial", 12)).pack(pady=15)

password_entry = tk.Entry(root, width=35, font=("Arial", 12), justify="center")
password_entry.pack()

tk.Button(root, text="Copy Password", command=copy_password,
          bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()

root.mainloop()