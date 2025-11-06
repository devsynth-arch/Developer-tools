#!/usr/bin/env python3
"""
Weather Fetcher
Fetches weather using wttr.in (no API key needed).
Usage: python weather.py <city>
"""

import sys
import requests

def get_weather(city):
    """Get weather."""
    try:
        response = requests.get(f'https://wttr.in/{city}?format=3')
        if response.status_code == 200:
            print(response.text.strip())
        else:
            print("City not found.")
    except requests.RequestException:
        print("Error fetching weather.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    get_weather(sys.argv[1])

if __name__ == "__main__":
    main()