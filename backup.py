#!/usr/bin/env python3
"""
Simple Backup
Copies files from source to backup directory.
Usage: python backup.py <source_dir> <backup_dir>
"""

import sys
import os
import shutil

def backup(source, backup):
    """Backup files."""
    if not os.path.exists(backup):
        os.makedirs(backup)
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(backup, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print(f"Backed up {source} to {backup}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <backup_dir>")
        sys.exit(1)
    source = sys.argv[1]
    backup_dir = sys.argv[2]
    if not os.path.isdir(source):
        print(f"Source {source} not found.")
        sys.exit(1)
    backup(source, backup_dir)

if __name__ == "__main__":
    main()