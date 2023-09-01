import pyperclip

# Global variables to store the content of the clipboard
ticket_content = ""
review_content = ""
authorization_code = ""
commit_message = ""

def capture_ticket():
    global ticket_content
    ticket_content = pyperclip.paste()
    print("Ticket captured and stored in the clipboard.")

def capture_review():
    global review_content
    review_content = pyperclip.paste()
    print("Review captured and stored in the clipboard.")

def capture_authorization_code():
    global authorization_code
    authorization_code = pyperclip.paste()
    print("Authorization code captured and stored in the clipboard.")

def capture_commit_message():
    global commit_message
    commit_message = pyperclip.paste()
    print("Commit message captured and stored in the clipboard.")

def print_values():
    if commit_message != "":
        output = f"""svn commit -m "#{ticket_content} Fix for {commit_message} @{authorization_code}" """
    else:
        output = f"""svn commit -m "#{ticket_content} @{authorization_code}" """
    pyperclip.copy(output)
    print(output)

def display_menu():
    print("Menu:")
    print("1. Capture Ticket")
    print("2. Capture Authorization Code")
    print("3. Capture Commit Message")
    print("4. Capture Review")
    print("5. Print Captured Values")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            capture_ticket()
        elif choice == "2":
            capture_authorization_code()
        elif choice == "3":
            capture_commit_message()
        elif choice == "4":
            capture_review()
        elif choice == "5":
            print_values()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
