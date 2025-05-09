import time
import re
from datetime import datetime

# File to monitor
file_path = '/Users/alrod/Development/2_7_WorkspaceSetup002/EnactorHome/cardAuthServer/IccReaderInfoCache.txt'  # Replace with the path to your file

# The line to search for and its replacement
search_line = "Verifone|275121825:Verifone:275121825:DECOMMISSIONED:false"
replace_line = "Verifone|275121825:Verifone:275121825:LIVE:false"

def get_timestamp():
    """Returns the current timestamp in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def update_file():
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the search line exists and replace it
        updated = False
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() == search_line:
                    file.write(replace_line + '\n')
                    updated = True
                else:
                    file.write(line)

        if updated:
            print(f"[{get_timestamp()}] Updated line in {file_path}")
        else:
            print(f"[{get_timestamp()}] No changes made to {file_path}")

    except Exception as e:
        print(f"[{get_timestamp()}] An error occurred: {e}")

def monitor_file():
    print(f"[{get_timestamp()}] Monitoring {file_path} for changes... Press Ctrl+C to stop.")
    try:
        while True:
            update_file()
            time.sleep(1)  # Check the file every second
    except KeyboardInterrupt:
        print(f"\n[{get_timestamp()}] Monitoring stopped.")

if __name__ == "__main__":
    monitor_file()