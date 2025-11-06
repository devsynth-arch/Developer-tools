#!/usr/bin/env python3
"""
File Finder
Finds files by name in a directory.
Usage: python file_finder.py <directory> <filename>
"""

import sys
import os

def find_files(directory, filename):
    """Find files."""
    for root, dirs, files in os.walk(directory):
        if filename in files:
            print(os.path.join(root, filename))

def main():
    if len(sys.argv) != 3:
        print("Usage: python file_finder.py <directory> <filename>")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Directory {directory} not found.")
        sys.exit(1)
    find_files(directory, sys.argv[2])

if __name__ == "__main__":
    main()