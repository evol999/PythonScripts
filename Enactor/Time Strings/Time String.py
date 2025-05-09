import os
import re
import pyperclip
from datetime import datetime

# Store time differences and timestamps in a list of tuples
time_format = "%Y-%m-%dT%H:%M:%S%z"
time_differences = []  # This will store the tuples (timestamp, time_difference)
previous_dt = None  # To hold the previous datetime for comparison
current_dt = None 


def display_menu():
    print("Menu:")
    print("1. Enter string time")
    print("2. Print results")
    # print("3. Capture Auth Code")
    # print("4. Generate Eclipse Message")
    # print("5. Generate console Command")
    print("0. Exit")

def enter_string_time():
    global previous_dt
    global time_differences
    current_dt = extract_time()
    if previous_dt is None:
        # No previous time to compare to, so time difference is None for the first entry
        time_differences.append((current_dt, None))
    else:
        # Calculate time difference with the previous timestamp
        time_difference = current_dt - previous_dt
        time_differences.append((current_dt, time_difference))
    
    # Update the previous_dt for the next iteration
    previous_dt = current_dt

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and Mac
    else:
        os.system('clear')
def extract_time():
    global current_dt
    global time_format
    string = pyperclip.paste()
    # Use regex to extract the time (HH:MM:SS format)
    time_match = re.search(r'T(\d{2}:\d{2}:\d{2})', string)

    if time_match:
        time = time_match.group(1)
        print("Extracted time:", time)
        # Get the current date
        current_date = datetime.now().date()
        # Combine the current date with the time string to form a full datetime object
        current_dt = datetime.strptime(f"{current_date} {time}", "%Y-%m-%d %H:%M:%S")

        # current_dt = datetime.strptime(full_datetime, time_format)
    else:
        print("No time found in the string.")

def print_results():
    for i, (ts, diff) in enumerate(time_differences):
        if diff is None:
            print(f"Timestamp {i}: {ts} | Time Difference: None (First timestamp)")
        else:
            print(f"Timestamp {i}: {ts} | Time Difference: {diff}")
    input("Press any key to continue...")


def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")
        clear_screen()

        if choice == "1":
            extract_time()
        elif choice == "2":
            print_results()
        # elif choice == "3":

        # elif choice == "4":

        # elif choice == "5":

        # elif choice == "6":
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()