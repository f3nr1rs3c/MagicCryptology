import hashlib
import os
from pyfiglet import Figlet
from colorama import init, Fore

# MD5 Hash
def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# SHA1 Hash
def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

# SHA256 Hash
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# SHA384 Hash
def sha384_hash(text):
    return hashlib.sha384(text.encode()).hexdigest()

# SHA512 Hash
def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

# Binary Code
def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

input_text = "@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX"
binary_text = text_to_binary(input_text)

# Ceaser Cipher
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

# Morse Alphet
morse_alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}

def morse_alphabe(text):
    morse_code = ""
    for char in text.upper():
        if char in morse_alphabet:
            morse_code += morse_alphabet[char] + " "
        else:
            morse_code += "/ " # Eğer karakter morse alfabesinde yoksa bir boşluk ekler.
    return morse_code

# Base16
def base16(text):
    base16_result = text.encode('utf-8').hex().upper()
    return base16_result

# Base32
def base32(text):
    base32_result = text.encode('utf-8').hex().upper()
    return base32_result

# Base64
def base64(text):
    base64_result = base64.encode('utf-8').hex().upper()
    return base64_result

    
def main():
    f = Figlet(font='slant', width=100)
    print(Fore.GREEN + f.renderText('Magic Cryptology') + Fore.RESET)
    print(Fore.RED + "                      | - |  By : f3nr1r - Cyber Security | - |         " + Fore.RESET)

    while True:
        
        print("""

1) MD5
2) SHA1
3) SHA256
4) SHA384
5) SHA512
6) Binary Code
7) Morse Alphabet
8) Caesar Cipher
9) Base16
10) Base32
11) Base64
x) Exit

        """)
        
        process = input("Enter your process number: ")
        
        # MD5 Hash
        if process == '1':
            text = input("Enter Text: ")
            hashed_text = md5_hash(text)
            print(Fore.GREEN + "MD5 Hash Output:" + Fore.RESET, hashed_text)
        
        # SHA1 Hash
        elif process == '2':
            text = input("Enter Text: ")
            hashed_text = sha1_hash(text)
            print(Fore.GREEN + "SHA1 Output:" + Fore.RESET, hashed_text)
        
        # SHA256 Hash
        elif process == '3':
            text = input("Enter Text: ")
            hashed_text = sha256_hash(text)
            print(Fore.GREEN + "SHA256 Hash Output:" + Fore.RESET, hashed_text)
        
        # SHA384 Hash    
        elif process == '4':
            text = input("Enter Text: ")
            hashed_text = sha384_hash(text)
            print(Fore.GREEN + "SHA384 Hash Output: " + Fore.RESET, hashed_text)
        
        # SHA512 Hash      
        elif process == '5':
            text = input("Enter Text: ")
            hashed_text = sha512_hash(text)
            print(Fore.GREEN + "SHA512 Hash Output:" + Fore.RESET, hashed_text)
        
        # Binary
        elif process == '6':
            text = input("Enter Text: ")
            binary_text = text_to_binary(input_text)
            print(Fore.GREEN + "Binary Output: " + Fore.RESET, binary_text)
        
        # Morse Alfabet
        elif process == '7':
            text = input("Enter Text: ")
            morse_alpha = morse_alphabe(text)
            morse_text = morse_alphabe(input_text)
        
            print(Fore.GREEN + "Morse Code: " + Fore.RESET, morse_alpha)
            
        # Ceaser Encryption
        elif process == '8':
            text = input("Enter Text: ")
            shift = int(input("Enter Shift Amount: "))
            encrypted_text = caesar_cipher(text, shift)
            print(Fore.RED + "Encrypted Text:" + Fore.RESET, encrypted_text)
            decrypted_text = caesar_decipher(encrypted_text, shift)
            print(Fore.GREEN + "Decrypted Text:" + Fore.RESET, decrypted_text)
        
        # Base16
        elif process == '9':
            text = input("Enter Text: ")
            base16_text = base16(text)
            print(Fore.GREEN + "Base16 Output: " + Fore.RESET, base16_text)
        
        # Base32
        elif process == '10':
            text = input("Enter Text: ")
            base32_text = base32(text)
            print(Fore.GREEN + "Base32 Output: " + Fore.RESET, base32_text)
        
        # Base64
        elif process == '10':
            text = input("Enter Text: ")
            base64_text = base64(text)
            print(Fore.GREEN + "Base64 Output: " + Fore.RESET, base64)
                            
        # Exit Program
        elif process == 'x':
            print("Exiting The Program...")
            break
        
        else:
            print("Invalid option. Please try again.")
            print("python3 Magic_Cryptology.py")

if __name__ == "__main__":
    main()
