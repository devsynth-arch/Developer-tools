#!/usr/bin/env python3
"""
File Renamer
Renames files in a directory with a pattern.
Usage: python file_renamer.py <directory> <old_pattern> <new_pattern>
"""

import sys
import os
import re

def rename_files(directory, old_pattern, new_pattern):
    """Rename files matching the pattern."""
    for filename in os.listdir(directory):
        if re.search(old_pattern, filename):
            new_name = re.sub(old_pattern, new_pattern, filename)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python file_renamer.py <directory> <old_pattern> <new_pattern>")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Directory {directory} not found.")
        sys.exit(1)
    rename_files(directory, sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()