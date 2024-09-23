import pyperclip
import os

# Global variables to store the content of the clipboard
ticket_content = ""
review_content = ""
authorization_code_27 = ""
authorization_code_1331 = ""
commit_message = ""

def capture_ticket():
    global ticket_content
    ticket_content = pyperclip.paste()
    output = f"""Ticket captured: {ticket_content}""" 
    print(output)

def capture_authorization_code_27():
    global authorization_code_27
    authorization_code_27 = pyperclip.paste()
    output = f"""Auth code for 2.7 captured: {authorization_code_27}""" 
    print(output)

def capture_authorization_code_1331():
    global authorization_code_1331
    authorization_code_1331 = pyperclip.paste()
    output = f"""Auth code for 1331 captured: {authorization_code_1331}"""
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
    print("1. Capture Ticket")
    print("2. Capture Auth Code for 2.7")
    print("3. Capture Auth Code for 1331")
    print("4. Capture Commit Message")
    print("5. Eclipse Message for 2.7")
    print("6. Console Command for 2.7")
    print("7. Eclipse Message for 1331")
    print("8. Console Command for 1331")
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
            capture_authorization_code_27()
        elif choice == "3":
            capture_authorization_code_1331()
        elif choice == "4":
            capture_commit_message()
        elif choice == "5":
            get_eclipse_msg(authorization_code_27)
        elif choice == "6":
            print_values(authorization_code_27)
        elif choice == "7":
            get_eclipse_msg(authorization_code_1331)
        elif choice == "8":
            print_values(authorization_code_1331)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
