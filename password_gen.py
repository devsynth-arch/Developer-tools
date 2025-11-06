#!/usr/bin/env python3
"""
Password Generator
Generates secure passwords.
Usage: python password_gen.py [length]
"""

import sys
import random
import string

def generate_password(length=12):
    """Generate a random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    length = 12
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print("Invalid length.")
            sys.exit(1)
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()