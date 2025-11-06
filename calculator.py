#!/usr/bin/env python3
"""
Simple Calculator
Evaluates basic math expressions.
Usage: python calculator.py <expression>
"""

import sys

def calculate(expression):
    """Calculate expression."""
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except:
        print("Invalid expression.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python calculator.py <expression>")
        sys.exit(1)
    calculate(sys.argv[1])

if __name__ == "__main__":
    main()