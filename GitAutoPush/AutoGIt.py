import tkinter as tk
from tkinter import messagebox
import os
import datetime

def git_operations():
    try:
        now = datetime.datetime.now()
        commit_message = f"This file was pushed at {now.strftime('%H:%M:%S')} on {now.strftime('%Y-%m-%d')} by me"
        os.system("git add .")
        os.system(f'git commit -m "{commit_message}"')
        os.system("git push")
        messagebox.showinfo("Success", "Changes pushed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Git Automation Tool")
root.geometry("400x300")

# Logo
logo = tk.PhotoImage(file="logo.png")  # Add your logo file
tk.Label(root, image=logo).pack()

# Button
push_button = tk.Button(root, text="Push Changes", command=git_operations, font=("Arial", 14))
push_button.pack(pady=20)

root.mainloop()
