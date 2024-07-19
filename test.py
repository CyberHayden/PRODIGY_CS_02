from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

def load_image():
    filepath = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.bmp;*.gif")])
    image = Image.open(filepath)
    return image

def image_to_array(image):
    array = np.array(image)
    return array

def encrypt_array(array, key):
    encrypted_array = np.bitwise_xor(array, key)
    encrypted_array = (encrypted_array + key) % 256
    return encrypted_array.astype(np.uint8)

def decrypt_array(encrypted_array, key):
    decrypted_array = encrypted_array - key
    decrypted_array = np.bitwise_xor(decrypted_array, key)
    return decrypted_array.astype(np.uint8)

def save_image(array, path):
    image = Image.fromarray(array)
    image.save(path)

def main():
    root = tk.Tk()
    root.withdraw()

    action = input("Do you want to (E)ncrypt or (D)ecrypt an image? ")

    if action.lower() == 'e':
        key = int(input("Enter a key (0-255): "))
        image = load_image()
        array = image_to_array(image)
        encrypted_array = encrypt_array(array, key)
        save_image(encrypted_array, "encrypted_image.png")
        print("Image encrypted and saved as encrypted_image.png")
        print("Key:", key)
    elif action.lower() == 'd':
        key = int(input("Enter the key (0-255): "))
        image = load_image()
        array = image_to_array(image)
        decrypted_array = decrypt_array(array, key)
        save_image(decrypted_array, "decrypted_image.png")
        print("Image decrypted and saved as decrypted_image.png")
    else:
        print("Invalid input. Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()