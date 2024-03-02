import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def send_wish():
    name = name_entry.get()
    if name:
        messagebox.showinfo(title="Birthday Wishes", message=f"Happy Birthday, {name}!")
    else:
        messagebox.showwarning(title="Error", message="Please enter a name")

root = tk.Tk()
root.geometry("400x200")
root.title("Birthday Wishing App")

header_label = tk.Label(root, text="Enter Name:")
header_label.pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack()

send_button = tk.Button(root, text="Send Wishes", command=send_wish)
send_button.pack()

current_year = datetime.now().year

footer_label = tk.Label(root, text=f"© {current_year} Birthday Wishing App")
footer_label.pack(side="bottom")

root.mainloop()
