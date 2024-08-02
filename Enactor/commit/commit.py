import pyperclip

# Global variables to store the content of the clipboard
ticket_content = ""
review_content = ""
authorization_code_27 = ""
authorization_code_RCX = ""
commit_message = ""

def capture_ticket():
    global ticket_content
    ticket_content = pyperclip.paste()
    print("Ticket captured and stored in the clipboard.")

def capture_authorization_code_27():
    global authorization_code_27
    authorization_code_27 = pyperclip.paste()
    print("Authorization code for 2.7 captured and stored in the clipboard.")

def capture_authorization_code_RCX():
    global authorization_code_RCX
    authorization_code_RCX = pyperclip.paste()
    print("Authorization code for RCX captured and stored in the clipboard.")

def capture_commit_message():
    global commit_message
    commit_message = pyperclip.paste()
    print("Commit message captured and stored in the clipboard.")

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
    print("2. Capture Authorization Code for 2.7")
    print("3. Capture Authorization Code for RCX")
    print("4. Capture Commit Message")
    print("5. Get Message For Eclipse for 2.7")
    print("6. Print Console Command for 2.7")
    print("7. Get Message For Eclipse for RCX")
    print("8. Print Console Command for RCX")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            capture_ticket()
        elif choice == "2":
            capture_authorization_code_27()
        elif choice == "3":
            capture_authorization_code_RCX()
        elif choice == "4":
            capture_commit_message()
        elif choice == "5":
            get_eclipse_msg(authorization_code_27)
        elif choice == "6":
            print_values(authorization_code_27)
        elif choice == "7":
            get_eclipse_msg(authorization_code_RCX)
        elif choice == "8":
            print_values(authorization_code_RCX)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
