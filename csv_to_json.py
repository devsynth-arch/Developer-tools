#!/usr/bin/env python3
"""
CSV to JSON Converter
Converts CSV files to JSON.
Usage: python csv_to_json.py <csv_file> <json_file>
"""

import sys
import csv
import json

def convert_csv_to_json(csv_file, json_file):
    """Convert CSV to JSON."""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Converted {csv_file} to {json_file}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py <csv_file> <json_file>")
        sys.exit(1)
    convert_csv_to_json(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()