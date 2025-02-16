import cv2
import os

# Load the encrypted image
img = cv2.imread("encryptedImage.png")  # Ensure the encrypted image exists

# Check if the image was loaded properly
if img is None:
    print("Error: Unable to load 'encryptedImage.png'. Ensure encryption was successful.")
    exit()

# Load the saved passcode
try:
    with open("passcode.txt", "r") as file:
        saved_password = file.read().strip()
except FileNotFoundError:
    print("Passcode file not found! Decryption cannot proceed.")
    exit()

# Ask the user for the passcode
entered_password = input("Enter passcode for decryption: ")

if entered_password != saved_password:
    print("Access Denied! Incorrect passcode.")
    exit()

# Character decoding dictionary
int_to_char = {i: chr(i) for i in range(255)}

# Flatten the image array to read data sequentially
flat_img = img.flatten()

# Read message length from the first pixel
msg_length = flat_img[0]

# Extract the hidden message
message = ''.join(int_to_char[flat_img[i + 1]] for i in range(msg_length))

print("Decrypted Message:", message)
