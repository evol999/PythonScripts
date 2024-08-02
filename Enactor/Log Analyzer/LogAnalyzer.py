import os
import re

# Define the regular expression pattern for the time expression
# time_pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}')
time_pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}')

# Define the input file path
# input_file_path = '/Users/alrod/Tickets/The Works/1056/pdc/pdc.log'  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/The Works/1056 (1)/pdc/pdc.log"  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/PAY-1829/POS/common.log.2024-01-07.1"  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/PAY-1829/PDC/pdc.log.2024-01-07.1"  # Update with your input file path
# input_file_path = r"/Users/alrod/Development/RC1_The_Works/EnactorHome/pdc/logs/OldLogs/pdc.log.2024-02-13.1"  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/PAY-1900 STUCK AUTHO SCREEN/right.txt"  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/PAY-1900 STUCK AUTHO SCREEN/wrong.txt"  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/PAY-1900 STUCK AUTHO SCREEN/other.txt"  # Update with your input file path
# input_file_path = r"/Users/alrod/Temp/LOGS_T650/PDC.TXT"  # Update with your input file path
# input_file_path = r"/Users/alrod/Temp/LOGS_T650/PDC01.TXT"  # Update with your input file path
# input_file_path = r"/Users/alrod/Tickets/PAY-1900 STUCK AUTHO SCREEN/Wrong002.txt"  # Update with your input file path
input_file_path = r"/Users/alrod/Tickets/PAY-1900 STUCK AUTHO SCREEN/Right002.txt"  # Update with your input file path

# Extract the directory path and file name from the input file path
input_dir, input_filename = os.path.split(input_file_path)

# Create the subdirectory if it doesn't exist
output_dir = os.path.join(input_dir, 'results')
os.makedirs(output_dir, exist_ok=True)

# Create the output file path
output_file_path = os.path.join(output_dir, input_filename)

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    line_number = 0
    # Loop through each line in the input file
    for line in input_file:
        line_number += 1
        # Check if the line starts with a matching time expression
        # writeLine = (time_pattern.match(line) and "Licence has expired:" not in line and "[ICCDioneCommandThread-" in line) or ("ErrorCode:'Disconnected'" in line)
        # writeLine = "theme on the bridge. The set" not in line and "Proxy has not been configured." not in line and not line.startswith('	at ') and " WARN " not in line and "ERROR com.enactor.coreUI.swing.thinClient.SwingThinClientResourceManager" not in line and "response code: 403" not in line and "Null imageUrl is returned" not in line and "Error loading image" not in line and not line.startswith('	... ') and not line.startswith('javax.imageio.')
        # writeLine = "Enactor Dummy Licence" not in line and not line.startswith('	at ') and not line.startswith('        at ')
        # writeLine = time_pattern.match(line) and "Enactor Dummy Licence" not in line and "Licence has expired:" not in line
        # writeLine = time_pattern.match(line) and "Licence has expired:" not in line
        # writeLine = "13:24" in line or "13:25" in line
        # writeLine = line_number > 8547 and line_number < 9583
        # writeLine = line.startswith('Received event ')
        # writeLine = "VerifonePSDK" in line or line.startswith('Received event ')
        # writeLine = "icc." in line or line.startswith('Received event ')
        # writeLine = "icc.verifone.psdk" in line or line.startswith('Received event ')
        # writeLine = "PerformEncryptionCommand" in line or line.startswith('Received event ')
        # writeLine = ("PerformEncryptionCommand" not in line and "400_825" not in line) or line.startswith('Received event ')
        # writeLine = ("PerformEncryptionCommand" not in line and "400_825" not in line and "'GET_DATA'" not in line) or line.startswith('Received event ')
        # writeLine = ("Thread-6" in line or "Thread-278" in line) or line.startswith('Received ')
        # writeLine = ("Thread-" in line) or line.startswith('Received ')
        # writeLine = ("Thread-" in line or "PSDK respond" in line) or line.startswith('Received ')
        writeLine = ("received: " in line)
        if writeLine:
            # If it does, write the line to the output file
            output_file.write(line)

# Close the files
input_file.close()
output_file.close()
