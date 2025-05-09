import requests
from datetime import datetime

def format_bin(bin_number, max_length=6):
    """
    Truncates the bin_number to max_length and replaces extra characters with '*'.
    """
    if len(bin_number) > max_length:
        return bin_number[:max_length] + '*' * (len(bin_number) - max_length)
    return bin_number

def make_rest_request(base_url, acquirer_id, merchant_id, bin_number, base_amount, pos_entry_mode, output_file="results.txt"):
    # Format the bin_number for display
    formatted_bin = format_bin(bin_number)
    
    # Construct the full URL using the provided parameters
    url = f"{base_url}/acquirers/{acquirer_id}/merchants/{merchant_id}/dccoffers?&bin={bin_number}&baseamount={base_amount}"

    # Add pos_entry_mode to the URL if it is not None
    if pos_entry_mode is not None:
        url += f"&posentrymode={pos_entry_mode}"
    
    # Construct the display URL with the formatted bin
    display_url = f"{base_url}/acquirers/{acquirer_id}/merchants/{merchant_id}/dccoffers?&bin={formatted_bin}&baseamount={base_amount}"

    if pos_entry_mode is not None:
        display_url += f"&posentrymode={pos_entry_mode}"
    
    # Record the time and date of the request
    request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Make the GET request
    try:
        # Prepare the output message
        output_message = (
            # f"{description}\n"
            f"Request Time: {request_time}\n"
            f"ACQ ID: {acquirer_id}\n"
            f"MID: {merchant_id}\n"
            f"BIN: {format_bin(bin_number)}\n"
            f"Base amount: {base_amount}\n"
            f"Request URL (Mangled PAN): {display_url}\n"
        )
        
        # Print the output to the console
        print(output_message)

        # Write the output to a file
        with open(output_file, "a") as file:
            file.write(output_message)


        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()

        response_message = (
            f"Response Status Code: {response.status_code}\n"
            f"Response Body: {response.json()}\n"
            "----------------------------------------\n"
        )

        print(response_message)
        
        # Write the output to a file
        with open(output_file, "a") as file:
            file.write(response_message)
    
    except requests.exceptions.RequestException as e:
        # Simplify the error message
        error_message = f"An error occurred: {e.response.status_code} {e.response.reason}\n----------------------------------------\n"
        print(error_message)
        with open(output_file, "a") as file:
            file.write(error_message)

if __name__ == "__main__":
    # Base URL of the API
    base_url = "https://dhstest2.fexcodccapps.com/dhsv2"
    
    # Test cases with descriptions
    test_cases = [
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600011",
            "bin_number": "4761730000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600011",
            "bin_number": "4761730000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600011",
            "bin_number": "4761730000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600007",
            "bin_number": "4761730000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600007",
            "bin_number": "4761730000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600007",
            "bin_number": "4761730000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600045",
            "bin_number": "4761730000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600045",
            "bin_number": "4761730000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600045",
            "bin_number": "4761730000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },


        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600011",
            "bin_number": "5253580002",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600011",
            "bin_number": "5253580002",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600011",
            "bin_number": "5253580002",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600007",
            "bin_number": "5253580002",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600007",
            "bin_number": "5253580002",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600007",
            "bin_number": "5253580002",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600045",
            "bin_number": "5253580002",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600045",
            "bin_number": "5253580002",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong ACQ ID",
            "acquirer_id": "TST",
            "merchant_id": "982600045",
            "bin_number": "5253580002",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },



        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "4761730000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "4761730000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "4761730000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "4761730000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "4761730000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "4761730000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "4761730000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "4761730000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should be successful",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "4761730000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },


        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "5253580002",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "5253580002",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "5253580002",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "5253580002",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "5253580002",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "5253580002",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "5253580002",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "5253580002",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "This case should fail because of wrong BIN",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "5253580002",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },


        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "5140180000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "5140180000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "5140180000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "5140180000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "5140180000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "5140180000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "5140180000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "5140180000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 1. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "5140180000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "2223000000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "2223000000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600011",
            "bin_number": "2223000000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "2223000000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "2223000000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600007",
            "bin_number": "2223000000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "2223000000",
            "base_amount": "100.01",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "2223000000",
            "base_amount": "100.02",
            "pos_entry_mode": "071",
        },
        {
            "description": "Testing Mastercard BIN 2. This should be successful.",
            "acquirer_id": "HAR",
            "merchant_id": "982600045",
            "bin_number": "2223000000",
            "base_amount": "100.03",
            "pos_entry_mode": "071",
        },

    ]
    
    # Output file name
    output_file = "results.txt"
    
    # Test each case
    for i, case in enumerate(test_cases, start=1):
        output_message = f"Test Case {i:03d}: {case['description']}\n"
        # Print the test case number and description
        print(output_message)

        # Write the output to a file
        with open(output_file, "a") as file:
            file.write(output_message)
        
        # Make the REST request
        make_rest_request(
            base_url,
            acquirer_id=case["acquirer_id"],
            merchant_id=case["merchant_id"],
            bin_number=case["bin_number"],
            base_amount=case["base_amount"],
            pos_entry_mode=case["pos_entry_mode"],
            output_file=output_file,
        )