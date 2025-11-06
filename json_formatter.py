#!/usr/bin/env python3
"""
JSON Formatter
A tool to format and validate JSON files.
Usage: python json_formatter.py <json_file>
"""

import sys
import json

def format_json(file_path):
    """Format and validate JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        formatted = json.dumps(data, indent=2)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
        print(f"Formatted {file_path}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python json_formatter.py <json_file>")
        sys.exit(1)
    format_json(sys.argv[1])

if __name__ == "__main__":
    main()