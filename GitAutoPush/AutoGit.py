import os
import subprocess
from datetime import datetime

def git_push():
    try:
        # Get the current time and date
        now = datetime.now()
        commit_time = now.strftime("%H:%M")
        commit_date = now.strftime("%d %m %Y")
        
        # Custom commit message
        commit_message = f"This file was pushed at time {commit_time} and date {commit_date} by MO"
        
        # Run Git commands
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        
        print("Files have been pushed to GitHub successfully.")
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
