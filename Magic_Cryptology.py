import hashlib
import os
from pyfiglet import Figlet
from colorama import init, Fore

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def main():
    f = Figlet(font='slant', width=100)
    print(Fore.GREEN + f.renderText('Magic Cryptology') + Fore.RESET)
    print(Fore.RED + "     | - |  By : f3nr1r - Cyber Security | - |         " + Fore.RESET)

    while True:
        
        print("""

1) MD5
2) SHA1
3) SHA256
4) SHA512
5) Caesar Encryption
6) Exit

        """)
        
        process = input("Enter your process number: ")

        if process == '1':
            text = input("Enter Text: ")
            hashed_text = md5_hash(text)
            print(Fore.GREEN + "MD5 Hash Output:" + Fore.RESET, hashed_text)
        
        elif process == '2':
            text = input("Enter Text: ")
            hashed_text = sha1_hash(text)
            print(Fore.GREEN + "SHA1 Output:" + Fore.RESET, hashed_text)
        
        elif process == '3':
            text = input("Enter Text: ")
            hashed_text = sha256_hash(text)
            print(Fore.GREEN + "SHA256 Hash Output:" + Fore.RESET, hashed_text)
            
        elif process == '4':
            text = input("Enter Text: ")
            hashed_text = sha512_hash(text)
            print(Fore.GREEN + "SHA512 Hash Output:" + Fore.RESET, hashed_text)
        
        elif process == '5':
            text = input("Enter Text: ")
            shift = int(input("Enter Shift Amount: "))
            encrypted_text = caesar_cipher(text, shift)
            print(Fore.RED + "Encrypted Text:" + Fore.RESET, encrypted_text)
            decrypted_text = caesar_decipher(encrypted_text, shift)
            print(Fore.GREEN + "Decrypted Text:" + Fore.RESET, decrypted_text)
        
        elif process == '6':
            print("Exiting The Program...")
            break
        
        else:
            print("Invalid option. Please try again.")
            print("python3 cryptology.py")

if __name__ == "__main__":
    main()