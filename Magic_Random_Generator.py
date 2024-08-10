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
    print(Fore.LIGHTMAGENTA_EX + f.renderText('Magic Passwords') + Fore.RESET)
    print(Fore.RED + "             | - | Made By : Fenrir - Cyber Security Specialist | - |         " + Fore.RESET)

def print_menu():
    print("""

{0}1){2} Lowercase Characters
{0}2){2} Uppercase Characters
{0}3){2} Number Characters
{0}4){2} Special Characters
{0}5){2} Random Characters
{0}6){2} Exit

""".format(Fore.RED, "0", Fore.RESET, "1", "2", "3", "4", "5", "6", "7", "8", "9", Fore.RESET))

def generate_password(length, characters):
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input(Fore.GREEN + "Enter Transaction Number: " + Fore.RESET)

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
                length = int(input(Fore.BLUE + "Enter password length: " + Fore.RESET))
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
