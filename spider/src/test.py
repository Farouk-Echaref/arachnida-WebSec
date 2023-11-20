#!/usr/bin/python3

from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def colorful_header():
    print(f"{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}=== Python Bot ==={Style.RESET_ALL}")

# Example usage
colorful_header()
print("Hello, this is your Python bot in action!")
