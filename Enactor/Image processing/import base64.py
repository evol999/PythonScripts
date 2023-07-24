import base64
from PIL import Image, ImageOps

def encode_image(image_path, text_path):
    # Read the JPEG image as binary data
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Encode the image data as Base64
    encoded_data = base64.b64encode(image_data)

    # Save the Base64 encoded data to a text file
    with open(text_path, 'w') as file:
        file.write(encoded_data.decode('utf-8'))
    
    print("Image encoded and saved as 'encoded_image.txt'.")

def decode_image(text_path, image_path):
    # Read the Base64 encoded data from the text file
    with open(text_path, 'r') as file:
        encoded_data = file.read()

    # Decode the Base64 data
    decoded_data = base64.b64decode(encoded_data)

    # Save the decoded binary data as a JPEG image
    with open(image_path, 'wb') as file:
        file.write(decoded_data)
    
    print("Image decoded and saved as 'decoded_image.jpg'.")

def display_image_attributes(image_path):
    # Open the image
    image = Image.open(image_path)

    # Display the image attributes
    print("Image Attributes:")
    print("Format:", image.format)
    print("Size:", image.size)
    print("Mode:", image.mode)

# def resize_image(image_path, new_size):
#     # Open the image
#     image = Image.open(image_path)

#     # Resize the image
#     resized_image = image.resize(new_size)

#     return resized_image

