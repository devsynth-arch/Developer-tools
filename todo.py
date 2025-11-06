#!/usr/bin/env python3
"""
Todo List Manager
A simple CLI todo list.
Usage: python todo.py [add <task> | list | done <index>]
"""

import sys
import json
import os

TODO_FILE = 'todo.json'

def load_todos():
    """Load todos from file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save todos to file."""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

def add_task(task):
    """Add a task."""
    todos = load_todos()
    todos.append({'task': task, 'done': False})
    save_todos(todos)
    print(f"Added: {task}")

def list_tasks():
    """List tasks."""
    todos = load_todos()
    for i, todo in enumerate(todos):
        status = '✓' if todo['done'] else ' '
        print(f"{i+1}. [{status}] {todo['task']}")

def mark_done(index):
    """Mark task as done."""
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]['done'] = True
        save_todos(todos)
        print(f"Marked done: {todos[index]['task']}")
    else:
        print("Invalid index.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add <task> | list | done <index>]")
        sys.exit(1)
    command = sys.argv[1]
    if command == 'add' and len(sys.argv) > 2:
        add_task(' '.join(sys.argv[2:]))
    elif command == 'list':
        list_tasks()
    elif command == 'done' and len(sys.argv) > 2:
        try:
            mark_done(int(sys.argv[2]) - 1)
        except ValueError:
            print("Invalid index.")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()