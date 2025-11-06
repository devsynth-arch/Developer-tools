#!/usr/bin/env python3
"""
Note Taker
Simple note taking CLI.
Usage: python notes.py [add <note> | list | clear]
"""

import sys
import json
import os

NOTES_FILE = 'notes.json'

def load_notes():
    """Load notes."""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    """Save notes."""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

def add_note(note):
    """Add note."""
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print(f"Added: {note}")

def list_notes():
    """List notes."""
    notes = load_notes()
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def clear_notes():
    """Clear notes."""
    save_notes([])
    print("Notes cleared.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python notes.py [add <note> | list | clear]")
        sys.exit(1)
    command = sys.argv[1]
    if command == 'add' and len(sys.argv) > 2:
        add_note(' '.join(sys.argv[2:]))
    elif command == 'list':
        list_notes()
    elif command == 'clear':
        clear_notes()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()