def resize_image(image_path, new_width):
    # Open the image
    image = Image.open(image_path)

    # Calculate the new height while maintaining the aspect ratio
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    new_height = int(new_width / aspect_ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    return resized_image

def convert_to_jpeg(image):
    # Convert the image mode to RGB
    rgb_image = image.convert('RGB')

    return rgb_image

def save_image(image, output_path):
    # Save the image as JPEG
    image.save(output_path, 'JPEG')

    print("Image converted and saved as '{}'.".format(output_path))

def create_blank_image(size):
    # Create a new blank white image
    new_image = Image.new('RGB', size, color='white')

    return new_image

def insert_image(background_path, foreground_path, output_path):
    # Open the background and foreground images
    background = Image.open(background_path)
    foreground = Image.open(foreground_path)

    # Calculate the center position for the foreground image
    background_width, background_height = background.size
    foreground_width, foreground_height = foreground.size

    center_x = (background_width - foreground_width) // 2
    center_y = (background_height - foreground_height) // 2

    # Create a new image by pasting the foreground image onto the background image
    new_image = background.copy()
    new_image.paste(foreground, (center_x, center_y))

    # Save the resulting image
    new_image.save(output_path)

    print("Image with inserted foreground saved as '{}'.".format(output_path))

def invert_colors(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Invert the colors of the image
    inverted_image = ImageOps.invert(image)

    # Save the inverted image
    inverted_image.save(output_path)

    print("Image with inverted colors saved as '{}'.".format(output_path))

def create_midpoint_image(image_path, output_path, factor=0.5):
    # Open the image
    image = Image.open(image_path)

    # Invert the colors of the image
    inverted_image = ImageOps.invert(image)

    # Adjust the pixel values to create the midpoint image
    midpoint_image = Image.blend(image, inverted_image, factor)

    # Save the midpoint image
    midpoint_image.save(output_path)

    print("Midpoint image saved as '{}'.".format(output_path))

def extract_hex_from_encoded_key(key_path):
    # Read the encoded image data from file
    with open(key_path, 'r') as file:
        encoded_data = file.read()

    # Decode the Base64-encoded data
    decoded_data = base64.b64decode(encoded_data)
    

    # Convert the decoded data to hexadecimal string
    # hex_string = decoded_data.hex()
    hex_string = decoded_data.decode('ascii')

    # Print the hexadecimal string
    print("Hexadecimal string of the actual key data:")
    print(hex_string)
    # print(decoded_data)

def encode_key(key_path):
    # Read the encoded image data from file
    with open(key_path, 'r') as file:
        decoded_data = file.read()

    # decoded_data = decoded_data[:-1]
    print("Original ASCII string:")
    print(decoded_data)
    # hex_string = decoded_data.hex()
    # print(hex_string)

    # Decode the Base64-encoded data
    # binary_data = bytes.fromhex(decoded_data.rstrip())
    binary_data = bytes(decoded_data.rstrip(),'utf-8')
    print("String converted to binary:")
    print(binary_data)
    encoded_data = base64.b64encode(binary_data)
    

    # Convert the decoded data to hexadecimal string
    # hex_string = decoded_data.hex()
    # hex_string = encoded_data.decode('ascii')

    # Print the hexadecimal string
    print("Base64-encoded string:")
    # print(hex_string)
    print(encoded_data)

# Main menu loop
while True:
    print("Menu:")
    print("01. Encode image")
    print("02. Decode image")
    print("03. Display image attributes")
    print("04. Resize and convert image")
    print("05. Create a blank white image")
    print("06. Insert foreground image into background image")
    print("07. Invert colors of an image")
    print("08. Create midpoint image")
    print("09. Extract hex string from encoded key")
    print("10. Encode key")
    print("0. Exit")

    choice = input("Enter your choice (0-10): ")

    if choice == '1':
        image_path = 'final.jpg'
        text_path = 'final.txt'
        encode_image(image_path, text_path)

        image_path = 'inverted.jpg'
        text_path = 'finalInverted.txt'
        encode_image(image_path, text_path)

        image_path = 'midpoint.jpg'
        text_path = 'finalmidpoint.txt'
        encode_image(image_path, text_path)
    elif choice == '2':
        text_path = 'encoded_image.txt'
        image_path = 'decoded_image.jpg'
        decode_image(text_path, image_path)
        text_path = 'encoded_original01.txt'
        image_path = 'decoded_original01.jpg'
        decode_image(text_path, image_path)
        text_path = 'encoded_original02.txt'
        image_path = 'decoded_original02.jpg'
        decode_image(text_path, image_path)
        text_path = 'encoded_original03.txt'
        image_path = 'decoded_original03.jpg'
        decode_image(text_path, image_path)
    elif choice == '3':
        # image_path = input("Enter the path of the image: ")
        image_path = 'decoded_image.jpg'
        display_image_attributes(image_path)
    elif choice == '4':
        # image_path = input("Enter the path of the PNG image: ")
        # new_width = int(input("Enter the desired width: "))
        # new_height = int(input("Enter the desired height: "))
        # output_path = input("Enter the output file name: ")

        image_path = 'input.png'
        new_width = 320
        new_height = 395
        output_path = 'output.jpg'

        # image = resize_image(image_path, (new_width, new_height))
        image = resize_image(image_path, new_width)
        jpeg_image = convert_to_jpeg(image)
        save_image(jpeg_image, output_path)        
    elif choice == '5':
        # new_width = int(input("Enter the desired width: "))
        # new_height = int(input("Enter the desired height: "))
        # output_path = input("Enter the output file name: ")

        new_width = 320
        new_height = 395
        output_path = 'background.jpg'

        blank_image = create_blank_image((new_width, new_height))
        blank_image.save(output_path, 'JPEG')

        print("Blank white image created and saved as '{}'.".format(output_path))
    elif choice == '6':
        # background_path = input("Enter the path of the background image: ")
        # foreground_path = input("Enter the path of the foreground image: ")
        # output_path = input("Enter the output file name: ")

        background_path = 'background.jpg'
        foreground_path = 'output.jpg'
        output_path = 'final.jpg'

        insert_image(background_path, foreground_path, output_path)
    elif choice == '7':
        # image_path = input("Enter the path of the image: ")
        # output_path = input("Enter the output file name: ")

        image_path = 'final.jpg'
        output_path = 'inverted.jpg'

        invert_colors(image_path, output_path)
    elif choice == '8':
        # image_path = input("Enter the path of the image: ")
        # output_path = input("Enter the output file name: ")
        # factor = float(input("Enter the blend factor (0.0-1.0): "))

        image_path = 'final.jpg'
        output_path = 'midpoint.jpg'
        factor = 0.25
        create_midpoint_image(image_path, output_path, factor)
    elif choice == '9':
        # key_path = input("Enter the path of the encoded key: ")
        key_path = 'encodedKey.txt'
        extract_hex_from_encoded_key(key_path)

    elif choice == '10':
        # key_path = input("Enter the path of the encoded key: ")
        key_path = 'decodedKey.txt'
        encode_key(key_path)

    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.\n")

