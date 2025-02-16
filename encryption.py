import cv2
import os

# Load the image
img = cv2.imread("mypic.png")  # Ensure the image exists

# Check if the image was loaded properly
if img is None:
    print("Error: Unable to load 'mypic.png'. Please check if the file exists.")
    exit()

msg = input("Enter secret message: ")
password = input("Set a passcode for decryption: ")

# Save passcode for verification
with open("passcode.txt", "w") as file:
    file.write(password)

# Character encoding dictionary
char_to_int = {chr(i): i for i in range(255)}

# Flatten the image array to store data sequentially
flat_img = img.flatten()

# Store message length in the first pixel
flat_img[0] = len(msg)

# Store the message in the pixel array
for i, char in enumerate(msg):
    flat_img[i + 1] = char_to_int[char]

# Reshape the image back to original shape
img_encrypted = flat_img.reshape(img.shape)

# Save the encrypted image
cv2.imwrite("encryptedImage.png", img_encrypted)
os.system("start encryptedImage.png")  # Opens the image (Windows), change for other OS

print("Message successfully encrypted into 'encryptedImage.png'.")
print("Remember your passcode for decryption!")
