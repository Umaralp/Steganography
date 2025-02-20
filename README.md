# Secure Data Hiding in Images using Steganography

## 📌 Overview
This project implements image steganography using Python and OpenCV. It allows users to hide secret messages inside an image while ensuring security with passcode protection for decryption.

## 📂 Project Structure
🛡️ **encryption.py** – Encrypts a message inside an image and saves the output.

🔓 **decryption.py** – Decrypts the hidden message from the encrypted image.

📊 **Steganography-ppt.pptx** – Presentation explaining the project.

🖼️ **mypic.png** – The original image used for hiding the message.

🖼️ **encryptedImage.png** – The output image containing the hidden message.

🖼️ **Screenshot2025-02-20 153400.png** – Screenshots related to the project.

🔑 **passcode.txt** – Stores the passcode for decryption.

📄 **LICENSE** – Project license (GPL-3.0).

📖 **README.md** – Project documentation.

## ✨ Features
✔️ **Secure Message Hiding** – Stores text inside image pixels without noticeable changes.

✔️ **Passcode Protection** – Ensures only authorized users can decrypt the message.

✔️ **Lightweight & Fast** – Minimal performance overhead with quick encryption/decryption.

✔️ **Open Source** – Free to modify and expand under the GPL-3.0 license.

## ✨ Project Screenshot

![Project Screenshot](https://github.com/Umaralp/Steganography/blob/main/Screenshot%202025-02-20%20153400.png)

## 🚀 Installation & Usage

### 🔹 Prerequisites
Ensure you have Python installed along with the required libraries

[pip install opencv-python]

### 🔹 Encryption Process

1️⃣ Place an image (e.g., mypic.png) in the project folder.

2️⃣ Run the encryption script

3️⃣ Enter the secret message and set a passcode

4️⃣ The encrypted image (encryptedImage.png) is generated successfully.


### 🔹 Decryption Process

1️⃣ Run the decryption script

2️⃣ Enter the correct passcode.

3️⃣ The hidden message is revealed on the console.

## 📜 License

This project is licensed under the GNU GPL-3.0 License.

## 👨‍💻 Contributing

Clone the repository: git clone https://github.com/Umaralp/Steganography.git

Contributions are welcome! If you’d like to improve this project, feel free to fork the repository and submit a pull request.
