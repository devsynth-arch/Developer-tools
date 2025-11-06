#!/usr/bin/env python3
"""
Word Counter
Counts words in a text file.
Usage: python word_counter.py <file>
"""

import sys

def count_words(file_path):
    """Count words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        words = text.split()
        print(f"Words: {len(words)}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <file>")
        sys.exit(1)
    count_words(sys.argv[1])

if __name__ == "__main__":
    main()