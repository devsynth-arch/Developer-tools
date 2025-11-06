#!/usr/bin/env python3
"""
Code Line Counter
A tool to count lines of code in a directory, excluding comments and blank lines.
Usage: python line_counter.py <directory>
"""

import sys
import os
import re

def count_lines(file_path):
    """Count non-blank, non-comment lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except:
        return 0

    code_lines = 0
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            code_lines += 1
    return code_lines

def main():
    if len(sys.argv) != 2:
        print("Usage: python line_counter.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Directory {directory} not found.")
        sys.exit(1)

    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                lines = count_lines(file_path)
                total_lines += lines
                print(f"{file_path}: {lines} lines")

    print(f"\nTotal lines of code: {total_lines}")

if __name__ == "__main__":
    main()