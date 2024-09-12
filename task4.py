import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({'Name': name, 'Phone':phone, 'Email': email, 'Address': address})
        messagebox.showinfo("Success","Contact added successfully!")
        clear_entries()
        display_contacts()

    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields. ")

def display_contacts():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")    

def search_contact():
    search_term = entry_search.get()
    listbox_contacts.delete(0, tk.END)

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            listbox_contacts.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def update_contact():
    selected_index = listbox_contacts.curselection()

    if selected_index:
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()


        if name and phone:
            contacts[selected_index[0]] = {'Name': name, 'Phone' : phone, 'Email':email, 'Address': address}
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_entries()
            display_contacts()

        else:
            messagebox.showwarning("Input Error","Name and Phone are required fields.")

    else:
        messagebox.showwarning("Selection Error","Please select a contact to update.")

def delete_contact():
    selected_index = listbox_contacts.curselection()

    if selected_index:
        del contacts[selected_index[0]]
        messagebox.showinfo("Success","Contact deleted successfully!")
        display_contacts()
    else:
        messagebox.showwarning("Selection Error","Please select a contact to delete.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


window = tk.Tk()
window.title("Contact Book")
window.geometry("850x650")
window.config(bg="#f0f8ff")

title_font = Font(family="Arial", size=25, weight="bold", slant="italic")
label_font = Font(family="Helvetica", size=12, weight="bold")
button_font = Font(family="Helvetica", size=14, weight="bold")

title_label = tk.Label(window, text="CONTACT BOOK", font=title_font, bg="#f0f8ff", fg="steelblue")
title_label.pack(pady=20)

frame_main = tk.Frame(window, bg="#f0f8ff")
frame_main.pack(fill=tk.BOTH, expand=True)

frame_left = tk.Frame(frame_main, bg="#f0f8ff", width=400)
frame_left.pack(side=tk.LEFT, padx=20, pady=10, fill=tk.Y, expand=True)

tk.Label(frame_left, text="Name", font=label_font, bg="#f0f8ff").pack(pady=5)
entry_name = tk.Entry(frame_left, font=label_font)
entry_name.pack(pady=5)

tk.Label(frame_left, text="Phone", font=label_font, bg="#f0f8ff").pack(pady=5)
entry_phone = tk.Entry(frame_left, font=label_font)
entry_phone.pack(pady=5)

tk.Label(frame_left, text="Email", font=label_font, bg="#f0f8ff").pack(pady=5)
entry_email = tk.Entry(frame_left, font=label_font)
entry_email.pack(pady=5)

tk.Label(frame_left, text="Address", font=label_font, bg="#f0f8ff").pack(pady=5)
entry_address = tk.Entry(frame_left, font=label_font)
entry_address.pack(pady=5)

frame_buttons = tk.Frame(frame_left, bg="#f0f8ff")
frame_buttons.pack(pady=20)

tk.Button(frame_buttons, text="Add Contact", command=add_contact,font=button_font, bg="#87cefa", width=15, height=2).pack(pady=10)
tk.Button(frame_buttons, text="Update Contact", command=update_contact,font=button_font, bg="#87cefa", width=15, height=2).pack(pady=10)
tk.Button(frame_buttons, text="Delete Contact", command=delete_contact,font=button_font, bg="#87cefa", width=15, height=2).pack(pady=10)

frame_right = tk.Frame(frame_main, bg="#f0f8ff", width=400)
frame_right.pack(side=tk.RIGHT, padx=20, pady=10, fill=tk.BOTH, expand=True)

tk.Label(frame_right, text="Search by name or Phone:", font=label_font, bg="#f0f8ff").pack(pady=5)
entry_search = tk.Entry(frame_right, font=label_font)
entry_search.pack(pady=5)
tk.Button(frame_right, text="Search", command=search_contact, bg="#87cefa",font=button_font, width=15, height=2).pack(pady=10)

listbox_contacts = tk.Listbox(frame_right, height=30, width=60, font=label_font)
listbox_contacts.pack(pady=10, expand=True)

display_contacts()

window.protocol("WM_DELETE_WINDOW", window.quit)

window.mainloop()




 
