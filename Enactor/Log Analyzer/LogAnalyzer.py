import os
import re

# Define the regular expression pattern for the time expression
time_pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}')

# Define the input file path
# input_file_path = '/Users/alrod/Tickets/The Works/1056/pdc/pdc.log'  # Update with your input file path
input_file_path = r"/Users/alrod/Tickets/The Works/1056 (1)/pdc/pdc.log"  # Update with your input file path

# Extract the directory path and file name from the input file path
input_dir, input_filename = os.path.split(input_file_path)

# Create the subdirectory if it doesn't exist
output_dir = os.path.join(input_dir, 'results')
os.makedirs(output_dir, exist_ok=True)

# Create the output file path
output_file_path = os.path.join(output_dir, input_filename)

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Loop through each line in the input file
    for line in input_file:
        writeLine = (time_pattern.match(line) and "Licence has expired:" not in line and "[ICCDioneCommandThread-" in line) or ("ErrorCode:'Disconnected'" in line)
        # writeLine = time_pattern.match(line) and "Licence has expired:" not in line
        # Check if the line starts with a matching time expression
        if writeLine:
            # If it does, write the line to the output file
            output_file.write(line)

# Close the files
input_file.close()
output_file.close()
