import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = length_scale.get()
    use_upper = upper_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"

    try:
        password = "".join(random.choice(chars) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        update_strength(length, use_upper, use_numbers, use_symbols)
    except IndexError:
        pass

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard! 📋")
    else:
        messagebox.showwarning("Warning", "Generate a password first!")

def update_strength(length, upper, nums, syms):
    score = 0
    if length >= 12: score += 1
    if length >= 16: score += 1
    if upper: score += 1
    if nums: score += 1
    if syms: score += 1

    if score >= 5:
        lbl_strength.config(text="Strength: 🔥 UNBREAKABLE", fg="green")
    elif score >= 3:
        lbl_strength.config(text="Strength: ✅ STRONG", fg="#2ecc71")
    else:
        lbl_strength.config(text="Strength: ⚠️ WEAK", fg="red")


root = tk.Tk()
root.title("Tayronuk PassGen v1.0")
root.geometry("400x450")
root.resizable(False, False)

tk.Label(root, text="🔐 Tayronuk PassGen", font=("Helvetica", 18, "bold"), pady=10).pack()

frame_settings = tk.Frame(root)
frame_settings.pack(pady=10)

tk.Label(frame_settings, text="Password Length:").grid(row=0, column=0, columnspan=2)
length_scale = tk.Scale(frame_settings, from_=8, to=32, orient=tk.HORIZONTAL, length=200)
length_scale.set(12)
length_scale.grid(row=1, column=0, columnspan=2, pady=5)

upper_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame_settings, text="Include Uppercase (A-Z)", variable=upper_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame_settings, text="Include Numbers (0-9)", variable=numbers_var).grid(row=3, column=0, sticky="w")
tk.Checkbutton(frame_settings, text="Include Symbols (!@#$)", variable=symbols_var).grid(row=4, column=0, sticky="w")

btn_generate = tk.Button(root, text="⚡ GENERATE PASSWORD", font=("Arial", 10, "bold"), bg="#3498db", fg="white", command=generate_password)
btn_generate.pack(pady=15, fill="x", padx=40)

entry_password = tk.Entry(root, font=("Courier", 14), justify="center", bd=2)
entry_password.pack(pady=5, padx=20, fill="x")

lbl_strength = tk.Label(root, text="Strength: -", font=("Arial", 9))
lbl_strength.pack()

btn_copy = tk.Button(root, text="📋 Copy to Clipboard", command=copy_to_clipboard)
btn_copy.pack(pady=10)

tk.Label(root, text="Built by Tayronuk", fg="gray", font=("Arial", 8)).pack(side="bottom", pady=10)

root.mainloop()