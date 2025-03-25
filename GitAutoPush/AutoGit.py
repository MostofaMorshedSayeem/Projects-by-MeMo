import os
import subprocess
from datetime import datetime
import tkinter as tk
from threading import Timer

def show_congratulations_screen():
    # Create a tkinter window
    root = tk.Tk()
    root.title("Congratulations")
    root.geometry("300x150")
    
    # Add a label
    label = tk.Label(root, text="🎉 Files pushed successfully to GitHub! 🎉", font=("Helvetica", 12), wraplength=280, justify="center")
    label.pack(expand=True)
    
    # Close the window after 8 seconds
    Timer(8.0, root.destroy).start()
    root.mainloop()

def git_push():
    try:
        # Get the current time, date, and day of the week
        now = datetime.now()
        commit_time = now.strftime("%H:%M")
        commit_date = now.strftime("%d-%m-%Y")  # Enhanced date format
        day_of_week = now.strftime("%A")
        
        # Enhanced commit message
        commit_message = f"Files pushed by MO on {day_of_week}, {commit_date} at {commit_time}"
        
        # Run Git commands
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        
        print("Files have been pushed to GitHub successfully.")
        
        # Show the congratulations screen
        show_congratulations_screen()
        
        # Exit the script automatically after 8 seconds
        Timer(8.0, os._exit, args=(0,)).start()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

if __name__ == "__main__":
    # Check if the current directory is a Git repository
    if not os.path.exists(".git"):
        print("Error: Current directory is not a Git repository.")
    else:
        git_push()
