#!/usr/bin/env python

import os 
from colorama import init, Fore
from pyfiglet import Figlet
import string
import random

# Initialize Colorama
init()

def clear_screen():
    os.system("clear")

def print_banner():
    f = Figlet(font='slant', width=100)
    print(Fore.LIGHTMAGENTA_EX + f.renderText('Magic Passswords') + Fore.RESET)
    print(Fore.RED + "             | - | Made By : f3nr1r - Cyber Security | - |         " + Fore.RESET)

def print_menu():
    print("""

1) Lowercase Characters
2) Uppercase Characters
3) Number Characters
4) Special Characters
5) Random Characters
6) Exit

""")

def generate_password(length, characters):
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input("Enter Transaction Number: ")

        if choice == '1':
            characters = string.ascii_lowercase
        elif choice == '2':
            characters = string.ascii_uppercase
        elif choice == '3':
            characters = string.digits
        elif choice == '4':
            characters = string.punctuation
        elif choice == '5':
            characters = string.ascii_letters + string.digits + string.punctuation
        elif choice == '6':
            print("Enter Transaction Number:...")
            break
        else:
            input("Invalid selection! Press any key to continue...")
            continue

        while True:
            try:
                length = int(input("Enter password length: "))
                if length <= 0:
                    raise ValueError("Enter a positive integer.")
                break
            except ValueError as ve:
                print("Error:", ve)

        password = generate_password(length, characters)
        print("Generated Password:", password)
        input("Press any key to continue...")

if __name__ == "__main__":
    main()
