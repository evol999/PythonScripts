import pyperclip
import os
import sys

# Global variables
file_paths = []
stash_name = ""

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 30)
    print("Git Stash Command Generator")
    print("=" * 30)
    print("1. Capture File Paths (from clipboard)")
    print("2. Enter Stash Name (message)")
    print("3. Generate Git Stash Command")
    print("0. Exit")
    print("=" * 30)

def capture_paths():
    """Capture file paths from clipboard."""
    global file_paths
    clipboard_content = pyperclip.paste().strip()
    if not clipboard_content:
        print("Clipboard is empty!")
        return
    
    file_paths = [line.strip() for line in clipboard_content.split('\n') if line.strip()]
    print(f"Captured {len(file_paths)} file path(s):")
    for path in file_paths:
        print(f"  - {path}")

def capture_stash_name():
    """Capture stash name (message) from user input."""
    global stash_name
    stash_name = input("Enter a name/description for the stash: ").strip()
    print(f"Stash name set to: '{stash_name}'")

def get_git_command():
    """Generate and copy the git stash command."""
    if not file_paths:
        print("No file paths captured! Use Option 1 first.")
        return
    
    stash_command = f"git stash push -m \"{stash_name}\" -- {' '.join(file_paths)}" if stash_name \
                    else f"git stash push -- {' '.join(file_paths)}"
    
    pyperclip.copy(stash_command)
    print("\nGit stash command generated and copied to clipboard:")
    print(stash_command)
    print("\nPaste it in your terminal to execute.")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")
        clear_screen()

        if choice == "1":
            capture_paths()
        elif choice == "2":
            capture_stash_name()
        elif choice == "3":
            get_git_command()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()