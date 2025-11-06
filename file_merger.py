#!/usr/bin/env python3
"""
Text File Merger
Merges multiple text files into one.
Usage: python file_merger.py <output_file> <input_file1> <input_file2> ...
"""

import sys

def merge_files(output_file, input_files):
    """Merge files."""
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file in input_files:
                with open(file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')
        print(f"Merged into {output_file}")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python file_merger.py <output_file> <input_file1> <input_file2> ...")
        sys.exit(1)
    merge_files(sys.argv[1], sys.argv[2:])

if __name__ == "__main__":
    main()