import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_pass():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")  
            return
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))

        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_pass():
    password = entry_password.get()
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Success", "Password copied to clipboard.")


def exit_application():
    window.destroy()

window = tk.Tk()
window.title("Password Generator")
window.geometry("600x500")
label_title = tk.Label(window, text="Password Generator", font=("Arial", 24, "bold"), fg="blue")
label_title.pack(pady=20)

label_length = tk.Label(window, text="Password Length:", font=("Arial", 14))
label_length.pack(pady=10)

entry_length = tk.Entry(window, font=("Arial", 14))
entry_length.pack(pady=10)

label_password_text = tk.Label(window, text="Generated Password", font=("Arial", 14))
label_password_text.pack(pady=10)

entry_password = tk.Entry(window,font=("Arial", 14))
entry_password.pack(pady=10)

butt_bg_color = "lightblue"
butt_fg_color = "black"
butt_font = ("Arial", 14, "bold")
butt_width = 20
butt_padx = 10
butt_pady = 10

button_generate = tk.Button(window, text="Generate", font=butt_font, bg=butt_bg_color, fg=butt_fg_color, width=butt_width, padx=butt_padx, pady=butt_pady, command=generate_pass)
button_generate.pack(pady=10)

button_copy = tk.Button(window, text="Copy", font=butt_font, bg=butt_bg_color, fg=butt_fg_color, width=butt_width, padx=butt_padx, pady=butt_pady, command=copy_pass)
button_copy.pack(pady=10)

button_exit = tk.Button(window, text="Exit", font=butt_font, bg=butt_bg_color, fg=butt_fg_color, width=butt_width, padx=butt_padx, pady=butt_pady, command=exit_application)
button_exit.pack(pady=10)

window.mainloop()


