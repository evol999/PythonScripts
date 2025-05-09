import pyperclip
import os

# Global variables to store the content of the clipboard
ticket_content = ""
review_content = ""
authorization_code = ""
commit_message = ""

def capture_ticket():
    global ticket_content
    ticket_content = pyperclip.paste()
    output = f"""Ticket captured: {ticket_content}""" 
    print(output)

def capture_authorization_code():
    global authorization_code
    authorization_code = pyperclip.paste()
    output = f"""Auth code captured: {authorization_code}""" 
    print(output)

def capture_commit_message():
    global commit_message
    commit_message = pyperclip.paste()
    output = f"""Commit message captured: {commit_message}"""
    print(output)

def print_values(authorization_code):
    if commit_message != "":
        output = f"""svn commit -m "#{ticket_content} Fix for {commit_message} @{authorization_code}" """
    else:
        output = f"""svn commit -m "#{ticket_content} @{authorization_code}" """
    pyperclip.copy(output)
    print(output)

def get_eclipse_msg(authorization_code):
    if commit_message != "":
        output = f"""#{ticket_content} Fix for {commit_message} @{authorization_code} """
    else:
        output = f"""#{ticket_content} @{authorization_code} """
    pyperclip.copy(output)
    print(output)

def display_menu():
    print("Menu:")
    print("1. Capture Ticket number")
    print("2. Capture Ticket title")
    print("3. Capture Auth Code")
    print("4. Generate Eclipse Message")
    print("5. Generate console Command")
    print("0. Exit")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and Mac
    else:
        os.system('clear')

def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")
        clear_screen()

        if choice == "1":
            capture_ticket()
        elif choice == "2":
            capture_commit_message()
        elif choice == "3":
            capture_authorization_code()
        elif choice == "4":
            get_eclipse_msg(authorization_code)
        elif choice == "5":
            print_values(authorization_code)
        elif choice == "6":
            print_values(authorization_code)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
